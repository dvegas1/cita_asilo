# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:47:49 2023

@author: PC
"""
import base64


class utils():
    
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
