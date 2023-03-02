# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import nest_asyncio
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    helpers,
)
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    PicklePersistence,
    filters,
    ConversationHandler,
    MessageHandler,
)
from telegram import __version__ as TG_VER
from typing import Dict
import datArray_cites
import testListDesplegable
import json
import telegram
import constants
import utilis
import base64
import re
from telegram.error import TimedOut
from telegram.error import NetworkError
import requests
import random
import time
import datetime
import time

CHOOSING, TYPING_REPLY, TYPING_CHOICE, BIO, SIGNUP, DOCUMENT, SIGNUP, TOKEN = range(
    8)


class citaAsilobot:

    application = ""
    token = "5940401924:AAHUZEP6BtTOWPk2Zvy5uQOatI8b8JySVu8"
    update = ""
    context = ""
    bot = telegram.Bot(token="5940401924:AAHUZEP6BtTOWPk2Zvy5uQOatI8b8JySVu8")
    arraysCites = datArray_cites.array_cites()
    newSelect = ""
    text_Loading = "🔤🔤🔤🔤🔤🔤🔤🔤"

    dat = {
        "provinciaGeneral": -1,
        "sede": -1,
        "tramite_oficina": -1,
        "tramite_cuperto_policial": -1,
        "typeDoc": -1,
        "doc": "",
        "name": "",
        "birth": -1,
        "country": -1,
        "plans": -1,
        "action": -1,
        "payment": False,
        "TypePayment": -1,
        "reference_payment": "",
        "sucess": False,
        constants.USERNAME: "",
        constants.PASSWORD: ""
    }

    dat1 = {
        "provinciaGeneral": 2,
        "sede": 0,
        "tramite_oficina": 0,
        "tramite_cuperto_policial": 0,
        "typeDoc": 0,
        "doc": "19452357",
        "name": "Darwin Vegas",
        "birth": 1990,
        "country": 1,
        "plans": 1,
        "action": -1,
        "payment": False,
        "TypePayment": -1,
        "reference_payment": "",
        "sucess": False,
        constants.USERNAME: "",
        constants.PASSWORD: ""
    }
    chaIds = -1
    optionValidate = -1
    optionValidat_Text = ""
    usernameTelegram = "-"
    usernameAsiloBot = "-"
    chatSend = ""
    chatMsgUser = []
    url = "http://localhost:3004/server"
    tokeUser = ""
    tokenAsiloBot = ""
    extra_params = {"tokeUser": "S/T","usernameAsiloBot": "-","usernameTelegram": "-"}
    chat_id = ''
    responseSingup = ''
    isLogin = False
    blockUser = False
    
   

    # optionValidate:0=doc
    # optionValidate:1=name
    # optionValidate:2=birth
    # optionValidate:3=reference_payment

    try:
        from telegram import __version_info__
    except ImportError:
        __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

    if __version_info__ < (20, 0, 0, "alpha", 1):
        raise RuntimeError(
            f"This example is not compatible with your current PTB version {TG_VER}. To view the "
            f"{TG_VER} version of this example, "
            f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
        )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(tokeUser)s [%(usernameAsiloBot)s:%(usernameTelegram)s] %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    
    logger.info("                 ", extra=extra_params)
    logger.info("                 ", extra=extra_params)
    logger.info("                 ", extra=extra_params)
    logger.info("                 ", extra=extra_params)
    logger.info("Inicio asiloBot.", extra=extra_params)
    
    async def LogoutUser(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        
        self.update = update
        
        self.logger.info(constants.START, extra=self.extra_params)
        
        
        await self.setIdChat()
        
        if(self.usernameAsiloBot == "" or self.tokenAsiloBot == ""):
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_NOT_LOGIN_TEXT, -1)
        else:
            self.isLogin = False
            self.token = ""
            self.tokenAsiloBot = ""
            self.usernameAsiloBot = ""
            self.tokeUser = ""
            self.dat[constants.USERNAME] = ""
            self.dat[constants.PASSWORD] = ""
            
            
            await self.setTokenUser()
            
            await self.setUserTelegram()
    
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.SUCESS_USER_LOGOUT_SUCESS_TEXT)
    
            self.logger.info(constants.END, extra=self.extra_params)
        
    async def loginAsiloBot(self):
        self.logger.info(constants.START, extra=self.extra_params)
        
        if(self.dat['username'] != "" and self.dat[constants.PASSWORD] != ""):
            payload = "username="+self.dat['username']+"&password="+self.dat[constants.PASSWORD]
            headers = {"Content-Type": "application/x-www-form-urlencoded"}

            response = requests.request(
                "POST", self.url + "/users_asilobot/loginAsiloBot", headers=headers, data=payload
            )
            _response = json.loads(response.text)
            
            self.logger.info(_response,extra=self.extra_params)
            
            await self.registerUser_validate(_response)
            
            
        else:
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_LOGOUT_SUCESS_TEXT)
            self.isLogin = True
            await self.validateLoginUser()
            
            
        self.logger.info(constants.END, extra=self.extra_params)
        
        
        
    async def validateLoginUser(self):
        self.logger.info(constants.START, extra=self.extra_params)
        error = False
        self.isLogin = True
        

        try:
            if self.dat[constants.USERNAME] == "":
                error = True
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_USERNAME_TEXT, 4)
                return False
                
            if self.dat[constants.PASSWORD] == "":
                error = True
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_PASSWORD_TEXT, 5)
                return False
            
            if(not error):
                await self.loginAsiloBot()
            
        except TimedOut as timedOutError:
              error = True
              self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
              error = True
              self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
              error = True
              self.logger.error(errors, extra=self.extra_params)

        if error:
            await self.clearMsg(True, self.update)
            await self.clearMsgText(True, self.update)
            await self.validateLoginUser()

        self.logger.info(constants.END, extra=self.extra_params)
        
        
    async def setIdChat(self):
        update_jsonStr = json.dumps(self.update.to_dict())
        update_json = json.loads(update_jsonStr)
        
        await self.clearMsg(True, self.update)
        await self.clearMsgText(True, self.update)

        if(self.chat_id == ''):
           self.chat_id = update_json['message']['chat']['id']

    async def LoginUser(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await self.setUserTelegram()
        
        if(self.blockUser):
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.BLOCKED_USER_TEXT, -1)
        
        self.logger.info(constants.START, extra=self.extra_params)
        self.update = update
        self.context = context
        
        self.isLogin = True
        
        await self.setIdChat()
        
        if(self.tokenAsiloBot != "" and self.usernameAsiloBot != ""):
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_ALREADY_LOGIN.replace("{username}", self.usernameAsiloBot), -1)
            return
        
        
        if(self.dat[constants.USERNAME] == "" or self.dat[constants.PASSWORD] == ""):
            validLogin = await self.validateLoginUser()
        
            
        self.logger.info(constants.END, extra=self.extra_params)

    
    def timBlockUser(self, _json):
        target_time = datetime.datetime.now() + datetime.timedelta(minutes=constants.BLOCKED_USER_MINUTES_BLOCK)
        while True:
            self.blockUser = True
            # obtén la diferencia de tiempo restante
            remaining_time = target_time - datetime.datetime.now()
            
            # si el tiempo restante es menor que un minuto, detén el contador
            if remaining_time.total_seconds() < 60:
                print(f"¡Tiempo finalizado! {remaining_time}")
                self.blockUser = False
                break
            
            # muestra el tiempo restante
            print("Tiempo restante: ", remaining_time)
            
            # espera un minuto antes de volver a verificar
            time.sleep(60)
        
        
    async def registerUser_validate(self, _json):
        self.logger.info(constants.START, extra=self.extra_params)

        sucess_register = True
        try:
            tokenSignup = _json["token"]
            self.tokenAsiloBot = tokenSignup
                
            self.tokeUser = str(tokenSignup[0:8]) + str(tokenSignup[-8:len(tokenSignup)])
                
            self.usernameAsiloBot = self.dat['username']
                
            self.extra_params = {"tokeUser": self.tokeUser,"usernameAsiloBot":self.usernameAsiloBot,"usernameTelegram":self.usernameTelegram}
        
            if(self.isLogin):
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.SUCESS_USER_LOGIN_TEXT, -1)
            else:
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.USER_REGISTER_SUCESS_TEXT, -1)
                self.logger.info(constants.USER_REGISTER_SUCESS_TEXT, extra=self.extra_params)
            
            return True
                
        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=self.extra_params)
            sucess_register = False
        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.extra_params)
            sucess_register = False
        except Exception as errors:
            self.logger.error(errors, extra=self.extra_params)
            sucess_register = False
            
        
        try:
            _json["errors"]
            sucess_register = False
        except Exception as errors:
            self.logger.error(errors, extra=self.extra_params)
            
        if(not sucess_register):
            try:
                await self.clearMsg(True, self.update)
                await self.clearMsgText(True, self.update)
                
                error_msg = _json["errors"]["msg"]
                
                if error_msg == constants.WARNING_API_USERNAME_ALREADY_EXIST:
                    self.dat[constants.USERNAME] = ""
                    await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_API_USERNAME_ALREADY_EXIST_TEXT, -1)
                    await self.validateFieldTextUser()
                
                if error_msg == constants.WARNING_API_WRONG_PASSWORD or error_msg == constants.WARNING_API_USER_DOES_NOT_EXIST:
                    self.dat[constants.USERNAME] = ""
                    self.dat[constants.PASSWORD] = ""
                    await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_API_WRONG_PASSWORD_TEXT, -1)
                    await self.validateLoginUser()
                        
                if error_msg == constants.BLOCKED_USER:
                    self.timBlockUser()
                    self.blockUser = True
                    self.dat[constants.USERNAME] = ""
                    self.dat[constants.PASSWORD] = ""
                    await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_API_WRONG_PASSWORD_TEXT, -1)
                    await self.sendMessageTelChatId(self.chat_id, self.update, constants.BLOCKED_USER_TEXT, -1)
                    return False
                    
            except Exception as errors:
                self.logger.error(errors, extra=self.extra_params)
            
            return False

    async def sendMessageTelChatId(self, chat_id, update, optionValidat_Text="", optionValidate=-1, add_clearList=True):
       sucess = False

       try:
          while(not sucess):
             self.optionValidate = optionValidate
             self.optionValidat_Text = optionValidat_Text
             self.chatSend = await self.bot.send_message(
                 chat_id=chat_id, text=optionValidat_Text
             )

             if(add_clearList):
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

             sucess = True
             self.logger.info(sucess, extra=self.extra_params)
       except TimedOut as timedOutError:
           self.logger.error(timedOutError, extra=self.extra_params)
           sucess = False
       except NetworkError as networkError:
           self.logger.error(networkError, extra=self.extra_params)
           sucess = False
       except Exception as errors:
           self.logger.error(errors, extra=self.extra_params)
           sucess = False

    async def sendesplegableButton(self, dat=[], case=-1, sucess_code=-1, _paginatorLisColumm=2, _paginatorGeneral=10, _add_title_text="", actions=0, page=-1):
       error = False
       try:
           self.newSelect = testListDesplegable.testList(
               self.token,
               self.update,
               self.context,
               dat,
               case,
               sucess_code,
               _paginatorLisColumm,
               _paginatorGeneral,
               _add_title_text,
               logger=self.logger,
               extra_params=self.extra_params
               )

           await self.newSelect.select(actions, page)

       except TimedOut as timedOutError:
           self.logger.error(timedOutError, extra=self.extra_params)
           error = True
       except NetworkError as networkError:
           self.logger.error(networkError, extra=self.extra_params)
           error = True
       except Exception as errors:
           if(str(errors).find('object has no attribute')):
              self.logger.warning(errors, extra=self.extra_params)
           else:
              error = True
              self.logger.error(errors, extra=self.extra_params)

       if(error):
         time.sleep(3)
         await self.sendesplegableButton(dat=dat,case=case,sucess_code=sucess_code,_paginatorLisColumm=_paginatorLisColumm,_paginatorGeneral=_paginatorGeneral,_add_title_text=_add_title_text)

    async def registerUser(self) -> int:
       self.logger.info(constants.START, extra=self.extra_params)
       error = False
       try:
           update_jsonStr = json.dumps(self.update.to_dict())
           update_json = json.loads(update_jsonStr)

           #$.message.chat.id
           self.logger.info(update_json, extra=self.extra_params)
           self.logger.info(update_json['message']
                            ['chat']['id'], extra=self.extra_params)

           #message_id = update.callback_query.message.message_id

           if(self.chat_id == ''):
              self.chat_id = update_json['message']['chat']['id']

           _payload = ""

           if(self.dat['username'] != ''):
               _payload += "username=" + self.dat['username'] + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['provinciaGeneral'] != -1):
               _payload += "provinciaGeneral=" + \
                   str(self.dat['provinciaGeneral']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['sede'] != -1):
               _payload += "sede=" + str(self.dat['sede']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['tramite_oficina'] != -1):
               _payload += "tramite_oficina=" + \
                   str(self.dat['tramite_oficina']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['tramite_cuperto_policial'] != -1):
               _payload += "tramite_cuperto_policial=" + \
                   str(self.dat['tramite_cuperto_policial']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['typeDoc'] != -1):
               _payload += "typeDoc=" + str(self.dat['typeDoc']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['doc'] != ''):
               _payload += "doc=" + self.dat['doc'] + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['name'] != ''):
               _payload += "name=" + self.dat['name'] + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['birth'] != -1):
               _payload += "birth=" + str(self.dat['birth']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat['country'] != -1):
               _payload += "country=" + str(self.dat['country']) + "&"
           else:
              await self.validateFieldTextUser()
              return

           if(self.dat[constants.PASSWORD] != ''):
               _payload += "password=" + self.dat[constants.PASSWORD] + "&"
           else:
              await self.validateFieldTextUser()
              return

           _payload += "role=" + "user" + "&"

           payload = _payload
           caracter_remove = payload[-1:len(payload)]
           if(caracter_remove == '&'):
                payload = payload[:-1]

           self.logger.info(payload, extra=self.extra_params)

           headers = {"Content-Type": "application/x-www-form-urlencoded",
                      "Accept-Language": "en"}

           await self.sendMessageTelChatId(self.chat_id, self.update, constants.USER_REGISTER_PROCESS_TEXT, -1)

       except TimedOut as timedOutError:
           error = True
           self.logger.error(timedOutError, extra=self.extra_params)
       except NetworkError as networkError:
           error = True
           self.logger.error(networkError, extra=self.extra_params)
       except Exception as errors:
           error = True
           self.logger.error(errors, extra=self.extra_params)

       if(error):
           await self.registerUser
           
       sucess_Singup = False
       
       try:
           errorRequest = False
           self.responseSingup = requests.request(
               "POST", self.url + "/users_asilobot/registerAsiloBot", headers=headers, data=payload)

           await self.clearMsg(True, self.update)
           await self.clearMsgText(True, self.update)

           responseSingoToJson = json.loads(self.responseSingup.text)

           self.logger.info(responseSingoToJson, extra=self.extra_params)

           sucess_Singup = await self.registerUser_validate( responseSingoToJson)

       except TimedOut as timedOutError:
           errorRequest = True
           self.logger.error(timedOutError, extra=self.extra_params)
       except NetworkError as networkError:
           errorRequest = True
           self.logger.error(networkError, extra=self.extra_params)
       except Exception as errors:
           errorRequest = True
          # if(str(error).find("NoneType")):
           self.logger.error(errors, extra=self.extra_params)

       if(errorRequest and not sucess_Singup):
           _text_intentns = ["Primera", "Segunda", "Tercera y ultima"]

           error_intents = False
           await self.clearMsg(True, self.update)
           await self.clearMsgText(True, self.update)
           self.responseSingoToJson = ''
           for i in range(0, 3):

               await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_INTENTS_TEXT.replace("{}", _text_intentns[i]), -1)
               time.sleep(5)

               try:
                   self.responseSingoToJson = requests.request(
                       "POST", self.url + "/users_asilobot/registerAsiloBot", headers=headers, data=payload)

                   error_intents = False

                   _response = json.loads(self.responseSingoToJson.text)

                   await self.registerUser_validate( _response)

               except Exception as errors:
                 self.logger.error(errors, extra=self.extra_params)
                 error_intents = True

               if(self.responseSingoToJson != "" and not error_intents):
                   await self.clearMsg(True, self.update)
                   await self.clearMsgText(True, self.update)

                   _response = json.loads(self.responseSingoToJson.text)

                   self.logger.info(_response, extra=self.extra_params)

                   await self.registerUser_validate( _response)
                   break

           if(error_intents):
               time.sleep(3)
               await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_TEXT_GENERAL_TEXT, -1)

       self.logger.info(constants.END, extra=self.extra_params)

    async def setLogger(self):
       self.logger.info(constants.START, extra=self.extra_params)
       self.formatter = logging.Formatter(
           "%(asctime)s %(levelname)s %(tokeUser)s %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
       )
       self.handler.setFormatter(self.formatter)
       self.logger.info(constants.END, extra=self.extra_params)

    async def setTokenUser(self):
       self.logger.info(constants.START, extra=self.extra_params)

       if self.tokeUser == "":
          self.tokeUser = str(random.randint(9999, 99999999999999)) + ":g"
          self.extra_params['usernameAsiloBot'] = ""

    async def setUserTelegram(self):
       try:
           user = self.update.message.from_user
           self.user = user
           self.usernameTelegram = self.user.username
           self.extra_params["usernameTelegram"] = self.usernameTelegram
       except Exception as errors:
           self.logger.error(errors, extra=self.extra_params)
          
       self.extra_params['tokeUser'] = self.tokeUser

    async def signup(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.logger.info(constants.START, extra=self.extra_params)
        
        self.update = update
        self.context = context
        
        await self.setIdChat()
        
        self.isLogin = False
        if(self.tokenAsiloBot != "" and self.usernameAsiloBot != ""):
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_ALREADY_LOGIN.replace("{username}", self.usernameAsiloBot), -1)
            return
        
        await self.setUserTelegram()
            
        await self.setUserTelegram()
        
        self.logger.info(update, extra=self.extra_params)
        

        self.chat_id = update.message.chat_id

        await self.setTokenUser()

        #await self.clearMsg(True, update)
        #await self.clearMsgText(True, update)
        await self.validateFieldTextUser()

        self.logger.info(constants.END, extra=self.extra_params)

    async def oficine(self) -> int:
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        if self.dat["sede"] != -1:
            await self.oficine_extrajera()
        else:
            try:
                dat = self.arraysCites.oficines

                await self.sendesplegableButton(
                    dat, 2, constants.SUCESS_OFICINE, 1, 8)

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if(error):
                await self.oficine()

        self.logger.info(constants.END, extra=self.extra_params)

    async def oficine_extrajera(self):
        self.logger.info(constants.START, extra=self.extra_params)

        if self.dat["tramite_oficina"] != -1:
            await self.tramite_cuerpo_policial()
        else:
            try:

                dat = self.arraysCites.tramite_oficine_extrajera

                await self.sendesplegableButton(
                    dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8)
            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.extra_params)
                await self.oficine_extrajera()
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.extra_params)
                await self.oficine_extrajera()
            except Exception as errors:
                self.logger.error(errors, extra=self.extra_params)
                await self.oficine_extrajera()

        self.logger.info(constants.END, extra=self.extra_params)

    
        
    async def validateFieldTextUser(self):
        self.logger.info(constants.START, extra=self.extra_params)
        error = False
        self.optionValidate = -1
        self.optionValidat_Text = ""

        try:
            if self.dat["provinciaGeneral"] == -1:
                dat = self.arraysCites.provinces
                await self.sendesplegableButton(
                    dat, 1, constants.SUCESS_PROVINCE, 3, 10)
                return

            if self.dat["sede"] == -1:
                dat = self.arraysCites.oficines
                await self.sendesplegableButton(
                    dat, 2, constants.SUCESS_OFICINE, 1, 8)
                return

            if self.dat["tramite_oficina"] == -1:
                dat = self.arraysCites.tramite_oficine_extrajera
                await self.sendesplegableButton(
                    dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8)
                return

            if self.dat["tramite_cuperto_policial"] == -1:
                dat = self.arraysCites.tramite_cuerpo_nacional_policial
                await self.sendesplegableButton(
                    dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8)
                return

            if self.dat["typeDoc"] == -1:
                dat = self.arraysCites.tipo_doc
                await self.sendesplegableButton(
                    dat, 5, constants.SUCESS_TIPO_DOC, 3, 1)
                return

            if self.dat["doc"] == "":
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_DOCUMENT_TEXT, 0)
                return

            if self.dat["name"] == "":
                self.optionValidate = 1
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_CONFIRM_NAME_TEXT, 1)

                return

            if self.dat["birth"] == -1:
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_CONFIRM_BIRTH_TEXT, 2)

                return

            if self.dat["country"] == -1:
                self.optionValidate = -1
                dat = self.arraysCites.countrys
                await self.sendesplegableButton(dat, 6, constants.SUCESS_COUNTRY, 3, 15)
                return

            if self.dat[constants.USERNAME] == "":
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_USERNAME_TEXT, 4)
                return

            if self.dat[constants.PASSWORD] == "":
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_PASSWORD_TEXT, 5)
                return
            
            await self.registerUser()
            
            if(self.tokenAsiloBot == ""):
                return

            if(self.usernameAsiloBot != ""):
                if self.dat["plans"] == -1:
                    self.optionValidate = -1
                    await self.plans()
                    return

                if((self.dat['plans'] != -1 and self.dat['plans'] > 0) and self.dat['TypePayment'] != -1):
                     dat = self.arraysCites.payment_method
                     await self.sendesplegableButton(dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10)
                     self.optionValidate = -1
                     return

                if((self.dat['plans'] > 0 and self.dat['TypePayment'] != -1) and self.dat['reference_payment'] == ''):
                    dat = self.arraysCites.confirm

                    await self.sendesplegableButton(
                         dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 3, 10, "")
                    return
        except TimedOut as timedOutError:
              error = True
              self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
              error = True
              self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
              error = True
              self.logger.error(errors, extra=self.extra_params)

        finally:
            self.logger.info(self.dat, extra=self.extra_params)

        if error:
            await self.clearMsg(True, self.update)
            await self.clearMsgText(True, self.update)
            await self.validateFieldTextUser()

        self.logger.info(constants.END, extra=self.extra_params)

    async def tramite_cuerpo_policial(self):
        self.logger.info(constants.START, extra=self.extra_params)
        if self.dat["tramite_cuperto_policial"] != -1:
            await self.tipo_doc()
        else:
            try:
                dat = self.arraysCites.tramite_cuerpo_nacional_policial

                await self.sendesplegableButton(
                    dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8)

            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
            except Exception as errors:
                self.logger.error(errors, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
        self.logger.info(constants.END, extra=self.extra_params)

    async def tipo_doc(self):
        self.logger.info(constants.START, extra=self.extra_params)
        await self.validateFieldTextUser()
        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_document(self):
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                dat, 7, constants.SUCESS_CONFIRM_DOCUMENT, 2, 1, self.optionValidat_Text)

        except TimedOut as timedOutError:
                  error = True
                  self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                  error = True
                  self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                  error = True
                  self.logger.error(errors, extra=self.extra_params)

        if error:
              self.confirm_document()

    async def confirm_name(self):
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1, self.optionValidat_Text)

        except TimedOut as timedOutError:
                  error = True
                  self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                  error = True
                  self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                  error = True
                  self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.confirm

              await self.sendesplegableButton(
                   dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1, self.optionValidat_Text)

    async def confirm_birth(self):
        error = False
        self.logger.error(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1, self.optionValidat_Text)

        except TimedOut as timedOutError:
                   error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                   error = True
                   self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.confirm

              await self.sendesplegableButton(
                   dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1, self.optionValidat_Text)

    async def country(self):
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.countrys

            await self.sendesplegableButton(
                dat, 6, constants.SUCESS_COUNTRY, 3, 15)

        except TimedOut as timedOutError:
                  error = True
                  self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                  error = True
                  self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                  error = True
                  self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.countrys

              await self.sendesplegableButton(
                   dat, 6, constants.SUCESS_COUNTRY, 3, 15)

    async def actions(self):
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.actions

            await self.sendesplegableButton(
                dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15)

        except TimedOut as timedOutError:
                   error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                   error = True
                   self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.actions

              await self.sendesplegableButton(
                   dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15)

    async def plans(self):
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(
                dat, 11, constants.SUCESS_CONFIRM_PLANS, 2, 15)

        except TimedOut as timedOutError:
                   error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                   error = True
                   self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.plans

              await self.sendesplegableButton(
                   dat, 11, constants.SUCESS_CONFIRM_PLANS, 2, 15)

    async def confirm_payment_method(self):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.payment_method

            await self.sendesplegableButton(
                dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10)

        except TimedOut as timedOutError:
                   error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
                   error = True
                   self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.payment_method

              await self.sendesplegableButton(
                   dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10)

    async def confirm_payment(self, update):
        self.logger.info(constants.START, extra=self.extra_params)
        error = False
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5)

        except TimedOut as timedOutError:
              error = True
              self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
              error = True
              self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
              error = True
              self.logger.error(errors, extra=self.extra_params)

        if error:
              dat = self.arraysCites.confirm

              await self.newSelect.select(0, 0)

              await self.sendesplegableButton(
                   dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5)

        self.logger.info(constants.END, extra=self.extra_params)

    async def readyUser(self):
       self.logger.info(constants.START, extra=self.extra_params)

       await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_MESSAGE_VERIFIED_TEXT.replace("{}", self.usernameAsiloBot, -1))

       self.logger.info(constants.END, extra=self.extra_params)

    async def paymentReference(self):
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        if self.dat["payment"]:
            await self.readyUser()

        if self.dat["reference_payment"]:
            await self.readyUser()

        else:
            try:
               await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 3)

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as errors:
                self.logger.error(errors, extra=self.extra_params)
                error = True

            if(error):
               await self.paymentReference()

        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_reference_payment(self):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                dat, 13, constants.SUCESS_REFERENCE_PAYMENT, 2, 1, self.optionValidat_Text)

        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.extra_params)
            await self.confirm_reference_payment()
        except Exception as errors:
            self.logger.error(errors, extra=self.extra_params)
            await self.confirm_reference_payment()

        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_username(self):
        self.logger.info(constants.START, extra=self.extra_params)
        error = False
        code = constants.SUCESS_USER_REGISTER_USERNAME
        
        if(self.isLogin):
            self.isLogin = True
            code = constants.SUCESS_USER_LOGIN_USERNAME
            
        try:
            dat = self.arraysCites.confirm
            await self.sendesplegableButton(
                dat, 14, code, 2, 1, self.optionValidat_Text)

        except TimedOut as timedOutError:
              error = True
              self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
              error = True
              self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
              error = True
              self.logger.error(errors, extra=self.extra_params)

        if error:
            self.optionValidat_Text = ""
            self.optionValidate = 4

            if self.chaIds != -1:
                await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_USERNAME_TEXT, 5)

        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_password(self):
        self.logger.info(constants.START, extra=self.extra_params)
        error = False
        
        code = constants.SUCESS_USER_REGISTER_PASSWORD
        
        if(self.isLogin):
            self.isLogin = True
            code = constants.SUCESS_USER_LOGIN_PASSWORD
            
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                dat, 15, code, 2, 1, self.optionValidat_Text)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
            error = True
            self.logger.error(errors, extra=self.extra_params)

        if error:
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.ENTER_PASSWORD_TEXT, 5)

        self.logger.info(constants.END, extra=self.extra_params)

    async def validateReference(self, chat_id):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            await self.sendMessageTelChatId(self.chat_id, self.update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT, -1)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
            error = True
            self.logger.error(errors, extra=self.extra_params)

        if error:
            await self.validateReference()

        self.logger.info(constants.END, extra=self.extra_params)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        
        error = False

        await self.setTokenUser()
        
        await self.setUserTelegram()
        
        self.logger.info(constants.START, extra=self.extra_params)

        user = ""

        try:
            user = update.message.from_user
            self.user = user
            self.usernameTelegram = self.user.username
        except Exception as errors:
            self.logger.error(errors, extra=self.extra_params)

        try:
            self.update = update
            self.context = context
            """Sends a message with three inline buttons attached."""

            await update.message.reply_text(
                "✋🏼 Hola {user['first_name']}, Saludos y bienvenido al bot de automatización web para la gestión de sistema de administración pública."
            )

            await update.message.reply_text(
                "NOTA: Este bot 🤖 no tiene nada que ver con el gobierno de España 🇪🇸  ni tampoco con algún ente publico, solo es un sistema realizado para la ayuda de todos, en las que su función nos trae Solicitar, verificar y Anular nuestra cita de asilo en el país de España de manera automática cada cierto tiempo."
            )

            await update.message.reply_text(
                "Ha comenzado el proceso de registro, se le pediran los datos necesarios que solicita la pagina https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus, Luego de que ingrese el dato solicitado si todo es correcto se le pedira el siguiente hasta culmitar el proceso."
            )

            await update.message.reply_text(
                "Comandos: /signup para comenzar el proceso de registro o continuar en un proceso no terminado."
            )
        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.extra_params)
        except Exception as errors:
            error = True
            self.logger.error(errors, extra=self.extra_params)

        if(error):
            await self.start(update, context)

        self.logger.info(constants.END, extra=self.extra_params)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        error = False
        self.logger.info(constants.START, extra=self.extra_params)
        if self.tokeUser == "":
            self.tokeUser = str(random.randint(9999, 99999999999999)) + ":g"

        try:
            """Displays info on how to use the bot."""
            await update.message.reply_text("Use /start to test this bot.")

        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=self.extra_params)
            await self.help_command()
        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.extra_params)
            await self.help_command()
        except Exception as errors:
            self.logger.error(errors, extra=self.extra_params)
            await self.help_command()

        if(error):
            await self.help_command(update, context)

        self.logger.info(constants.END, extra=self.extra_params)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.logger.info(constants.START, extra=self.extra_params)

        query = update.callback_query

        self.logger.info("data in query:%s", query.data,
                         extra=self.extra_params)

        json_object = {}
        try:
            json_object = json.loads(query.data)
        except Exception as errors:
            self.logger.warning(errors, extra=self.extra_params)
            await self.clearMsg(True, update)
            await self.clearMsgText(True, update)
            index, _actions = query.data.split("-")
            _index = int(index)
            _actions = int(_actions)
            json_object = {"action": _actions, "page": 0,
                           "text": "", "page": 0, "index": _index}

        self.logger.info(json_object, extra=self.extra_params)

        # actions
        # 0:first
        # 1:after
        # 2:paginatorP
        # 3:paginationSelect

        text = json_object["text"]
        action = json_object["action"]
        newPage = json_object["page"]

        self.text_Loading = "🔤🔤🔤🔤🔤🔤🔤🔤"

        # print(f"query.data:{query.data}")\

        if json_object["action"] == constants.SUCESS_PROVINCE:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.provinces[json_object["index"]]
                _index = json_object["index"]
                self.dat["provinciaGeneral"] = _index

                # await self.oficine()
                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_OFICINE:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.oficines[json_object["index"]]
                _index = json_object["index"]
                self.dat["sede"] = _index

                #await self.oficine()
                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()
        elif json_object["action"] == constants.SUCESS_OFICINE_EXTRANJERA:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.tramite_oficine_extrajera[json_object["index"]]
                _index = json_object["index"]
                self.dat["tramite_oficina"] = _index
                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_TRAMITE_CUERPO_POLICIAL:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.tramite_cuerpo_nacional_policial[json_object["index"]]
                _index = json_object["index"]
                self.dat["tramite_cuperto_policial"] = _index

                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_TIPO_DOC:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.tipo_doc[json_object["index"]]
                _index = json_object["index"]
                self.dat["typeDoc"] = _index

                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_DOCUMENT:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                       self.dat["doc"] = self.optionValidat_Text
                       await self.validateFieldTextUser()

                else:
                       await self.validateFieldTextUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_NAME:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                       self.dat["name"] = self.optionValidat_Text
                       self.optionValidat_Text = ""
                       await self.validateFieldTextUser()
                else:
                       await self.validateFieldTextUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_NAME:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                       await self.clearMsgText(True, update)
                       self.dat["name"] = self.optionValidat_Text
                       await self.validateFieldTextUser()

                else:
                       await self.validateFieldTextUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_BIRTH:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]

                if _text == constants.YES:
                       await self.clearMsgText(True, update)
                       self.dat["birth"] = self.optionValidat_Text
                       await self.validateFieldTextUser()
                else:
                       await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_COUNTRY:
            error = False
            try:
                await self.clearMsg(True, update)
                _index = json_object["index"]
                _text = self.arraysCites.countrys[json_object["index"]]
                self.dat["country"] = _index
                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_USER_REGISTER_USERNAME:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _index = json_object["index"]
                _text = self.arraysCites.confirm[_index]
                if _text == constants.YES:
                    await self.clearMsgText(True, update)
                    self.dat[constants.USERNAME] = self.optionValidat_Text
                    await self.validateFieldTextUser()
                    return
                else:
                    await self.validateFieldTextUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_USER_REGISTER_PASSWORD:
            error = False
            try:
                await self.clearMsg(True, update)
                _index = json_object["index"]
                _text = self.arraysCites.confirm[_index]
                if _text == constants.YES:
                    await self.clearMsgText(True, update)
                    self.dat[constants.PASSWORD] = self.optionValidat_Text
                    await self.validateFieldTextUser()

                else:
                       await self.validateFieldTextUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_PLANS:
            error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.plans[json_object["index"]]
                _index = json_object["index"]

                self.dat["plans"] = _index
                await self.validateFieldTextUser()
                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
               await self.clearMsg(True, update)
               await self.clearMsgText(True, update)
               await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT_METHOD:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.payment_method[json_object["index"]]
                _index = json_object["index"]

                if _text != "":
                    self.dat["TypePayment"] = _index
                    await self.validateFieldTextUser()
                    return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
               await self.clearMsg(True, update)
               await self.clearMsgText(True, update)
               await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.payment_method[json_object["index"]]
                _index = json_object["index"]

                _value = False

                if(_index == 0):
                   _value = True

                if(_index == 1):
                  _value = False

                if _text != "":
                    self.dat["payment"] = _value
                    self.optionValidate = 3

                await self.validateFieldTextUser()

            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
               await self.clearMsg(True, update)
               await self.clearMsgText(True, update)
               await self.validateFieldTextUser()

        elif json_object["action"] == constants.SUCESS_REFERENCE_PAYMENT:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                       await self.clearMsgText(True, update)
                       self.dat["reference_payment"] = self.optionValidat_Text
                       await self.validateFieldTextUser()

                else:
                       await self.validateFieldTextUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateFieldTextUser()
                
                
        elif json_object["action"] == constants.SUCESS_USER_LOGIN_USERNAME or json_object["action"] == constants.SUCESS_USER_LOGIN_PASSWORD:
            error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                       await self.clearMsgText(True, update)
                       
                       
                       if(json_object["action"] == constants.SUCESS_USER_LOGIN_USERNAME):
                           self.dat[constants.USERNAME] = self.optionValidat_Text
                           
                       if(json_object["action"] == constants.SUCESS_USER_LOGIN_PASSWORD):
                           self.dat[constants.PASSWORD] = self.optionValidat_Text
                       await self.validateLoginUser()
                else:
                       await self.validateLoginUser()

                return
            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.validateLoginUser()

        else:
            self.logger.error("Actiones sin seleccion.",
                              extra=self.extra_params)
            await query.answer()

            if text == "first":
                await self.clearMsg(True, update)
                self.newSelect.page += 1
                await self.newSelect.select(0, action, self.newSelect.page)

            if text == "after":
                await self.clearMsg(True, update)
                self.newSelect.page -= 1
                await self.newSelect.select(0, action, self.newSelect.page)

            if text == "paginatorP" and action == 2:
                await self.clearMsg(True, update)
                self.page = json_object["page"]
                action = 2
                self.newSelect._paginatorActive = True
                await self.newSelect.select(0, action, self.newSelect.page)
            else:
                if text == "pageselect" and action == 3:
                    await self.clearMsg(True, update)
                    # await self.clearMsg(True,update)
                    action = 3
                    # print(f"JSON PAGE:{json_object['page']}")
                    self.page = json_object["page"]
                    self.newSelect._paginatorActive = True
                    await self.newSelect.select(0, action, newPage)

        # print(f"query.message====={query.message}")
        # print(f"query.message.chat.message_id:{query.message.message_id}")
        # print(f"query.message:{query.message}")

        self.logger.info(constants.END, extra=self.extra_params)

    async def clearMsgText(self, clearChatHistoryButtos, update):
        self.logger.info(constants.START, extra=self.extra_params)
        error = False
        
        if len(self.chatMsgUser) > 0:
            count = 0
            try:
                for x in self.chatMsgUser:
                    message_id = x[1]
                    chat_id = x[0]
                    #self.logger.info("Eliminando MsgChat:%s",
                                    # message_id, extra=self.extra_params)
                    await self.bot.delete_message(chat_id=chat_id, message_id=message_id)
                    del self.chatMsgUser[count]
                    
            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                if(str(networkError).find('not found')):
                    self.logger.warning(networkError, extra=self.extra_params)
                    del self.chatMsgUser[count]
                else:
                     error = True
                     self.logger.error(networkError, extra=self.extra_params)

            except Exception as errors:
                error = True
                self.logger.error(errors, extra=self.extra_params)

            if(error):
               time.sleep(1)
               await self.clearMsgText(clearChatHistoryButtos, update)
                
        self.logger.info(constants.END, extra=self.extra_params)

    async def clearMsg(self, clearChatHistoryButtos, update):
        self.logger.info(constants.START, extra=self.extra_params)
        #self.logger.info(update, extra=self.extra_params)
        error = False

        try:
               message_id = update.callback_query.message.message_id
               chat_id = update.callback_query.message.chat.id
               await self.bot.delete_message(chat_id=chat_id, message_id=message_id)
               self.logger.info("Eliminando buttons:%s",
                                message_id, extra=self.extra_params)
        except TimedOut as timedOutError:
               error = True
               self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
              if(networkError == 'not found'):
                    error = True
                    self.logger.warning(networkError, extra=self.extra_params)
              else:
                    self.logger.error(networkError, extra=self.extra_params)

        except Exception as errors:
               if(str(error).find("NoneType")):
                   self.logger.warning(errors, extra=self.extra_params)
               else:
                   self.logger.error(errors, extra=self.extra_params)
                   error = True

        if(error):
            time.sleep(3)
            await self.clearMsg(clearChatHistoryButtos, update)

        self.logger.info(constants.END, extra=self.extra_params)

    async def handle_text(self, update, context):
        self.logger.info(constants.START, extra=self.extra_params)
        text = update.message.text
        chat_id = update.message.chat_id
        messageId = update.message.message_id


        if text.find(".") !=-1:
            text = text.replace(".", "\.")
            
            
            

        self.logger.info(text, extra=self.extra_params)

        self.chatUserSend = chat_id
        self.chatUserMsgId = messageId

        self.chatMsgUser.append([chat_id, messageId])

        self.chaIds = chat_id

        self.optionValidat_Text = text

        if self.optionValidate == 0:
            await self.confirm_document()
        elif self.optionValidate == 1:
            await self.confirm_name()
        elif self.optionValidate == 2:
            await self.confirm_birth()
        elif self.optionValidate == 3:
            await self.confirm_reference_payment()
        elif self.optionValidate == 4:
            await self.confirm_username()
        elif self.optionValidate == 5:
            await self.confirm_password()
        else:
            await self.clearMsg(True, update)
            await self.clearMsgText(True, update)

            await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_USER_TEXT)

        self.logger.info(constants.END, extra=self.extra_params)

    def main(self) -> None:
        error = False
        try:
            
            persistence = PicklePersistence(filepath="conversationbot")

            self.logger.info(constants.START, extra=self.extra_params)

            #self.application = Application.builder().token(self.token).build()
            self.application = Application.builder().token(self.token).persistence(persistence).build()

            

            self.application.add_handler(CommandHandler("start", self.start))
            self.application.add_handler(
                CommandHandler("registerUser", self.registerUser))
            
            self.application.add_handler(CommandHandler("signup", self.signup))
            
            self.application.add_handler(CommandHandler("login", self.LoginUser))
            
            self.application.add_handler(CommandHandler("close", self.LogoutUser))

            self.application.add_handler(CallbackQueryHandler(self.button))
            
            self.application.add_handler(
                MessageHandler(filters.TEXT, self.handle_text))

            self.application.run_polling()

            self.logger.info(constants.END, extra=self.extra_params)
        except Exception:
            self.logger.warning(constants.ERROR_RUN_MAIN_FAILE, extra=self.extra_params)
            error = True

        if(error):
            self.logger.warning(constants.ERROR_RUN_MAIN_FAILE, extra=self.extra_params)
            nest_asyncio.apply()
            citaAsilobot().main()

        citaAsilobot().logger.info(constants.END, extra=citaAsilobot().extra_params)


if __name__ == "__main__":
    citaAsilobot().logger.info(constants.START, extra=citaAsilobot().extra_params)
    nest_asyncio.apply()
    citaAsilobot().main()
    citaAsilobot().logger.info(constants.END, extra=citaAsilobot().extra_params)



