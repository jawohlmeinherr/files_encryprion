import pyAesCrypt
import string
import secrets
import sys
import os

def encrypt(file, password):
	buffer_size = 512*1024

	pyAesCrypt.encryptFile(str(file), str(file) + '.crp', password, buffer_size)

	os.remove(file)

def decrypt(file, password):
	buffer_size = 512*1024

	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)

	os.remove(file)

def dir_encrypt(dir, password):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)

		if os.path.isfile(path):
			encrypt(path, password)
		else:
			dir_encrypt(dir, password)

def dir_decrypt(dir, password):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)

		if os.path.isfile(path):
			decrypt(path, password)
		else:
			dir_decrypt(dir, password)

def keygen(length):
	alphabet = string.ascii_letters + string.digits
	password = ''.join(secrets.choice(alphabet) for i in range(length))

while True:
	choice = input('Action> ')

	if choice == '1':
		filename = input('Filename> ')
		password = input('Password> ')

		encrypt(filename, password)

	elif choice == '2':
		filename = input('Filename> ')
		password = input('Password> ')

		decrypt(filename, password)

	elif choice == '3':
		exit()

	else:
		continue