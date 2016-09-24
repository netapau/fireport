#!/usr/bin/python

#######################################################
#                 FirePort - By Wlan01                #
#######################################################
# @Website: https://programacaogratuita.wordpress.com #
#######################################################

import socket
import os
import os.path
import sys
from time import sleep

def fp_connect(ip, port):
	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.settimeout(1)
	sk.connect((str(ip), int(port)))
	if sk == 0:
		return False
	else:
		return True
	sk.close()
def log_file(string):
	if not os.path.exists("log.txt"):
		file = open("log.txt", "w")
		file.close()
	log = open("log.txt", "a")
	log.write(string + "\n")	
	log.close()
def reset_log():
	file = open("log.txt", "w")
	file.close()
def __main__(ip):
	i = 1
	while i <= 65535:
		port = int(i)
		try:
			if fp_connect(ip, port) == True:
				print("Porta " + str(i) + " aberta no IP " + str(ip))
				log_file("Porta " + str(i) + " aberta no IP " + str(ip))
			else:
				log_file("Porta " + str(i) + " fechada no IP " + str(ip))
		except socket.error:
			log_file("Porta " + str(i) + " fechada no IP " + str(ip))
		i += 1
def main():
	if len(sys.argv) > 2 or len(sys.argv) < 2:
		print("Ajuda: \n")
		print("python fireport.py [IP]")
		sys.exit(1)
	else:
		print(" _____ _          ____            _  ")
		print("|  ___(_)_ __ ___|  _ \ ___  _ __| |_ ")
		print("| |_  | | '__/ _ \ |_) / _ \| '__| __|")
		print("|  _| | | | |  __/  __/ (_) | |  | |_ ")
		print("|_|   |_|_|  \___|_|   \___/|_|   \__|\n")
		print("Iniciando o script...")
		sleep(1)
		__main__(sys.argv[1])
def fp_init():
	try:
		main()
	except KeyboardInterrupt:
		reset_log()
		print("[*] Fechando o script...")
		sleep(1)
		sys.exit(1)
	except: 
		reset_log()
		print("[*] Ocorreu um erro inesperado.")
		sys.exit(1)
fp_init()
reset_log()
