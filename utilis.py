# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:47:49 2023

@author: PC
"""
import base64
import re
import datetime



class utils():
    
    def __init__(self):
        print("Clase utilis")
    
    async def encriptbase64(self, encoded_data):
            encoded_strings = [s.encode() for s in encoded_data]
            joined_strings = b"".join(encoded_strings)
            base64_encoded =  base64.b64encode(joined_strings)
            print("base64_encoded",base64_encoded)
            return base64_encoded
    
    async def decriptbase64(self, encoded_data):
            base64_decoded = base64.b64encode(encoded_data)
            decoded_strings = base64_decoded.split(b"")
            decoded_array = [s.decode() for s in decoded_strings]        
            print("base64_decoded",decoded_array)
            return decoded_array
    
    async def validateName(self,nombre_apellido):
        patron = r'^[a-zA-ZÁÉÍÓÚáéíóúñÑ ]{7,40}$'
        resultado = re.match(patron, nombre_apellido)
        if resultado:
                return True
        else:
                return False
        
    async def validateReference(self,reference):
        patron = r'^[a-zA-Z0-9]{3,40}$'
        resultado = re.match(patron, reference)
        if resultado:
                return True
        else:
                return False
        
    async def validateDoc(self,doc):
        patron = r'^[a-zA-Z0-9]{6,40}$'
        resultado = re.match(patron, doc)
        if resultado:
                return True
        else:
                return False      
       
    async def validate_Birt(self,birt):
        now = datetime.datetime.now()
        current_year = now.year
        patron = r'^[0-9]{4}$'
        resultado = re.match(patron, birt)
        if resultado and (int(birt) <= int(current_year)):
                return True
        else:
                return False
        
    async def validate_username(self,username):
        if(username == ""):
                return False
        patron = r'^(?!_)(?!.*_{2})[a-zA-Z0-9_]{4,20}(?<!_)$'
        resultado = re.match(patron, username)
        if resultado:
                return True
        else:
                return False     


    async def validate_password(self,password):
        patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$'
        resultado = re.match(patron, password)
        if resultado:
                return True
        else:
                return False  
        
        
    async def validate_email(self,password):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        resultado = re.match(patron, password)
        if resultado:
                return True
        else:
                return False  