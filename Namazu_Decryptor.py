from cryptography.fernet import Fernet
import sys,os,glob

__author__  = 'n0obit4'
__date__    = '29/09/2020'
__version__ = 'v1.0'

class decrypter:

	def load_key(self):
		return open(sys.argv[1], 'rb').read()

	def decrypt(self,key,dir):
		for x in os.walk(dir):
			for item in glob.glob(os.path.join(x[0], '*')):
				if os.path.isfile(item):
					llave = Fernet(key)
					crypt = open(item, 'rb')
					file = llave.decrypt(crypt.read())
					out = open(item, 'wb')
					out.write(file)

if __name__ == '__main__':
	try:
		decrypt = decrypter()
		decrypt.decrypt(decrypt.load_key(),'Directory_to/decrypt')
	except:
		print('-Error to load key\n\nUsage: python3 {} key.key'.format(__file__))
