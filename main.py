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
    
    dat1 = {
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
        "payment": True,
        "TypePayment": -1,
        "reference_payment": "",
        "sucess": False,
        "username": "",
        "password": ""
    }

    dat = {
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
        "payment": True,
        "TypePayment": 0,
        "reference_payment": "231231231231231231",
        "sucess": False,
        "username": "dvegas1",
        "password": ""
    }
    chaIds = -1
    optionValidate = -1
    optionValidat_Text = "SD"
    usernameTelegram = ""
    usernameAsiloBot = ""
    chatSend = ""
    chatMsgUser = []
    url = "http://localhost:3004/server"
    tokeUser = ""
    loginUser = {"username": "", "password": ""}
    extra_params = {"tokeUser": "S/T"}
    chat_id = ''

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
        "%(asctime)s %(levelname)s %(tokeUser)s %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # logging.basicConfig(format="%(asctime)s %(tokeUser)s %(name)s %(funcName)s %(filename)s:%(lineno)d %(levelname)s %(message)s",level=logging.INFO)
    # log = logging.getLogger("asiloBot")

    logger.info("Inicio asiloBot.", extra=extra_params)

    # logger.info("response LoginUser:%s","ddddddddddddddd", extra=extra_params)

    async def LogoutUser(self, chat_id, update):
        self.logger.info(constants.START, extra=self.extra_params)
        self.token = ""
        self.chatSend = await self.bot.send_message(
            chat_id=chat_id, text=constants.SUCESS_USER_LOGOUT_SUCESS
        )
        self.chatMsgUser.append(
            [self.chatSend.chat.id, self.chatSend.message_id])

        self.optionValidate = -1

        self.logger.info(constants.END, extra=self.extra_params)

    async def LoginUser(self, chat_id, update):
        self.logger.info(constants.START, extra=self.extra_params)
        payload = "username=dvegaslopez&password=12345"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.request(
            "POST", self.url + "/users_asilobot/loginAsiloBot", headers=headers, data=payload
        )
        _response = json.loads(response.text)

        self.optionValidate = -1

        self.logger.info(constants.END, extra=self.extra_params)

    async def registerUser_validate(self, chat_id, update, _json):
        self.logger.info(constants.START, extra=self.extra_params)

        _error = False

        try:
            _json["errors"]
        except Exception as error:
            self.logger.error(error, extra=self.extra_params)

            return _error

        try:
            _json["errors"]["msg"]
        except Exception as error:
            self.logger.error(error, extra=self.extra_params)
            return _error

            _error_msg = _json["errors"]["msg"]
            _error = True
            await self.clearMsg(True, update)
            await self.clearMsgText(True, update)

            if _error_msg == "USERNAME_ALREADY_EXISTS":
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.WARNING_USER_EMAIL_ALREADY_EXISTS
                )

                self.chatSend.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_USERNAME_TEXT
                )

                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

                self.chatSend.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

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
       except Exception as error:
           self.logger.error(error, extra=self.extra_params)
           sucess = False

    async def sendesplegableButton(self, _dat=[], case=-1, sucess_code=-1, _paginatorLisColumm=0, _paginatorGeneral=10, _add_title_text="", actions=0, page=-1):
       sucess = False
       try:
           self.newSelect = testListDesplegable.testList(
                self.token,
                self.update,
                self.context,
                _dat,
                case,
                sucess_code,
                _paginatorLisColumm,
                _paginatorGeneral,
                _add_title_text,
                logger=self.logger,
                extra_params=self.extra_params
            )

           await self.newSelect.select(actions, page)

           sucess = True

       except TimedOut as timedOutError:
           self.logger.error(timedOutError, extra=self.extra_params)
           sucess = False
       except NetworkError as networkError:
           self.logger.error(networkError, extra=self.extra_params)
           sucess = False
       except Exception as error:
           if(error == "'str' object has no attribute 'message'"):
              self.logger.warning(error, extra=self.extra_params)
           else:
              sucess = False
              self.logger.error(error, extra=self.extra_params)


       if(not sucess):
         time.sleep(3)

         self.newSelect = testListDesplegable.testList(
             self.token,
             self.update,
             self.context,
             _dat,
             case,
             sucess_code,
             _paginatorGeneral,
             _paginatorLisColumm,
             _add_title_text,
             logger=self.logger,
             extra_params=self.extra_params
             )
         await self.newSelect.select(actions, page)

    async def registerUser(self) -> int:
       self.logger.info(constants.START, extra=self.extra_params)
        #= update
       #self.context = context
       
       
       update = self.update
       
       self.logger.info(update, extra=self.extra_params)

       update_jsonStr = json.dumps(self.update.to_dict())
       update_json = json.loads(update_jsonStr)

       #$.message.chat.id
       self.logger.info(update_json, extra=self.extra_params)
       self.logger.info(update_json['message']
                        ['chat']['id'], extra=self.extra_params)

       #message_id = update.callback_query.message.message_id

       if(self.chat_id == ''):
          self.chat_id = update_json['message']['chat']['id']

       _sucess_form = True

       _payload = ""

       if(self.dat['username'] != ''):
           _payload += "username=" + self.dat['username'] + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Nombre de usuario"), 4)
          await self.sendMessageTelChatId(self.chat_id, update, constants.SUCESS_USERNAME_TEXT, 4)
          _sucess_form = False
          return

       if(self.dat['provinciaGeneral'] != -1 and _sucess_form):
           _payload += "provinciaGeneral=" + \
               str(self.dat['provinciaGeneral']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Provincia"), 4)
          _sucess_form = False
          _dat = self.arraysCites.provinces
          await self.sendesplegableButton(
              _dat, 1, constants.SUCESS_PROVINCE, 3, 10)

          return

       if(self.dat['sede'] != -1 and _sucess_form):
           _payload += "sede=" + str(self.dat['sede']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Sede"), 4)
          _sucess_form = False
          _dat = self.arraysCites.oficines
          await self.sendesplegableButton(
              _dat, 2, constants.SUCESS_OFICINE, 1, 8)
          return

       if(self.dat['tramite_oficina'] != -1 and _sucess_form):
           _payload += "tramite_oficina=" + \
               str(self.dat['tramite_oficina']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Oficina extranjera"), 4)
          _sucess_form = False
          _dat = self.arraysCites.tramite_oficine_extrajera
          await self.sendesplegableButton(
              _dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8)
          return

       if(self.dat['tramite_cuperto_policial'] != -1 and _sucess_form):
           _payload += "tramite_cuperto_policial=" + \
               str(self.dat['tramite_cuperto_policial']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Tramite Cuerpo Policial"), 4)
          _sucess_form = False
          _dat = self.arraysCites.tramite_cuerpo_nacional_policial
          await self.sendesplegableButton(
              _dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8)
          return

       if(self.dat['typeDoc'] != -1 and _sucess_form):
           _payload += "typeDoc=" + str(self.dat['typeDoc']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Tipo de documento"), -1)
          _sucess_form = False
          _dat = self.arraysCites.tipo_doc
          await self.sendesplegableButton(
              _dat, 5, constants.SUCESS_TIPO_DOC, 3, 1)
          return

       if(self.dat['doc'] != '' and _sucess_form):
           _payload += "doc=" + self.dat['doc'] + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Documento de Identidad"), 0)
          await self.sendMessageTelChatId(self.chat_id, update, constants.SUCESS_CONFIRM_DOCUMENT_TEXT, 0)
          _sucess_form = False
          return

       if(self.dat['name'] != '' and _sucess_form):
           _payload += "name=" + self.dat['name'] + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Nombre y Apellido"), -1)
          await self.sendMessageTelChatId(self.chat_id, update, constants.SUCESS_CONFIRM_NAME_TEXT, 1)
          _sucess_form = False
          return

       if(self.dat['birth'] != -1 and _sucess_form):
           _payload += "birth=" + str(self.dat['birth']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Año de Nacimiento"), -1)
          await self.sendMessageTelChatId(self.chat_id, update, constants.SUCESS_CONFIRM_BIRTH_TEXT, 2)
          _sucess_form = False
          return

       if(self.dat['country'] != -1 and _sucess_form):
           _payload += "country=" + str(self.dat['country']) + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "País de nacionalidad"), -1)
          _sucess_form = False
          _dat = self.arraysCites.countrys
          await self.sendesplegableButton(
              _dat, 6, constants.SUCESS_COUNTRY, 3, 15)
          return

       # if(self.dat['plans'] != -1 and _sucess_form):
       #     _payload += "plans=" + str(self.dat['plans']) + "&"
       # else:
       #    await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Plan"), -1)
       #    _sucess_form = False
       #    _dat = self.arraysCites.plans
       #    await self.sendesplegableButton(
       #        _dat, 11, constants.SUCESS_CONFIRM_PLANS, 2, 15, "")
       #    return

       # if(self.dat['plans'] != -1 and (_sucess_form and self.dat['plans'] > 0) and self.dat['TypePayment'] != -1):
       #     _payload += "TypePayment=" + str(self.dat['TypePayment']) + "&"
       # else:
       #    if(self.dat['plans'] != -1 and self.dat['plans'] > 0):
       #       await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Método de pago"), -1)
       #       _sucess_form = False
       #       _dat = self.arraysCites.payment_method

       #       await self.sendesplegableButton(
       #           _dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10, "")
       #       return

       # if(self.dat['plans'] > 0 and (_sucess_form and self.dat['TypePayment'] != -1) and self.dat['reference_payment'] != ''):
       #    if(self.dat['sucess']):
       #       _payload += "sucess=" + str(self.dat['sucess']) + "&"
       #    else:
       #       _sucess_form = False
       #       _dat = self.arraysCites.confirm

       #       await self.sendesplegableButton(
       #           _dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 3, 10, "")
       #       return

       if(self.dat['password'] != '' and _sucess_form):
           _payload += "password=" + self.dat['password'] + "&"
       else:
          await self.sendMessageTelChatId(self.chat_id, update, constants.WARNING_FIELD_EMPTY_OR_INVALID.replace("{}", "Contraseña"), -1)
          await self.sendMessageTelChatId(self.chat_id, update, constants.SUCESS_PASSWORD_TEXT, 5)
          _sucess_form = False
          return

       if(_sucess_form):
          payload = _payload
          caracter_remove = payload[-1:len(payload)]
          if(caracter_remove == '&'):
             payload = payload[:-1]

          # payload = "username=dvegaslopez&provinciaGeneral=0&sede=0&tramite_oficina=0&tramite_cuperto_policial=0&typeDoc=0&doc=19452357&name=Darwin%20Vegas&birth=1990&country=0&plans=1&payment=false&TypePayment=0&reference_payment=&phone=%2B584242727712&password=12345&role=user"

          self.logger.info(payload,extra=self.extra_params)

          headers = {"Content-Type": "application/x-www-form-urlencoded",
                     "Accept-Language": "en"}

          response = requests.request(
              "POST", self.url + "/users_asilobot/registerAsiloBot", headers=headers, data=payload
          )

          await self.clearMsg(True, update)
          await self.clearMsgText(True, update)

          self.chatSend = await self.bot.send_message(
              chat_id=self.chat_id, text=constants.SUCESS_USER_REGISTER_SUCESS
          )
          self.chatMsgUser.append(
              [self.chatSend.chat.id, self.chatSend.message_id])

          _response = json.loads(response.text)

          self.logger.info(_response, extra=self.extra_params)

          self.optionValidate = -1

          self.logger.info(constants.END, extra=self.extra_params)

          #await self.registerUser_validate(self.chat_id, update, _response)
       else:
          self.registerUser(self, self.chat_id, update)

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

       self.extra_params['tokeUser'] = self.tokeUser

    async def signup(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.logger.info(constants.START, extra=self.extra_params)
        self.update = update
        self.context = context
        
        self.logger.info(update,extra=self.extra_params)
        
        self.chat_id = update.message.chat_id

        await self.setTokenUser()

        if self.dat["provinciaGeneral"] != -1:
            await self.oficine()
        else:
            _dat = self.arraysCites.provinces
            
            await self.sendesplegableButton(
                _dat, 1, constants.SUCESS_PROVINCE, 3, 10)


        self.logger.info(constants.END, extra=self.extra_params)

    async def oficine(self) -> int:
        self.logger.info(constants.START, extra=self.extra_params)
        if self.dat["sede"] != -1:
            await self.oficine_extrajera()
        else:
            try:
                _dat = self.arraysCites.oficines

                regex = r"[^\w-]+"
                texto_limpio = [re.sub(r"/[^a-zA-Z0-9_ -]+/g", "", s)
                                for s in _dat]

                # self.newSelect = testListDesplegable.testList(
                #     self.token,
                #     self.update,
                #     self.context,
                #     texto_limpio,
                #     2,
                #     constants.SUCESS_OFICINE,
                #     1,
                #     8,
                #     logger=self.logger, extra_params=self.extra_params
                # )
                # await self.newSelect.select(0, 0)

                await self.sendesplegableButton(
                    _dat, 2, constants.SUCESS_OFICINE, 1, 8)

            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.extra_params)
                await self.oficine()
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.extra_params)
                await self.oficine()
            except Exception as error:
                self.logger.error(error, extra=self.extra_params)
                await self.oficine()
        self.logger.info(constants.END, extra=self.extra_params)

    async def oficine_extrajera(self):
        self.logger.info(constants.START, extra=self.extra_params)
        
        if self.dat["tramite_oficina"] != -1:
            await self.tramite_cuerpo_policial()
        else:
            try:

                _dat = self.arraysCites.tramite_oficine_extrajera
                # self.newSelect = testListDesplegable.testList(
                #     self.token,
                #     self.update,
                #     self.context,
                #     _dat,
                #     3,
                #     constants.SUCESS_OFICINE_EXTRANJERA,
                #     1,
                #     8,
                #     logger=self.logger, extra_params=self.extra_params
                # )

                # await self.newSelect.select(0, 0)

                await self.sendesplegableButton(
                    _dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8)



            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.extra_params)
                await self.oficine_extrajera()
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.extra_params)
                await self.oficine_extrajera()
            except Exception as error:
                self.logger.error(error, extra=self.extra_params)
                await self.oficine_extrajera()

        self.logger.info(constants.END, extra=self.extra_params)

    async def tramite_cuerpo_policial(self):
        self.logger.info(constants.START, extra=self.extra_params)
        if self.dat["tramite_cuperto_policial"] != -1:
            await self.tipo_doc()
        else:
            try:
                _dat = self.arraysCites.tramite_cuerpo_nacional_policial
                # self.newSelect = testListDesplegable.testList(
                #     self.token,
                #     self.update,
                #     self.context,
                #     _dat,
                #     4,
                #     constants.SUCESS_TRAMITE_CUERPO_POLICIAL,
                #     1,
                #     8,
                #     logger=self.logger, extra_params=self.extra_params
                # )

                # await self.newSelect.select(0, 0)

                await self.sendesplegableButton(
                    _dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8)

            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
            except Exception as error:
                self.logger.error(error, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
        self.logger.info(constants.END, extra=self.extra_params)

    async def tipo_doc(self):
        _error = False
        self.logger.info(constants.START, extra=self.extra_params)
        
        if self.dat["typeDoc"] != -1:
            # await self.oficine_extrajera()
            self.optionValidate = 0
            try:
                self.chatSend = await self.bot.send_message(
                    chat_id=self.chat_id, text=constants.SUCESS_CONFIRM_DOCUMENT_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])
            except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            if _error:
                await self.tipo_doc()
                
        else:
            try:
                _dat = self.arraysCites.tipo_doc
    
                await self.sendesplegableButton(
                    _dat, 5, constants.SUCESS_TIPO_DOC, 3, 1)
                
                self.logger.info(constants.END, extra=self.extra_params)
    
            except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
            if _error:
                  _dat = self.arraysCites.tipo_doc
            
                  await self.sendesplegableButton(
                      _dat, 5, constants.SUCESS_TIPO_DOC, 3, 1)
            
        self.logger.info(constants.END, extra=self.extra_params)
        
        
    async def confirm_document(self):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.confirm
            # self.newSelect = testListDesplegable.testList(
            #     self.token,
            #     self.update,
            #     self.context,
            #     _dat,
            #     7,
            #     constants.SUCESS_CONFIRM_DOCUMENT,
            #     2,
            #     1,
            #     self.optionValidat_Text,
            #     logger=self.logger, extra_params=self.extra_params
            # )

            # await self.newSelect.select(0, 0)

            await self.sendesplegableButton(
                _dat, 7, constants.SUCESS_CONFIRM_DOCUMENT, 2, 1,self.optionValidat_Text)
            
        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.tipo_doc
            
               await self.sendesplegableButton(
                   _dat, 7, constants.SUCESS_CONFIRM_DOCUMENT, 2, 1,self.optionValidat_Text)

    async def confirm_name(self):
        _error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                _dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1,self.optionValidat_Text)

        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.confirm
            
               await self.sendesplegableButton(
                   _dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1,self.optionValidat_Text)

    async def confirm_birth(self):
        _error = False
        self.logger.error(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                _dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1,self.optionValidat_Text)

        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.confirm
            
               await self.sendesplegableButton(
                   _dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1,self.optionValidat_Text)
               

    async def country(self):
        _error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.countrys

            await self.sendesplegableButton(
                _dat, 6, constants.SUCESS_COUNTRY, 3, 15)

        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.countrys
            
               await self.sendesplegableButton(
                   _dat, 6, constants.SUCESS_COUNTRY, 3, 15)
               

    async def actions(self):
        _error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.actions

            await self.sendesplegableButton(
                _dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15)

        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.actions
            
               await self.sendesplegableButton(
                   _dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15)

    async def plans(self):
        _error = False
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.plans

            await self.sendesplegableButton(
                _dat, 11, constants.SUCESS_CONFIRM_PLANS, 2, 15)

        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.plans
            
               await self.sendesplegableButton(
                   _dat, 11, constants.SUCESS_CONFIRM_PLANS, 2, 15)

    async def confirm_payment_method(self):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.payment_method

            await self.sendesplegableButton(
                _dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10)

        except TimedOut as timedOutError:
                   _error = True
                   self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
                   _error = True
                   self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
                   _error = True
                   self.logger.error(error, extra=self.extra_params)
            
        if _error:
               _dat = self.arraysCites.payment_method
            
               await self.sendesplegableButton(
                   _dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10)

    async def confirm_payment(self, update):
        self.logger.info(constants.START, extra=self.extra_params)
        _error = False
        try:
            _dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                _dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5)

        except TimedOut as timedOutError:
               _error = True
               self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
               _error = True
               self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
               _error = True
               self.logger.error(error, extra=self.extra_params)

        if _error:
               _dat = self.arraysCites.confirm

               await self.newSelect.select(0, 0)

               await self.sendesplegableButton(
                   _dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5)

        self.logger.info(constants.END, extra=self.extra_params)

    async def readyUser(self):
       self.logger.info(constants.START, extra=self.extra_params)

       await self.sendMessageTelChatId(self.chat_id, self.update, constants.WARNING_MESSAGE_VERIFIED.replace("{}", self.usernameAsiloBot, -1))

       self.logger.info(constants.END, extra=self.extra_params)

    async def paymentReference(self):
        _error = False
        self.logger.info(constants.START, extra=self.extra_params)
        if self.dat["payment"]:
            await self.readyUser()
            
        if self.dat["reference_payment"]:
            await self.readyUser()

        else:
            try:
               self.optionValidate = 3
               self.logger.info(self.dat, extra=self.extra_params)

               self.chatSend = await self.bot.send_message(
                   chat_id=self.chat_id, text=constants.SUCESS_REFERENCE_PAYMENT_TEXT
                   )
               self.chatMsgUser.append(
                   [self.chatSend.chat.id, self.chatSend.message_id])

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True

            if(_error):
               await self.paymentReference()

        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_reference_payment(self):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            _dat = self.arraysCites.confirm
            
            await self.sendesplegableButton(
                _dat, 13, constants.SUCESS_REFERENCE_PAYMENT, 2, 1,self.optionValidat_Text)

        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.extra_params)
            await self.confirm_reference_payment()
        except Exception as error:
            self.logger.error(error, extra=self.extra_params)
            await self.confirm_reference_payment()

        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_username(self):
        self.logger.info(constants.START, extra=self.extra_params)
        _error = False
        try:
            _dat = self.arraysCites.confirm

            await self.sendesplegableButton(
                _dat, 14, constants.SUCESS_USER_REGISTER_USERNAME, 2, 1,self.optionValidat_Text)

        except TimedOut as timedOutError:
               _error = True
               self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
               _error = True
               self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
               _error = True
               self.logger.error(error, extra=self.extra_params)

        if _error:
            self.optionValidat_Text = ""
            self.optionValidate = 4
            self.logger.info(self.dat, extra=self.extra_params)
            if self.chaIds != -1:
                self.optionValidate = 5
                self.chatSend = await self.bot.send_message(
                    chat_id=self.chaIds, text=constants.SUCESS_USERNAME_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

        self.logger.info(constants.END, extra=self.extra_params)

    async def confirm_password(self):
        self.logger.info(constants.START, extra=self.extra_params)
        _error = False
        try:
            _dat = self.arraysCites.confirm
            
            await self.sendesplegableButton(
                _dat, 15, constants.SUCESS_USER_REGISTER_PASSWORD, 2, 1,self.optionValidat_Text)

        except TimedOut as timedOutError:
            _error = True
            self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
            _error = True
            self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
            _error = True
            self.logger.error(error, extra=self.extra_params)

        if _error:
            self.optionValidat_Text = ""
            self.optionValidate = 5
            self.logger.info(self.dat, extra=self.extra_params)
            if self.chaIds != -1:
                self.optionValidate = 5
                self.chatSend = await self.bot.send_message(
                    chat_id=self.chaIds, text=constants.SUCESS_PASSWORD_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

        self.logger.info(constants.END, extra=self.extra_params)

    async def validateReference(self, chat_id):
        self.logger.info(constants.START, extra=self.extra_params)
        try:
            self.chatSend = await self.bot.send_message(
                chat_id=chat_id, text=constants.SUCESS_REFERENCE_PAYMENT_WAITING
            ) 

        except TimedOut as timedOutError:
            _error = True
            self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
            _error = True
            self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
            _error = True
            self.logger.error(error, extra=self.extra_params)
            
        if _error:
            await self.validateReference()
            
        self.logger.info(constants.END, extra=self.extra_params)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.logger.info(constants.START, extra=self.extra_params)
        _error=False
        
        await self.setTokenUser()

        user = ""

        try:
            user = update.message.from_user
            self.user = user
            self.usernameTelegram = self.user.username
        except Exception as error:
            self.logger.error(error, extra=self.extra_params)

        try:
            self.update = update
            self.context = context
            """Sends a message with three inline buttons attached."""

            await update.message.reply_text(
                f"✋🏼 Hola {user['first_name']}, Saludos y bienvenido al bot de automatización web para la gestión de sistema de administración pública."
            )

            await update.message.reply_text(
                f"NOTA: Este bot 🤖 no tiene nada que ver con el gobierno de España 🇪🇸  ni tampoco con algún ente publico, solo es un sistema realizado para la ayuda de todos, en las que su función nos trae Solicitar, verificar y Anular nuestra cita de asilo en el país de España de manera automática cada cierto tiempo."
            )

            await update.message.reply_text(
                f"Ha comenzado el proceso de registro, se le pediran los datos necesarios que solicita la pagina https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus, Luego de que ingrese el dato solicitado si todo es correcto se le pedira el siguiente hasta culmitar el proceso."
            )

            await update.message.reply_text(
                f"Comandos: /signup para comenzar el proceso de registro o continuar en un proceso no terminado."
            )
        except TimedOut as timedOutError:
            _error = True
            self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
            _error = True
            self.logger.error(networkError, extra=self.extra_params)
        except Exception as error:
            _error = True
            self.logger.error(error, extra=self.extra_params)
            
            
        if(_error):
            await self.start(update,context)
            
        self.logger.info(constants.END, extra=self.extra_params)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        _error = False
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
        except Exception as error:
            self.logger.error(error, extra=self.extra_params)
            await self.help_command()
            
        if(_error):
            await self.help_command(update,context)
            
        self.logger.info(constants.END, extra=self.extra_params)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.logger.info(constants.START, extra=self.extra_params)

        query = update.callback_query

        self.logger.info("data in query:%s", query.data,
                         extra=self.extra_params)

        json_object = {}
        try:
            json_object = json.loads(query.data)
        except Exception as error:
            self.logger.warning(error, extra=self.extra_params)
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

        chat_id = query.message.chat.id
        # ID del mensaje que se desea editar
        message_id = query.message.message_id

        self.text_Loading = "🔤🔤🔤🔤🔤🔤🔤🔤"

        # print(f"query.data:{query.data}")\

        if json_object["action"] == constants.SUCESS_PROVINCE:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.provinces[json_object["index"]]
                _index = json_object["index"]
                self.dat["provinciaGeneral"] = _index
                self.logger.info(self.dat, extra=self.extra_params)
                await self.oficine()
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
                await self.signup(self.update, self.context)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.signup(self.update, self.context)

        elif json_object["action"] == constants.SUCESS_OFICINE:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.oficines[json_object["index"]]
                _index = json_object["index"]
                self.dat["sede"] = _index
                self.logger.info(self.dat, extra=self.extra_params)
                await self.oficine()
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.oficine()
        elif json_object["action"] == constants.SUCESS_OFICINE_EXTRANJERA:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.tramite_oficine_extrajera[json_object["index"]]
                _index = json_object["index"]
                self.dat["tramite_oficina"] = _index
                self.logger.info(self.dat, extra=self.extra_params)
                await self.tramite_cuerpo_policial()
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.oficine_extrajera()

        elif json_object["action"] == constants.SUCESS_TRAMITE_CUERPO_POLICIAL:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.tramite_cuerpo_nacional_policial[json_object["index"]]
                _index = json_object["index"]
                self.dat["tramite_cuperto_policial"] = _index
                self.logger.info(self.dat, extra=self.extra_params)
                
                await self.tipo_doc()
                
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)

            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.tramite_cuerpo_policial()

        elif json_object["action"] == constants.SUCESS_TIPO_DOC:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.tipo_doc[json_object["index"]]
                _index = json_object["index"]
                self.dat["typeDoc"] = _index
                self.logger.info(self.dat, extra=self.extra_params)
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_CONFIRM_DOCUMENT_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])
                self.optionValidate = 0
                self.logger.info(self.dat, extra=self.extra_params)
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.tipo_doc()

        elif json_object["action"] == constants.SUCESS_CONFIRM_DOCUMENT:
            _error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == "Si":
                        self.dat["doc"] = self.optionValidat_Text
                        self.optionValidat_Text = "SD"
                        self.optionValidate = 1
                        self.logger.info(self.dat, extra=self.extra_params)
                        self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_NAME_TEXT
                        )
                        self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])

                        self.logger.info(self.dat, extra=self.extra_params)
                else:
                        self.optionValidate = 0
                        self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_DOCUMENT_TEXT
                        )
                        self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_CONFIRM_DOCUMENT_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])
                self.optionValidate = 0

        elif json_object["action"] == constants.SUCESS_CONFIRM_NAME:
            _error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == "Si":
                        self.dat["name"] = self.optionValidat_Text
                        self.optionValidat_Text = "SD"
                        self.optionValidate = 2
                        self.logger.info(self.dat, extra=self.extra_params)
                        self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_BIRTH_TEXT
                        )
                        self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])
                else:
                       self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_NAME_TEXT
                        )
                       self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])

                       self.optionValidate = 1

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_CONFIRM_NAME_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])
                self.optionValidate = 1

        elif json_object["action"] == constants.SUCESS_CONFIRM_NAME:
            _error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == "Si":
                        await self.clearMsgText(True, update)
                        self.dat["name"] = self.optionValidat_Text
                        self.optionValidat_Text = "SD"
                        self.optionValidate = 2
                        self.logger.info(self.dat, extra=self.extra_params)
                        self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_BIRTH_TEXT
                        )
                        self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])
                else:
                       self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_NAME_TEXT
                        )
                       self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])

                       self.optionValidate = 1

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_CONFIRM_NAME_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

                self.optionValidate = 1

        elif json_object["action"] == constants.SUCESS_CONFIRM_BIRTH:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]

                if _text == "Si":
                        await self.clearMsgText(True, update)
                        self.dat["birth"] = self.optionValidat_Text
                        self.optionValidat_Text = "SD"
                        self.optionValidate = 3
                        self.logger.info(self.dat, extra=self.extra_params)
                        await self.country()
                else:
                       await self.clearMsg(True, update)
                       await self.clearMsgText(True, update)
                       self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_CONFIRM_BIRTH_TEXT
                        )
                       self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])
                       self.optionValidate == 2

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_CONFIRM_BIRTH_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])
                self.optionValidate == 2

        elif json_object["action"] == constants.SUCESS_COUNTRY:
            _error = False
            try:
                await self.clearMsg(True, update)
                _index = json_object["index"]
                _text = self.arraysCites.countrys[json_object["index"]]
                self.dat["country"] = _index
                self.optionValidate = 4
                self.optionValidat_Text = constants.SUCESS_USERNAME_CONFIRM
                self.logger.info(self.dat, extra=self.extra_params)
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_USERNAME_TEXT)

                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.country()

        elif json_object["action"] == constants.SUCESS_USER_REGISTER_USERNAME:
            _error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _index = json_object["index"]
                _text = self.arraysCites.confirm[_index]
                if _text == "Si":
                    await self.clearMsgText(True, update)
                    self.dat["username"] = self.optionValidat_Text
                    self.optionValidat_Text = ""
                    self.optionValidate = 5
                    self.logger.info(self.dat, extra=self.extra_params)
                    self.chatSend = await self.bot.send_message(
                        chat_id=chat_id, text=constants.SUCESS_PASSWORD_TEXT
                    )
                    self.chatMsgUser.append(
                        [self.chatSend.chat.id, self.chatSend.message_id])
                else:
                    self.chatSend = await self.bot.send_message(
                        chat_id=chat_id, text=constants.SUCESS_USERNAME_TEXT
                    )
                    self.chatMsgUser.append(
                        [self.chatSend.chat.id, self.chatSend.message_id])

                    self.optionValidate = 4

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)

                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_USERNAME_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

        elif json_object["action"] == constants.SUCESS_USER_REGISTER_PASSWORD:
            _error = False
            try:
                await self.clearMsg(True, update)
                _index = json_object["index"]
                _text = self.arraysCites.confirm[_index]
                if _text == "Si":
                    await self.clearMsgText(True, update)
                    self.dat["password"] = self.optionValidat_Text
                    self.optionValidat_Text = ""
                    self.optionValidate = -1
                    self.logger.info(self.dat, extra=self.extra_params)
                    self.chatSend = await self.bot.send_message(
                        chat_id=chat_id, text=constants.SUCESS_USER_REGISTER_PROCESS
                    )
                    self.chatMsgUser.append(
                        [self.chatSend.chat.id, self.chatSend.message_id])

                    await self.registerUser(chat_id, update)

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                self.optionValidate = 5
                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_PASSWORD_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

        elif json_object["action"] == constants.SUCESS_CONFIRM_PLANS:
            _error = False
            try:
                await self.clearMsg(True, update)
                _text = self.arraysCites.plans[json_object["index"]]
                _index = json_object["index"]

                if _text != "":
                    self.dat["plans"] = _index
                    self.optionValidat_Text = "SD"
                    self.optionValidate = -1
                    self.logger.info(self.dat, extra=self.extra_params)

                await self.confirm_payment_method()
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                await self.plans()

        elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT_METHOD:
            _error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.payment_method[json_object["index"]]
                _index = json_object["index"]

                if _text != "":
                    self.dat["TypePayment"] = _index
                    self.optionValidate = -1
                    self.logger.info(self.dat, extra=self.extra_params)

                # self.chatSend = await self.bot.send_message(
                #     chat_id=chat_id, text=constants.SUCESS_REFERENCE_PAYMENT_TEXT
                # )
                # self.chatMsgUser.append(
                #     [self.chatSend.chat.id, self.chatSend.message_id])
                await self.confirm_payment(update)

                self.logger.info(self.dat, extra=self.extra_params)
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.confirm_payment(update)
                self.optionValidate = -1

        elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT:
            _error = False
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
                    self.logger.info(self.dat, extra=self.extra_params)

                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_REFERENCE_PAYMENT_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])
                self.logger.info(self.dat, extra=self.extra_params)
            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.confirm_payment(update)

        elif json_object["action"] == constants.SUCESS_REFERENCE_PAYMENT:
            _error = False
            try:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == "Si":
                        await self.clearMsgText(True, update)
                        self.dat["reference_payment"] = self.optionValidat_Text
                        self.optionValidat_Text = "SD"
                        self.optionValidate = -1
                        self.logger.info(self.dat, extra=self.extra_params)
                        await self.validateReference(chat_id)
                else:
                        self.chatSend = await self.bot.send_message(
                            chat_id=chat_id, text=constants.SUCESS_REFERENCE_PAYMENT_TEXT
                        )
                        self.chatMsgUser.append(
                            [self.chatSend.chat.id, self.chatSend.message_id])
                        self.optionValidate = 3

            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                _error = True
                self.logger.error(networkError, extra=self.extra_params)
            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            if _error:
                await self.clearMsg(True, update)
                await self.clearMsgText(True, update)
                self.optionValidate = 3

                self.chatSend = await self.bot.send_message(
                    chat_id=chat_id, text=constants.SUCESS_REFERENCE_PAYMENT_TEXT
                )
                self.chatMsgUser.append(
                    [self.chatSend.chat.id, self.chatSend.message_id])

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
        _error = False
        if len(self.chatMsgUser) > 0:
            try:
                for x in self.chatMsgUser:
                    message_id = x[1]
                    chat_id = x[0]
                    self.logger.info("Eliminando MsgChat:%s",
                                     message_id, extra=self.extra_params)
                    await self.bot.delete_message(chat_id=chat_id, message_id=message_id)
            except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
            except NetworkError as networkError:
                if(networkError == 'Message to delete not found'):
                    self.logger.warning(networkError, extra=self.extra_params)
                else:
                    _error = True
                    self.logger.error(networkError, extra=self.extra_params)

            except Exception as error:
                _error = True
                self.logger.error(error, extra=self.extra_params)

            while(_error):
               time.sleep(1)
               await self.clearMsgText(clearChatHistoryButtos, update)

            self.chatMsgUser = []
        self.logger.info(constants.END, extra=self.extra_params)

    async def clearMsg(self, clearChatHistoryButtos, update):
        self.logger.info(constants.START, extra=self.extra_params)
        self.logger.info(update, extra=self.extra_params)
        _error = False

        try:
               message_id = update.callback_query.message.message_id
               chat_id = update.callback_query.message.chat.id
               await self.bot.delete_message(chat_id=chat_id, message_id=message_id)
               self.logger.info("Eliminando buttons:%s",
                                message_id, extra=self.extra_params)
        except TimedOut as timedOutError:
                _error = True
                self.logger.error(timedOutError, extra=self.extra_params)
        except NetworkError as networkError:
               if(networkError == 'Message to delete not found'):
                    _error = True
                    self.logger.warning(networkError, extra=self.extra_params)
               else:
                    self.logger.error(networkError, extra=self.extra_params)

        except Exception as error:
                if(error =="NoneType' object has no attribute 'message'"):
                   self.logger.error(error, extra=self.extra_params)
                else:
                   _error = True

        if(_error):
            time.sleep(3)
            await self.clearMsg(clearChatHistoryButtos, update)
        
        self.logger.info(constants.END, extra=self.extra_params)

    async def handle_text(self, update, context):
        self.logger.info(constants.START, extra=self.extra_params)
        text = update.message.text
        chat_id = update.message.chat_id
        messageId = update.message.message_id
        
        
        if text.find(".")!=-1:
            text = text.replace(".","\.")
  
        self.logger.info(text,extra=self.extra_params)

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

            self.chatSend = await self.bot.send_message(
                chat_id=chat_id, text=constants.WARNING_USER
            )
            self.chatMsgUser.append(
                [self.chatSend.chat.id, self.chatSend.message_id])

        self.optionValidate = -1
      
        self.logger.info(constants.END, extra=self.extra_params)

    def main(self) -> None:
        _error=False
        try:
            
            self.logger.info(constants.START,extra=self.extra_params)
    
            self.application = Application.builder().token(self.token).build()
    
            self.application.add_handler(CommandHandler("start", self.start))
            self.application.add_handler(CommandHandler("registerUser", self.registerUser))
            self.application.add_handler(CommandHandler("signup", self.signup))
    
            self.application.add_handler(CallbackQueryHandler(self.button))
            self.application.add_handler(
                MessageHandler(filters.TEXT, self.handle_text))
    
            self.application.run_polling()
            
            self.logger.info(constants.END,extra=self.extra_params)
        except Exception:
            self.logger.warning(constants.ERROR_RUN_MAIN_FAILE,extra=self.extra_params)
            _error=True
        
        
        if(_error):
            self.logger.warning(constants.ERROR_RUN_MAIN_FAILE,extra=self.extra_params)
            nest_asyncio.apply()
            citaAsilobot().main()
            
        citaAsilobot().logger.info(constants.END,extra=citaAsilobot().extra_params)
            


if __name__ == "__main__":
    citaAsilobot().logger.info(constants.START,extra=citaAsilobot().extra_params)
    nest_asyncio.apply()
    citaAsilobot().main()
    citaAsilobot().logger.info(constants.END,extra=citaAsilobot().extra_params)
    
        
   