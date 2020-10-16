<h1 align="center">
  <br>
  <a href="https://github.com/n0obit4/Namazu_Ransom"><img src="https://raw.githubusercontent.com/n0obit4/Fuzzpy/master/Logo.png" alt="Namazu Ransom Logo" border="0" width="180"></a>
  <br>
  Namazu Ransom
  <br>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Release-v1.0-Red.svg">
  <img src="https://img.shields.io/badge/License-APACHE%202.0-brightyellow.svg">
  <img src="https://img.shields.io/badge/Tested_on-Linux-yellow.svg">
</p>

## Introduction

Namazu Ransom is a mini ransomware that i create with EDUCATIONAL PURPOSE. This ransomware encrypt all files into a folder with a symetric cipher, that means that do you use the same key to encrypt and decrypt data.

As it is for educational purposes I have placed both the crypt and the decryptor.

## How it work

Namazu Ransom use a aes cipher with 256 bits and cbc cryptography Since it uses Fernet and it uses the aes-256-cbc composition to encrypt data.
See more about Fernet [Here](https://cryptography.io/en/latest/fernet/).

To encrypt data do you need specify the key generate by the crypter.

If you want encrypt all personal files into a linux system, you only need chanhe the folder un the **rw.encrypt_files()** by a **/home**.

## Cryptor demostration
