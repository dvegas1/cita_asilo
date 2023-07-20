# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:47:49 2023

@author: PC
"""
import base64
import re
import datetime
import constants
import logging
import traceback
import inspect
import random
import hashlib
import string

class utils():

    def __init__(self, logger=None, data={}, dataUser={}):
        self.logger = logger
        self.data = data
        self.dataUser = dataUser
        print("Clase utilis: Logger:%s,data:%s,DataUser:%s","NO" if logger is None else "SI","NO" if len(data) == 0 else "SI","NO" if len(dataUser) == 0 else "SI")

    async def encriptbase64(self, encoded_data):
        encoded_strings = [s.encode() for s in encoded_data]
        joined_strings = b"".join(encoded_strings)
        base64_encoded = base64.b64encode(joined_strings)
        print("base64_encoded", base64_encoded)
        return base64_encoded

    async def decriptbase64(self, encoded_data):
        base64_decoded = base64.b64encode(encoded_data)
        decoded_strings = base64_decoded.split(b"")
        decoded_array = [s.decode() for s in decoded_strings]
        print("base64_decoded", decoded_array)
        return decoded_array

    async def validateName(self, nombre_apellido):
        patron = r'^[a-zA-ZÁÉÍÓÚáéíóúñÑ ]{7,40}$'
        resultado = re.match(patron, nombre_apellido)
        if resultado:
            return True
        else:
            return False

    async def validateReference(self, reference):
        patron = r'^[a-zA-Z0-9]{3,40}$'
        resultado = re.match(patron, reference)
        if resultado:
            return True
        else:
            return False

    async def validateDoc(self, doc):
        patron = r'^[a-zA-Z0-9]{6,40}$'
        resultado = re.match(patron, doc)
        if resultado:
            return True
        else:
            return False

    async def validate_Birt(self, birt):
        now = datetime.datetime.now()
        current_year = now.year
        patron = r'^[0-9]{4}$'
        resultado = re.match(patron, birt)
        if resultado and (int(birt) <= int(current_year)):
            return True
        else:
            return False

    async def validate_username(self, username):
        if (username == ""):
            return False
        patron = r'^(?!_)(?!.*_{2})[a-zA-Z0-9_]{4,20}(?<!_)$'
        resultado = re.match(patron, username)
        if resultado:
            return True
        else:
            return False

    async def validate_password(self, password):
        patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$'
        resultado = re.match(patron, password)
        if resultado:
            return True
        else:
            return False

    async def validate_email(self, password):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        resultado = re.match(patron, password)
        if resultado:
            return True
        else:
            return False

    async def getlogger(self):
        logger = logging.getLogger(__name__)
        
        if not logger.hasHandlers():
            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s %(levelname)s %(chat_id)s %(token)s [%(usernameAsiloBot)s:%(usernameTelegram)s] %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
            )
            handler = logging.StreamHandler()
            handler.setLevel(logging.INFO)
            handler.setFormatter(formatter)

            logger.addHandler(handler)

            fileHandler = logging.FileHandler(
                filename='logasilo_test.log', encoding='utf-8')
            fileHandler.setFormatter(formatter)
            fileHandler.setLevel(level=logging.INFO)

            logger.addHandler(fileHandler)

        self.logger = logger
        return logger

    async def setUserTelegram(self, update):
        user = "Desconocido"
        usernameTelegram = "Desconocido"
        try:
            if (update.message and update.message.chat.id):
                user = update.message.from_user
                usernameTelegram = user.username

            if update.callback_query and update.callback_query.message.chat.id:
                #chatId = update.callback_query.message.chat.id
                user = update.callback_query.message.from_user
                usernameTelegram = user.username
            
            extra_params = self.dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy())
            extra_params.update({constants.USERNAME_TELEGRAM: usernameTelegram})  
            self.dataUser.update({constants.EXTRA_PARAMS:extra_params})
            
            return self.dataUser

        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.dataUser.get(
                constants.EXTRA_PARAMS))

    async def setTokenUser(self):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy()))
        md5 = hashlib.md5()
        caracteres = string.ascii_letters + string.digits
        numero_aleatorio = ''.join(random.choice(caracteres) for _ in range(30)).join(':g')
        md5.update(numero_aleatorio.encode('utf-8'))

        extra_param = self.dataUser.get(
            constants.EXTRA_PARAMS,constants.extra_params.copy())

        token = md5.hexdigest()
        extra_params = self.dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy())
        extra_params.update({constants.TOKEN: token})  
        self.dataUser.update({constants.EXTRA_PARAMS: extra_param})

        self.logger.info(constants.END, extra=self.dataUser.get(
            constants.EXTRA_PARAMS))

        return self.dataUser
            

    async def setLogger(self, logger):
        self.logger = logger
