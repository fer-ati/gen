#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
	
	BY FER - ATI
	Module Filter Color From Coloroma
	
	!@# -> -> Follow Me -> -> https://github.com/fer-ati

'''

import colorama as co

class C:
	
	blu = co.Fore.BLUE         #@
	cyan = co.Fore.CYAN        #@
	rosso = co.Fore.RED        #@
	verde = co.Fore.GREEN      #@
	giallo = co.Fore.YELLOW    #@
	bianco = co.Fore.WHITE     #@
	magenta = co.Fore.MAGENTA  #@
	resetta = co.Fore.RESET    #@
	
	blu_b = co.Back.BLUE        #@
	cyan_b = co.Back.CYAN       #@
	rosso_b = co.Back.RED       #@
	verde_b = co.Back.GREEN     #@
	giallo_b = co.Back.YELLOW   #@
	bianco_b = co.Back.WHITE    #@
	magenta_b = co.Back.MAGENTA #@
	resetta_b = co.Back.RESET   #@
	
	al_re = co.Fore.RESET + co.Back.RESET
	
	def olori(f):
		''' Color Print  '''
    
		if f == 1:
			print(blu)
		
		elif f == 2:
			print(cyan)
		
		elif f == 3:
			print(rosso)
		
		elif f == 4:
			print(verde)
		
		elif f == 5:
			print(giallo)
		
		elif f == 6:
			print(bianco)
		
		elif f == 7:
			print(magenta)
		
		else:
			print(resetta)
	
	def bac(b):
		###########################@
		blu = co.Back.BLUE        #@
		cyan = co.Back.CYAN       #@
		rosso = co.Back.RED       #@
		verde = co.Back.GREEN     #@
		giallo = co.Back.YELLOW   #@
		bianco = co.Back.WHITE    #@
		magenta = co.Back.MAGENTA #@
		resetta = co.Back.RESET   #@
		
		if b == 1:
			print(blu)
		
		elif b == 2:
			print(cyan)
		
		elif b == 3:
			print(rosso)
		
		elif b == 4:
			print(verde)
		
		elif b == 5:
			print(giallo)
		
		elif b == 6:
			print(bianco)
		
		elif b == 7:
			print(magenta)
		
		else:
			print(resetta)

class CA:

	def quad():
		print("[" + co.Fore.GREEN + "+" + co.Fore.RESET +"]") 
	
	def catalogo():
		x = [C.rosso,C.bianco,C.cyan,C.giallo,C.verde,C.magenta,C.blu,C.resetta]
		
		for i in x:
			print(f"Prova123 {i}")


if __name__ == "__main__":
	CA.catalogo()


''' '''









