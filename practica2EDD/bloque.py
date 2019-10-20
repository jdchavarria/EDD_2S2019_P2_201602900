import hashlib
import json
import csv
import os
from datetime import datetime

results = []
index = 0;
ph = ' '

class Bloque:
	#now = datetime.now()
	#print(now.strftime("%d-%m-%Y::%H:%M:%S"))
	def __init__(self, ind, has, pre, dat, time ):
		self.next = None
		self.previous = None
		self.hash = has
		self.previos_hash = pre
		self.index = ind
		self.timestamp = time 
		self.data = dat

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

	
	
	def add_first(self, index, has, prehas,dato, time):
		temporal = Bloque(index, has, prehas, dato, time)
		if self.vacia()==True: 
			self.head = temporal
			self.cola = temporal
		else:
			temporal.next = self.head
			self.head.previous = temporal
			self.head = temporal
			
	#def MostrarInicio_Fin(self):
	#	if self.vacia() != True:
	#		auxiliar = self.head
	#		while auxiliar != None:
	#			tener = auxiliar.hash
				#print(tener)
				#print(auxiliar.hash)
	#			auxiliar = auxiliar.next

	def encrypt_string(self, seguro):
		sha_encryption = hashlib.sha256(seguro.encode()).hexdigest()
		return sha_encryption

	def lectu(self, leer):
		var =''
		contador = 1
		with open(leer)as file:
			reader = csv.reader(file, delimiter=';')
			for row in reader:
				var += row[1]
			if self.vacia()==True:
				ph = '0000'
				index = 0
				now = datetime.now()
				suma = str(str(index)+str(now.strftime("%d-%m-%Y::%H:%M:%S"))+var+ph)
				has = self.encrypt_string(suma)
			else:
				auxiliar = self.head
				while auxiliar.next is not None:
					auxiliar = auxiliar.next
					if auxiliar == self.cola:
						ph = auxiliar.hash
						index = int(auxiliar.index)+1
				now = datetime.now()
				suma = str(str(index)+str(now.strftime("%d-%m-%Y::%H:%M:%S"))+var+ph)
				has = self.encrypt_string(suma)



	#def convertir_json(self, tiempo, indice, clave, pre_clave, dato):


			

	def escuchar(self):
		permiso= str(input("ingrese la opcion TRUE, FALSE, JSON"))
		if permiso == "true":
			print("se añadira el bloque")
			#self.add_first(index, has, ph, var, now)
		elif permiso == "false":
			print("no se añade el bloque")
		else: 
			print("se analiza bloque")
			self.comprobar(permiso)


	def comprobar(self, bloque):
		#CONVERTIR ESE BLOQUE QUE VIENE DE JSON EN PARTES PARA GUARDAR EN VARIABLES QUE LUEGO SE 
		#INGRESAN EN LA LISTA AL RECIBIR TRUE
		temporal = self.head
		clave = ''
		while temporal.next is not None:
			temporal = temporal.next
			if temporal == self.cola:
				clave = temporal.hash
		if bloque == clave:
			return 'true'
		else: 
			return 'false'
		print("analizar el bloque entrante")


	def crear_bloque(self):
		os.system('cls')
		archivo_aper = str(input("ingrese el nombre del archivo: "))
		self.lectu(archivo_aper)



	def menu(self):
		while True:
			os.system('cls')
			print("1. Insert block")
			print("2. Select block")
			print("3. Reports")
			print("4. Exit")
			opcion = input("ingrese una opcion ")
			if opcion == "1":
				self.crear_bloque()
			elif opcion == "2":
				self.add_first()
				self.MostrarInicio_Fin()
				print(self.tener)
				print("2222")
			elif opcion == "3":
				print("3333")
			elif opcion == "4":
				break
	

lista = ListaE()
lista.menu()
#lista.lectu('prueba.csv')







#string = 'Estructuras de Datos'
#print(lista.encrypt_string('Convert this text to sha-256 and place it in the answer'))
#lista.add_first(SHA-256(pre1+ind1, pre1, ind1, time1