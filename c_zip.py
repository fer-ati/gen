#!/usr/bin/env python3   
# -*- coding: utf-8 -*-    

import os                #@
import zipfile           #@ 
import subprocess as sp  #@

def verifica():
	x = list(os.uname())
	b = None
	
	if x[0] == "Linux":	
		b = 1
	
	else:
		b = 0
	
	return b
	
def fai():
	passw = str(input("Password zip = "))
	nome_zip = str(input("Nome zip File = "))
	fil = str(input("Path file or directory = "))
	
	sp.run([
	 
	 f"zip -r -P {passw} {nome_zip} {fil}  "
	 
	],shell=True)

if __name__ == "__main__":
	x = str(input("avvio zip [y,n] = ")).upper()
	
	if x == "Y":
		
		if verifica() == 1:
			fai()
		
		elif verifica() == 0:
			print("Script non compatibile con systema")
			quit()
	
	else:
		quit()

''' '''
