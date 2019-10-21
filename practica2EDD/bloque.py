import hashlib
import json
import csv
import os
from datetime import datetime

results = []
index = 0;
ph = ' '
cadena = ' '

texto_envio = ' '

has1 = ' '
pre1 = ' '
tiempo1 = ' '
indice1 = 0
info1 = ' '
name1 = ' '

class Bloque:
	#now = datetime.now()
	#print(now.strftime("%d-%m-%Y::%H:%M:%S"))
	def __init__(self, nombre, ind, has, pre, dat, time ):
		self.next = None
		self.previous = None
		self.hash = has
		self.previos_hash = pre
		self.index = ind
		self.timestamp = time 
		self.data = dat
		self.clase = nombre

	def VerNodo(self):
		return self.hash

class ListaE:
	palabra = 'Estructuras de Datos'
	tener = ''
	def __init__(self):
		self.head = None
		self.cola = None

	def vacia(self):
		if self.head == None:
			return True
		else: 
			return False

	
	
	def add_first(self,name, index, has, prehas,dato, time):
		temporal = Bloque(name, index, has, prehas, dato, time)
		if self.vacia() == True:
			self.head = temporal
			self.cola = temporal
		else:
			temporal.next =None
			temporal.previous = self.cola
			self.cola.next = temporal
			self.cola = temporal
			
	def MostrarInicio_Fin(self):
		if self.vacia() != True:
			auxiliar = self.head
			while auxiliar != None:
				#tener = auxiliar.hash
				#print(tener)
				print(auxiliar.hash)
				print(auxiliar.index)
				print(auxiliar.previos_hash)
				auxiliar = auxiliar.next
	def Graphviz_Block(self):
		if self.head == None:
			print("The list is empty")
		else:
			file = open('ListaEnlazada.dot', 'w')
			file.write('digraph secondGraph{\n')
			file.write('node [shape=record];\n')
			file.write('rankdir=LR;\n')
			temporal = self.head
			count = 0
			while temporal is not None:
				txt = 'Class='+str(temporal.clase)+'TimeStamp='+str(temporal.timestamp)+'PHASH='+str(temporal.previos_hash)+'HASH='+str(temporal.hash)
				file.write('node{} [label=\" {} \"];\n'.format(count, txt))
				count += 1
				file.write('node{} -> node{};\n'.format(count-1,count))
				file.write('node{} -> node{};\n'.format(count, count-1))
				temporal = temporal.next
				#if temporal == self.cola:
				#	file.write('node{} [label=\" {} \"];\n'.format(count, txt))
				#	file.wsrite('}')
			file.close()
			os.system("\"C:\\Program Files (x86)\\Graphviz2.26.3\\bin\\dot.exe\" -Tpng ListaEnlazada.dot -o  ListaEnlazada.png")
			os.system("start ListaEnlazada.png")
    

	def encrypt_string(self, seguro):
		sha_encryption = hashlib.sha256(seguro.encode()).hexdigest()
		return sha_encryption

	def lectu(self, leer):
		var =''
		contador = 1
		global index
		global ph
		auxiliar = self.head
		with open(leer)as file:
			reader = csv.reader(file, delimiter=';')
			for row in reader:
				var = var+";"+row[1]
		separador = var.split(sep=';')
		clase = separador[1]
		data = separador[2]
		#print("la clase: "+ str(clase)+" "+"data: "+ str(data))
		if self.vacia() == True:
			print("entro aqui y si ejecuta")
			ph = '0000'
			index = 0
			now = datetime.now()
			suma = str(str(index)+str(now.strftime("%d-%m-%Y::%H:%M:%S"))+clase+data+ph)
			has = self.encrypt_string(suma)
			self.convertir_json(clase,str(now.strftime("%d-%m-%Y::%H:%M:%S")),index,has,ph,data)
			#self.add_first(clase, index, has, ph, data, now)
		else:
			while auxiliar is not None:
				if auxiliar == self.cola:
					ph = auxiliar.hash
					index = int(auxiliar.index)+1
					auxiliar = auxiliar.next
				else:
					auxiliar = auxiliar.next

			now = datetime.now()
			suma = str(str(index)+str(now.strftime("%d-%m-%Y::%H:%M:%S"))+clase+data+ph)
			has = self.encrypt_string(suma)
			self.convertir_json(clase,str(now.strftime("%d-%m-%Y::%H:%M:%S")),index,has,ph,data)
			#self.add_first(clase, index, has, ph, data, now)



	def convertir_json(self, name, tiempo, indice, clave, pre_clave, dato):
		data = {}
		global cadena
		data['INDEX'] = indice
		data['TIMESTAMP'] = tiempo
		data['CLASS'] = name
		data['DATA'] = dato
		data['PREVIOUSHASH'] = pre_clave
		data['HASH'] = clave
		with open('archivo.json', 'w') as file:
			json.dump(data,file)
			cadena = json.dumps(data)
		#print(cadena)
		#return str(cadena)
		#self.des(cadena)


	def mostrar_carrusel(self):
		temporal = self.head
		if self.vacia()==True:
			print("la lista esta vacia ")
		else:
			while temporal is not None:
				os.system('cls')
				eleccion = str(input("oprima un 4 para avanzar a la izquieda y un  6 para avanzar a la derecha"))
				if eleccion == "6":
					print("INDEX: "+str(temporal.index))
					print("TIMESTAMP: "+ str(temporal.timestamp))
					print("DATA: "+ str(temporal.data))
					print("PREVIOUSHASH:" +str(temporal.previos_hash))
					print("HASH: "+str(temporal.hash))
					temporal = temporal.next
				elif eleccion == "4":
					print("INDEX: "+str(temporal.index))
					print("TIMESTAMP: "+ str(temporal.timestamp))
					print("DATA: "+ str(temporal.data))
					print("PREVIOUSHASH:" +str(temporal.previos_hash))
					print("HASH: "+str(temporal.hash))
					temporal = temporal.previous

	def des(self, cadenita):
		d = json.loads(cadenita)
		ind = d["INDEX"]
		tiem = d["DATA"]
		print(" ")
		print(str(ind) + str(tiem))			

	def comprobar(self, bloque):
		global has1
		global pre1
		global tiempo1
		global indice1
		global info1
		global name1

		d1 = json.loads(bloque)
		indice1 = d1["INDEX"]
		tiempo1 = d1["TIMESTAMP"]
		name1 = d1["CLASS"]
		info1 = d1["DATA"]
		pre1 = d1["PREVIOUSHASH"]
		has1 = d1["HASH"]

		temporal = self.head
		clave = ''
		if self.vacia() == True:
			return 'true'
		else:
			while temporal is not None:
				if temporal == self.cola:
					clave = temporal.hash
					temporal = temporal.next
				else:
					temporal = temporal.next
			if pre1 == clave:
				return 'true'
			else: 
				return 'false'
		#print("analizar el bloque entrante")


	def crear_bloque(self):
		os.system('cls')
		archivo_aper = str(input("ingrese el nombre del archivo: "))
		self.lectu(archivo_aper)



	def menu(self):
		enviar = ' '
		global texto_envio
		while True:
			os.system('cls')
			print("1. Insert block")
			print("2. Select block")
			print("3. Reports")
			print("4. Exit")
			opcion = input("ingrese una opcion ")
			if opcion == "1":
				self.crear_bloque()
				texto_envio = cadena
				#return enviar
				os.system("PAUSE")
			elif opcion == "2":
				#self.add_first()
				self.mostrar_carrusel()
				#print(self.tener)
				#print("2222")
				os.system("PAUSE")
			elif opcion == "3":
				self.Graphviz_Block()
				#self.MostrarInicio_Fin()
				os.system("PAUSE")
			elif opcion == "4":
				break
		return texto_envio
	

lista = ListaE()
lista.menu()
#lista.lectu('prueba.csv')







#string = 'Estructuras de Datos'
#print(lista.encrypt_string('Convert this text to sha-256 and place it in the answer'))
#lista.add_first(SHA-256(pre1+ind1, pre1, ind1, time1