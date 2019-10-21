# Python program to implement client side of chat room.
import socket
import select
import sys
#import json
import bloque
texto_enviar = None

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

	read_sockets = select.select([server], [], [], 1)[0]
	import msvcrt
	if msvcrt.kbhit(): read_sockets.append(sys.stdin)

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
			msj = message.decode('utf-8')
			print(message.decode('utf-8'))
			if msj == "true":
				bloque.lista.add_first(bloque.name1, bloque.indice1, bloque.has1, bloque.pre1, bloque.info1, bloque.tiempo1) #INSERTO EL BLOQUE CON LOS DATOS DEL JSON
				print("recibido true ")
			elif msj == "false":
				print("bloque denegado")
			else:
				#ANALIZAR EL JSON
				print("entro un json")
				#mi_texto = message.decode('utf-8')
				#texto_enviar = str(bloque.lista.comprobar(mi_texto))    #EL METODO DE ANALIZAR PONGO DE PARAMETRO MI_JON
				#print("enviar respuesta: "+texto_enviar)
				#server.sendall(texto_enviar.encode('utf-8'))

		else:
			message = sys.stdin.readline()
			mi_json = str(bloque.lista.menu())    #IGUALAR AL MENU PRINCIPAL
			if mi_json is not "":
				print(mi_json)
				server.sendall(mi_json.encode('utf-8'))
				sys.stdout.write("<You>")
				sys.stdout.write(message)
			sys.stdout.flush()
server.close()
