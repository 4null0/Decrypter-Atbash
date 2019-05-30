
import argparse  

#Colores
rd='\033[1;31m'
gr='\033[1;32m'
xx='\033[0m'

# Parse the target options 
parser = argparse.ArgumentParser() 
parser.add_argument("-c", "--cadenita", help="Cadena a descifrar")

args = parser.parse_args() 

if args.cadenita:
	cadena = args.cadenita
else:
	print "\n"+rd+"El argumento: [-c|--cadena], es obligatorio\n"+xx
	exit()


if __name__ == "__main__":
	
	Diccionario = [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]]

	Mensaje = ""
	
	for c in range(len(cadena)):
		Control="0"
		for i in range(len(Diccionario[0])):
			if cadena[c] == Diccionario[0][i]:
				Mensaje += Diccionario[1][i]
				Control = "1"
						
		if Control == "0":
			Mensaje += cadena[c]			
				
			
print "\nEl mensaje ha quedado: "+gr+str(Mensaje)
