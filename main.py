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
import traceback
from telegram.constants import ParseMode
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    helpers,
    KeyboardButton
)
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    PicklePersistence,
    filters,
    ConversationHandler,
    MessageHandler
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
import inspect
import threading
import asyncio

CHOOSING, TYPING_REPLY, TYPING_CHOICE, BIO, SIGNUP, DOCUMENT, SIGNUP, TOKEN = range(
    8)


class citaAsilobot:

    def __init__(self):
        # self.data = threading.local()
        # setattr(self.data, 'menuDat', [])
        a = 1

    _text_intentns = ["Primera", "Segunda", "Tercera y ultima"]
    application = ""
    token = "5940401924:AAHUZEP6BtTOWPk2Zvy5uQOatI8b8JySVu8"
    update = ""
    context = ""
    bot = telegram.Bot(token=token)
    bot.setWebhook(
    url = None,
    certificate = None,
    max_connections = 100,
    allowed_updates = None,
    ip_address = None,
    drop_pending_updates = False,
    secret_token = token
    )
    arraysCites = datArray_cites.array_cites()
    newSelect = ""
    text_Loading = "🔤🔤🔤🔤🔤🔤🔤🔤"
    data = threading.local()

    datDefault = {
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
        "typePayment": -1,
        "reference_payment": "",
        "sucess": False,
        constants.USERNAME: "",
        constants.PASSWORD: "",
        constants.DATA_CHAT_ID: "-1",
    }

    chaIds = -1
    optionValidate = -1
    optionValidat_Text = ""
    usernameTelegram = "-"
    usernameAsiloBot = "-"
    chatSend = ""
    chatMsgUser = []
    chatMsgMenu = []

    url = "http://localhost:3004/server"

    extra_params = {"chat_id": "-1",
                    "usernameAsiloBot": "-", "usernameTelegram": "-"}
    responseSingup = ''
    isLogin = False
    blockUser = False
    isErrorFormulary = False
    data.hidden_menu = False
    data = {}

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
        "%(asctime)s %(levelname)s %(chat_id)s [%(usernameAsiloBot)s:%(usernameTelegram)s] %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    print("                 ")
    print("                 ")
    print("                 ")
    print(" Inicio asiloBot ")
    print("                 ")
    print("                 ")
    print("                 ")

    async def LogoutUser(self, update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=-1) -> int:
        update = update

        if(chat_id == -1):
            chat_id = update.message.chat_id
            self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        self.logger.info(self.data.get(chat_id), extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        
        self.logger.info(self.data, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        
        if(self.data.get(chat_id).get(constants.TOKEN_ASILO, "") == ""):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_NOT_LOGIN_TEXT, -1)
        else:
            self.isLogin = False
            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,
                          self.datDefault).update({constants.USERNAME: ""})
            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,
                          self.datDefault).update({constants.PASSWORD: ""})
            self.data.get(chat_id).update({constants.TOKEN_ASILO: ""})
            self.dat = self.datDefault
            self.data.get(chat_id).update({constants.CHAT_DATA_PERFIL:self.datDefault})
            self.data.get(chat_id).update({constants.EXTRA_PARAMS:self.extra_params})

            await self.setUserTelegram(update, chat_id)

            await self.sendMessageTelChatId(chat_id, update, constants.SUCESS_USER_LOGOUT_SUCESS_TEXT)

            self.data.get(chat_id).update({constants.HIDDEN_MENU: True})
            await self.persistentBtns(update, True, chat_id)
            self.logger.info(constants.END, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def loginAsiloBot(self, update, chat_id):

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        _error = False

        if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.USERNAME, '') != "" and self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.PASSWORD, '') != ""):
            payload = "username=" + \
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.USERNAME, '')+"&password=" + \
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,
                              self.datDefault).get(constants.PASSWORD, '')
            headers = {"Content-Type": "application/x-www-form-urlencoded"}

            try:
                response = requests.request(
                    "POST", self.url + "/login", headers=headers, data=payload
                )
                _response = json.loads(response.text)

                self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", response.text), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            except Exception as error:
                self.logger.error(str(error) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))
                _error = True

            if(not _error):
                self.data.get(chat_id).update(
                    {constants.ACTIONS_USER: constants.ACTION_USER_BOT_LOGIN})
                await self.registerUser_validate(update, _response, chat_id)

        else:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGOUT_SUCESS_TEXT)
            self.isLogin = True
            await self.validateLoginUser(update, False, chat_id)

        self.logger.info("Error in login %s", _error,
                         extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        return _error

    
    async def updatePerfil(self, update, chat_id):

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        _error = False

        if(len(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, {})) > 10):

            headers = {"Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Bearer " + self.data.get(chat_id).get(constants.TOKEN_ASILO)}

            payload = self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL)

            self.logger.info("Request:" + str(payload), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            

            try:
                response = requests.request(
                    "PATCH", self.url + "/profile", headers=headers, data=payload
                )
                response_json = json.loads(response.text)

                if(len(response_json) > 0):
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_PERFIL_UPTADATE_SUCESS_TEXT, -1)
                    await self.listButtonsModifiedPerfil(update,chat_id)

                self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", response.text), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                return True
            except Exception as error:
                self.logger.error(str(error) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))
                _error = True

            if(_error):
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_PERFIL_UPDATE_TEXT_GENERAL_TEXT, -1)

        else:
            self.logger.error("No se encontro perfil o no cumple con los campos requeridos: Perfil:%s, Campos:%s",self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, {}) ,str(len(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, {}))),extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_PERFIL_UPDATE_TEXT_GENERAL_TEXT,-1)
            return False

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        return _error

    async def validateLoginUser(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        self.isLogin = True
        await self.persistentBtns(update, False, chat_id)

        try:
            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.USERNAME, '') == "" or self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.PASSWORD, '') == ""):
                if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.USERNAME, '') == "":
                    await self.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 6)
                    return False

                if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.PASSWORD, '') == "":
                    await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 7)
                    return False
            else:
                if(not error):
                    isErrorLogin = await self.loginAsiloBot(update, chat_id)
                    if(isErrorLogin):
                        await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT, -1)
                        self.data.get(chat_id).update(
                            {constants.HIDDEN_MENU: True})
                        await self.persistentBtns(update, True, chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True

            _finError = str(errors).find("Failed to establish")
            if(_finError != -1):
                self.logger.warning(errors, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            else:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

        if error:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_ERROR_GENERAL, -1)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def listButtonsModifiedPerfil(self, update, chat_id):
            self.logger.info(constants.START + ":" + inspect.stack()
                            [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            
            dataPerfil = await self.getPerfil(update,chat_id)

            self.logger.info(dataPerfil, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            
            error = False

            dat = []
            lists = []
            count = 0

            items = self.arraysCites.data_perfil.get("data")

            for item in items:
                nameLbl = item.get("lbl")
                text = item.get("text")
                for clave, valor in dataPerfil.items():
                    if(nameLbl == clave):
                        self.logger.info("%s,%s",clave,str(valor), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                        if(len(item.get("array",[])) > 0):
                            if(valor == -1 or (type(valor) == str and str(valor).strip() == "")):
                                dat.append(text + "--")
                            else:
                                dat.append(text + item.get("array",[])[valor])
                        else:
                            if(valor == -1 or (type(valor) == str and str(valor).strip() == "")):
                                dat.append(text + "--")
                            else:
                                dat.append(text + str(valor))
            
            if(len(dat) > 0):
                try:
                    msgOld = self.data.get(chat_id).get(constants.UPDATE_PERFIL_MESSAGE_ID,-1)
                    await self.bot.delete_message(chat_id=chat_id, message_id=msgOld)
                except Exception as errors:
                    self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                        constants.EXTRA_PARAMS, self.extra_params))
            
                msg =await self.sendesplegableButton(update,dat, 17, constants.SELECT_INPUT_MODIFY_PERFIL, 1, 20, chat_id=chat_id,delete=False)

                self.data.get(chat_id).update({constants.UPDATE_PERFIL_MESSAGE_ID: msg.message_id})

                msgFinish = await self.sendesplegableButton(update,self.arraysCites.finishUpdateProdifle, 19, constants.FINISH_UPDATE, 1, 20, chat_id=chat_id,delete=False)

            else:
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_GET_PERFIL_NOT_DATA_TEXT, -1)
 

    async def getDataText(self,data,chat_id):
        json = {}

        if(data.get(constants.PLANS) is not None and data.get(constants.PLANS) != -1):
            json.update({constants.PLANS:self.arraysCites.plans[data.get(constants.PLANS)]})

        if(data.get(constants.ACTION) is not None and data.get(constants.ACTION) != -1):
            json.update({constants.ACTION:self.arraysCites.actions[data.get(constants.ACTION)]})

        if(bool(data.get(constants.PAYMENT)) is not None and bool(data.get(constants.PAYMENT))):
            json.update({constants.PAYMENT:"Pago realizado con exito"})
        else:
            json.update({constants.PAYMENT:"En espera de su pago"})

        if(data.get(constants.TYPE_PAYMENT) is not None and data.get(constants.TYPE_PAYMENT) != -1):
            json.update({constants.TYPE_PAYMENT:self.arraysCites.payment_method[data.get(constants.TYPE_PAYMENT)]})

        if(data.get(constants.REFERENCE_PAYMENT) is not None and data.get(constants.REFERENCE_PAYMENT) != ""):
            json.update({constants.REFERENCE_PAYMENT:data.get(constants.REFERENCE_PAYMENT)})
        else:
            json.update({constants.REFERENCE_PAYMENT:"Sin referencia"})

        if(data.get(constants.USERNAME) is not None and data.get(constants.USERNAME) != ""):
            json.update({constants.USERNAME:data.get(constants.USERNAME)})

        if(data.get(constants.PROVINCIAGENERAL) is not None and data.get(constants.PROVINCIAGENERAL) != -1):
            json.update({constants.PROVINCIAGENERAL:self.arraysCites.provinces[data.get(constants.PROVINCIAGENERAL)]})

        if(data.get(constants.TRAMITE_CUERPO_POLICIAL) is not None and data.get(constants.TRAMITE_CUERPO_POLICIAL) != -1):
            json.update({constants.TRAMITE_CUERPO_POLICIAL:self.arraysCites.tramite_cuerpo_nacional_policial[data.get(constants.TRAMITE_CUERPO_POLICIAL)]})

        if(data.get(constants.TYPEDOC) is not None and data.get(constants.TYPEDOC) != -1):
            json.update({constants.TYPEDOC:self.arraysCites.tipo_doc[data.get(constants.TYPEDOC)]})

        if(data.get(constants.DOC) is not None and data.get(constants.DOC) != ""):
            json.update({constants.DOC:data.get(constants.DOC)})

        if(data.get(constants.NAME) is not None and data.get(constants.NAME) != ""):
            json.update({constants.NAME:data.get(constants.NAME)})

        if(data.get(constants.BIRTH) is not None and data.get(constants.BIRTH) != ""):
            json.update({constants.BIRTH:data.get(constants.BIRTH)})

        if(data.get(constants.COUNTRY) is not None and data.get(constants.COUNTRY) != ""):
            json.update({constants.COUNTRY:self.arraysCites.countrys[data.get(constants.COUNTRY)]})

        if(data.get(constants.SEDE) is not None and data.get(constants.SEDE) != ""):
            json.update({constants.SEDE:self.arraysCites.oficines[data.get(constants.SEDE)]})



        self.logger.info(json, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            
        return json


    async def getPerfil(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        
        _response = {}
        error = False
       # token = self.data.get(chat_id).get(constants.TOKEN_ASILO)
       # self.logger.info(token, self, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Authorization": "Bearer " + self.data.get(chat_id).get(constants.TOKEN_ASILO)}

        self.data.get(chat_id).update(
            {constants.ACTIONS_USER: constants.ACTION_USER_BOT_UPDATE_PERFIL})

        try:
            response = requests.request(
                "GET", self.url + "/profile", headers=headers
            )
            _response = json.loads(response.text)

            self.data.get(chat_id).update(
                {constants.CHAT_DATA_PERFIL: _response})

            self.logger.info(constants.RESPONSE_API_CORE.replace(
                "{msg}", response.text), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

            self.logger.info(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault),
                             extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

            # terminar metodo
            self.logger.info(constants.END, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))


        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))
        finally:
            if(error):
              await self.sendMessageTelChatId(chat_id, update, constants.WARNING_GET_PERFIL_FAIL_TEXT, -1)
           
            return _response

        
    async def setIdChat(self, update, chat_id):
        update_jsonStr = json.dumps(update.to_dict())
        update_json = json.loads(update_jsonStr)

        if(chat_id == ''):
            chat_id = update_json['message']['chat']['id']

    async def LoginUser(self, update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=-1) -> int:
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        update = update
        self.context = context

        if(chat_id == -1):
            chat_id = update.message.chat_id

        await self.setUserTelegram(update, chat_id)
        await self.setTokenUser(chat_id)
        await self.setIdChat(update, chat_id)

        if(self.blockUser):
            await self.sendMessageTelChatId(chat_id, update, constants.BLOCKED_USER_TEXT, -1)

        self.isLogin = True

        if(self.data.get(chat_id).get(constants.TOKEN_ASILO, "") != "" and self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params).get(constants.USERNAME_ASILO_BOT) != ""):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_ALREADY_LOGIN, -1)
            return

        if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.USERNAME, '') == "" or self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL, self.datDefault).get(constants.PASSWORD, '') == ""):
            await self.validateLoginUser(update, chat_id)
        else:
            isErrorLogin = await self.loginAsiloBot(update, chat_id)
            if(isErrorLogin):
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT, -1)
                self.data.get(chat_id).update({constants.HIDDEN_MENU: True})
                await self.persistentBtns(update, True, chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    def timBlockUser(self, _json):
        target_time = datetime.datetime.now(
        ) + datetime.timedelta(minutes=constants.BLOCKED_USER_MINUTES_BLOCK)
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

    async def registerUser_validate(self, update, _json, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        sucess = True
        try:
            self.logger.info(self.data.get(chat_id).get(constants.ACTIONS_USER), extra=self.data.get(
                            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            token = _json.get("token", "")

            if(token != ""):

                self.data.get(chat_id).update({constants.TOKEN_ASILO: token})

                self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params).update(
                    {constants.USERNAME_ASILO_BOT: _json.get("user").get(constants.USERNAME)})

                if(self.data.get(chat_id).get(constants.ACTIONS_USER) == constants.ACTION_USER_BOT_LOGIN):
                    
                    await self.sendMessageTelChatId(chat_id, update, constants.SUCESS_USER_LOGIN_TEXT, -1,False)
                    
                    self.data.get(chat_id).update(
                        {constants.HIDDEN_MENU: True})
                    await self.persistentBtns(update, True, chat_id)
                    await self.getPerfil(update, chat_id)
                    
                    

                if(self.data.get(chat_id).get(constants.ACTIONS_USER) == constants.ACTION_USER_BOT_SIGNUP):
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_REGISTER_SUCESS_TEXT, -1)
                    self.logger.info(
                        constants.USER_REGISTER_SUCESS_TEXT, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                    await self.persistentBtns(True, update, chat_id=chat_id)

                error_msg = _json.get("errors",{"msg":[]}).get("msg")
                

                if(len(error_msg) == 0):
                    valid = True
                else:
                        if(type(error_msg)=="list"):
                            for error in error_msg:
                                if(error.get("msg") == constants.MISSING):
                                    await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_INTENTS_TEXT, -1)
                                    valid = False
                                    
                        if error_msg == constants.WARNING_API_USERNAME_ALREADY_EXIST:
                            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.USERNAME: ""})
                            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_API_USERNAME_ALREADY_EXIST_TEXT, -1)
                            self.isErrorFormulary = True
                            await self.validateFieldTextUser(update, chat_id)

                        if error_msg == constants.WARNING_API_WRONG_PASSWORD or error_msg == constants.WARNING_API_USER_DOES_NOT_EXIST:
                            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.USERNAME: ""})
                            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.PASSWORD: ""})
                            
                            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_API_WRONG_PASSWORD_TEXT, -1)
                            self.data.get(chat_id).update(
                                {constants.HIDDEN_MENU: True})
                            valid = False
                            await self.persistentBtns(update, True, chat_id)

                        if error_msg == constants.BLOCKED_USER:
                            self.isErrorFormulary = True
                            self.timBlockUser()
                            self.blockUser = True
                            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.USERNAME: ""})
                            self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.PASSWORD: ""})
                            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_API_WRONG_PASSWORD_TEXT, -1)
                            await self.sendMessageTelChatId(chat_id, update, constants.BLOCKED_USER_TEXT, -1)
                            valid = False

                return valid
            
        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            sucess = False
        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            sucess = False
        except Exception as errors:
            sucess = False
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

            return False
        

    async def sendMessageTelChatId(self, chat_id, update, optionValidat_Text="", optionValidate=-1, add_clearList=True,parseMode="",delete=False):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        sucess = True
        error_str = ""
        msg = ""
        # await self.plansMenu(chat_id)

        try:
            self.optionValidate = optionValidate
            self.optionValidat_Text = optionValidat_Text
            if(parseMode == "html"):
                msg = await self.bot.sendMessage(
                    chat_id=chat_id, text=optionValidat_Text,parse_mode=ParseMode.HTML
                )
               
            else:
                msg = await self.bot.send_message(
                    chat_id=chat_id, text=optionValidat_Text
                )

            if(add_clearList):
                self.logger.info("✅ Agregando mensaje del chat: %s a pendiente por eliminar con message_id: %s y contiene el texto:%s",
                                 chat_id, msg.message_id, msg.text, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                
                msgsUser = self.data.get(chat_id).get(constants.CHAT_MSG_USER,[])
                msgsUser.append(
                    [chat_id, msg.message_id])

                self.data.get(chat_id).update({constants.CHAT_MSG_USER:msgsUser})
                
                

            self.chatSend = ""
        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            error_str = str(timedOutError)
            sucess = False
        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            error_str = str(networkError)
            sucess = False
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))
            error_str = str(errors)
            sucess = False

        self.logger.info("Message:%s,send sucess:%s",
                         optionValidat_Text, sucess, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        if(not sucess and error_str.find("not found") == -1):
            await self.sendMessageTelChatId(update, optionValidat_Text, optionValidate, add_clearList)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def sendesplegableButton(self, update, dat=[], case=-1, sucess_code=-1, _paginatorLisColumm=2, _paginatorGeneral=10, _add_title_text="", actions=0, page=-1, chat_id=None,delete=True):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        if(chat_id is None):
            self.logger.error("chat_id is None.", extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            return
        error = False

        self.newSelect = testListDesplegable.testList(
            self.token,
            update,
            self.context,
            dat,
            case,
            sucess_code,
            _paginatorLisColumm,
            _paginatorGeneral,
            _add_title_text,
            logger=self.logger,
            extra_params=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params),
            chat_id=chat_id
        )

        msgBtns = await self.newSelect.select(update, 0, actions, page)
       # self.logger.info(msgBtns,extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

        chatid = msgBtns.chat.id
        messageId = msgBtns.message_id

        if(chat_id is not None and messageId is not None and delete):
           # msgs.append({msgBtns,messageId})
            msgs = self.data.get(chat_id).get(constants.CHAT_MSG_USER, [])
            msgs.append([chatid, messageId])

            self.data.get(chat_id).update({constants.CHAT_MSG_USER: msgs})
            self.logger.info(self.data.get(chat_id).get(
                constants.CHAT_MSG_USER, []), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            
            
        if(error):
            time.sleep(3)
            await self.sendesplegableButton(update=update, dat=dat, case=case, sucess_code=sucess_code, _paginatorLisColumm=_paginatorLisColumm, _paginatorGeneral=_paginatorGeneral, _add_title_text=_add_title_text, chat_id=chat_id)

        
        self.logger.info(constants.END + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        return msgBtns

    async def registerUser(self, update, chat_id) -> int:
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                       "Accept-Language": "en"}
        _payload = ""
        try:
            # $.message.chat.id
            # self.logger.info(update_json, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

            # message_id = update.callback_query.message.message_id

            if(chat_id == '' or chat_id is None):
                update_jsonStr = json.dumps(update.callback_query.to_dict())
                update_json = json.loads(update_jsonStr)
                chat_id = update_json['message']['chat']['id']

            

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.USERNAME, "") != ''):
                _payload += "username=" + self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.USERNAME,'') + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.USERNAME), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PROVINCIAGENERAL, -1) != -1):
                _payload += "provinciaGeneral=" + \
                    str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PROVINCIAGENERAL,-1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.PROVINCIAGENERAL), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SEDE, -1) != -1):
                _payload += "sede=" + str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SEDE,-1)) + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.SEDE), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_OFICINA, -1) != -1):
                _payload += "tramite_oficina=" + \
                    str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_OFICINA,-1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.TRAMITE_OFICINA), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_CUERPO_POLICIAL, -1) != -1):
                _payload += "tramite_cuperto_policial=" + \
                    str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_CUERPO_POLICIAL,-1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.TRAMITE_CUERPO_POLICIAL), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TYPEDOC,-1) != -1):
                _payload += "typeDoc=" + str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TYPEDOC,-1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.TRAMITE_CUERPO_POLICIAL), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.DOC, '') != ''):                
                _payload += "doc=" + self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.DOC,'') + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.DOC), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.NAME, '') != ''):
                _payload += "name=" + self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.NAME,'') + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.NAME), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.BIRTH, '') != ''):
                _payload += "birth=" + str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.BIRTH,'')) + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.BIRTH), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.COUNTRY, -1) != -1):
                _payload += "country=" + str(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.COUNTRY,-1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.COUNTRY), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False

            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PASSWORD, '') != ''):
                _payload += "password=" + self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PASSWORD,'') + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.PASSWORD), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.validateFieldTextUser(update, chat_id)
                return False
            

            _payload += "role=" + "user" + "&" + "chat_id=" + str(chat_id) + "&"

            payload = _payload
            caracter_remove = payload[-1:len(payload)]
            if(caracter_remove == '&'):
                payload = payload[:-1]

            self.logger.info(payload, extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

            

            await self.sendMessageTelChatId(chat_id, update, constants.USER_REGISTER_PROCESS_TEXT, -1)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            
            self.logger.error(traceback.print_exc(), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        sucess_Singup = False
        timetOut = False

        try:
            errorRequest = False
            self.responseSingup = requests.request(
                "POST", self.url + "/register", headers=headers, data=payload)

            responseSingoToJson = json.loads(self.responseSingup.text)

            self.logger.info(responseSingoToJson, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            
            self.data.get(chat_id).update({constants.ACTIONS_USER:constants.ACTION_USER_BOT_SIGNUP})

            sucess_Singup = await self.registerUser_validate(update, responseSingoToJson, chat_id)

            if(sucess_Singup):
                return True

        except TimedOut as timedOutError:
            errorRequest = True
            timetOut = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            errorRequest = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            errorRequest = True
           # if(str(error).find("NoneType")):
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if(timetOut):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT, -1)
            self.data.get(chat_id).update({constants.HIDDEN_MENU: True})
            await self.persistentBtns(update, True, chat_id)
        else:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_INTENTS_TEXT.replace("{}", ""), -1)

            return

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def setLogger(self):
        self.formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(tokeUser)s %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
        )
        self.handler.setFormatter(self.formatter)

    async def setTokenUser(self, chat_id):

        if(self.data.get(chat_id) is None):
            self.data.update({chat_id: {constants.DATA_CHAT_ID: chat_id}})

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        tempToken = "S/T"
        token = self.data.get(chat_id).get(constants.TOKEN_ASILO, "")
        extra_param = self.data.get(chat_id).get(
            constants.EXTRA_PARAMS, self.extra_params)

        if token == "" or token == tempToken:
            token = str(random.randint(9999, 99999999999999)) + ":g"
            extra_param["tokeUser"] = token
            self.data.get(chat_id).update(
                {constants.EXTRA_PARAMS: extra_param})

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def setUserTelegram(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:
            user = update.message.from_user
            usernameTelegram = user.username
            self.data.get(chat_id).get(constants.EXTRA_PARAMS).update(
                {constants.USERNAME_TELEGRAM: usernameTelegram})

        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

    async def signup(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

        self.actions_user_bot = constants.ACTION_USER_BOT_SIGNUP

        

        self.context = context
        chat_id = -1

        if(update.message.chat_id is not None):
            chat_id = update.message.chat_id
            self.logger.info("Chat id usuario:%s", chat_id,
                             extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

            if(self.data.get(chat_id) is None):
                self.data.update({chat_id: {constants.DATA_CHAT_ID: chat_id}})

        if(chat_id == -1):
            self.logger.error(
                "No se encontro el id del chat, por favor validar.", extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                
            return
        
        self.data.get(chat_id).update({constants.ACTIONS_USER:constants.ACTION_USER_BOT_SIGNUP})

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        await self.setIdChat(update, chat_id)

        self.isLogin = False
        if(self.data.get(chat_id).get(constants.TOKEN_ASILO, "")):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_ALREADY_LOGIN.replace("{username}", self.usernameAsiloBot), -1)
            return

        await self.setUserTelegram(update, chat_id)

        chat_id = update.message.chat_id

        # self.logger.info(update, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

        await self.setTokenUser(chat_id)

        await self.validateFieldTextUser(update, chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def oficine(self, update, chat_id) -> int:
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SEDE,-1) != -1:
            await self.oficine_extrajera(update, chat_id)
        else:
            try:
                dat = self.arraysCites.oficines
                await self.sendesplegableButton(update,
                                                dat, 2, constants.SUCESS_OFICINE, 1, 8, chat_id=chat_id)

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            except NetworkError as networkError:
                error = True
                self.logger.error(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if(error):
                await self.oficine(update, chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def oficine_extrajera(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_OFICINA,-1) != -1:
            await self.tramite_cuerpo_policial(update, chat_id)
        else:
            try:

                dat = self.arraysCites.tramite_oficine_extrajera

                await self.sendesplegableButton(update,
                                                dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8, chat_id=chat_id)
            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                error = True
            except Exception as errors:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))
                error = True
            if(error):
                await self.oficine_extrajera(update, chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def validateFieldTextUser(self, update, chat_id=-1,fieldOptional=[]):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        if(chat_id == -1):
            self.logger.error("Error en parametro chat_id",
                              extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            return

        error = False
        self.optionValidate = -1
        self.optionValidat_Text = ""

        if(len(fieldOptional) > 0):
            if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(fieldOptional[0], -1) == -1:
                dat = fieldOptional[2]
                await self.sendesplegableButton(update,
                                                dat, fieldOptional[4], fieldOptional[1], 3, 10, chat_id=chat_id,delete=False)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PROVINCIAGENERAL, -1) == -1:
            dat = self.arraysCites.provinces
            await self.sendesplegableButton(update,
                                            dat, 1, constants.SUCESS_PROVINCE, 3, 10, chat_id=chat_id)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SEDE, -1) == -1:
            dat = self.arraysCites.oficines
            await self.sendesplegableButton(update,
                                            dat, 2, constants.SUCESS_OFICINE, 1, 8, chat_id=chat_id)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_OFICINA, -1) == -1:
            dat = self.arraysCites.tramite_oficine_extrajera
            await self.sendesplegableButton(update,
                                            dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8, chat_id=chat_id)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_CUERPO_POLICIAL, -1) == -1:
            dat = self.arraysCites.tramite_cuerpo_nacional_policial
            await self.sendesplegableButton(update,
                                            dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8, chat_id=chat_id)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TYPEDOC,-1) == -1:
            dat = self.arraysCites.tipo_doc
            await self.sendesplegableButton(update,
                                            dat, 5, constants.SUCESS_TIPO_DOC, 3, 1, chat_id=chat_id)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.DOC, '') == "":
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_DOCUMENT_TEXT, 0)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.NAME, '') == "":
            self.optionValidate = 1
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_NAME_TEXT, 1)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.BIRTH, '') == '':
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_BIRTH_TEXT, 2)
            return False

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.COUNTRY, -1) == -1:
            self.optionValidate = -1
            dat = self.arraysCites.countrys
            await self.sendesplegableButton(update, dat, 6, constants.SUCESS_COUNTRY, 3, 15, chat_id=chat_id)
            return False
        
        if(self.data.get(chat_id).get(constants.ACTIONS_USER,-1) != constants.ACTION_USER_BOT_UPDATE_PERFIL):
            if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.USERNAME,'') == "":
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 4)
                return False

            if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PASSWORD, '') == "":
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 5)
                return False

        if(self.data.get(chat_id).get(constants.ACTIONS_USER) == constants.ACTION_USER_BOT_SIGNUP):
            await self.registerUser(update, chat_id)

        if(self.data.get(chat_id).get(constants.ACTIONS_USER) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
            await self.updatePerfil(update, chat_id)

        if(self.data.get(chat_id).get(constants.TOKEN_ASILO, "") == ""):
            return False

        if error:
            await self.validateFieldTextUser(update, chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        return True

    async def tramite_cuerpo_policial(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.TRAMITE_CUERPO_POLICIAL,-1) != -1:
            await self.tipo_doc(update, chat_id)
        else:
            try:
                dat = self.arraysCites.tramite_cuerpo_nacional_policial

                await self.sendesplegableButton(update,
                                                dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8, chat_id=chat_id)

            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.tramite_cuerpo_policial(update, chat_id)
            except NetworkError as networkError:
                self.logger.error(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                await self.tramite_cuerpo_policial(update, chat_id)
            except Exception as errors:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))
                await self.tramite_cuerpo_policial(update, chat_id)
        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def tipo_doc(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        await self.validateFieldTextUser(update, chat_id)
        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def confirm_document(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:

            if(not await utilis.utils.validateDoc(self,self.optionValidat_Text)):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_DOC_FORMAT, -1,parseMode="html")
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.ENTER_DOCUMENT_TEXT, 0)
                return False
            
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,dat, 7, constants.SUCESS_CONFIRM_DOCUMENT, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            self.confirm_document(update, chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def confirm_name(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        
        if(not await utilis.utils.validateName(self,self.optionValidat_Text)):
           await self.sendMessageTelChatId(chat_id, update, constants.WARNING_NAME_FORMAT, -1,parseMode="html")
           await self.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_NAME_TEXT, 1)
           return False

        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1, self.optionValidat_Text, chat_id=chat_id)

    async def confirm_birth(self, update, chat_id):
        error = False
        self.logger.error(constants.START, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:

            if(not await utilis.utils.validate_Birt(self,self.optionValidat_Text)):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_BIRT_FORMAT, -1,parseMode="html")
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.ENTER_CONFIRM_BIRTH_TEXT, 2)
                return False
            
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1, self.optionValidat_Text, chat_id=chat_id)

    async def country(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:
            dat = self.arraysCites.countrys

            await self.sendesplegableButton(update,
                                            dat, 6, constants.SUCESS_COUNTRY, 3, 15, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            dat = self.arraysCites.countrys

            await self.sendesplegableButton(update,
                                            dat, 6, constants.SUCESS_COUNTRY, 3, 15, chat_id=chat_id)

    async def actions(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:
            dat = self.arraysCites.actions

            await self.sendesplegableButton(update,
                                            dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            dat = self.arraysCites.actions

            await self.sendesplegableButton(update,
                                            dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15, chat_id=chat_id)

    async def plans(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(update,
                                            dat, 11, constants.SUCESS_CONFIRM_PLANS, 1, 15, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(update,
                                            dat, 11, constants.SUCESS_CONFIRM_PLANS, 2, 15, chat_id=chat_id)

    async def plansMenu(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(update,
                                            dat, 11, constants.SUCESS_CONFIRM_MENU_PLANS, 1, 15, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            time.sleep(3)
            self.plansMenu(update, chat_id)

    async def payment_method(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        try:
            dat = self.arraysCites.payment_method

            await self.sendesplegableButton(update,
                                            dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            self.logger.warn(
                constants.WARNING_USER_PAYMENT_FAIL_TEXT, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_PAYMENT_FAIL_TEXT, -1)

    async def confirm_payment(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            dat = self.arraysCites.confirm

            await self.newSelect.select(update, 0, 0, 0)

            await self.sendesplegableButton(update,
                                            dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5, chat_id=chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def readyUser(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        await self.sendMessageTelChatId(chat_id, update, constants.WARNING_MESSAGE_VERIFIED_TEXT.replace("{}", self.usernameAsiloBot, -1))

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def paymentReference(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PAYMENT,False):
            await self.readyUser()

        if self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.REFERENCE_PAYMENT,False):
            await self.readyUser()

        else:
            try:
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 3)

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            except NetworkError as networkError:
                error = True
                self.logger.error(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            except Exception as errors:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))
                error = True

            if(error):
                await self.sendMessageTelChatId(chat_id, update, constants.USER_REFERENCE_PAYMENT_NOT_SAVE_TEXT)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def confirm_reference_payment(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        try:

            if(not await utilis.utils.validateReference(self,self.optionValidat_Text)):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_REFERENCE_FORMAT, -1,parseMode="html")
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 3)
                return False
    
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 13, constants.SUCESS_REFERENCE_PAYMENT, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            error = True

        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))
            error = True

        if(error):
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def confirm_reference_Menu_payment(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        dat = self.arraysCites.confirm

        await self.sendesplegableButton(update,
                                        dat, 13, constants.SUCESS_REFERENCE_PAYMENT, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def setReferenceMenu(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        await self.sendMessageTelChatId(chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 15)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def confirm_username(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        code = constants.SUCESS_USER_REGISTER_USERNAME

        if(not await utilis.utils.validate_username(self,self.optionValidat_Text)):
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USERNAME_FORMAT, -1,parseMode="html")
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 4)
                return False

        if(self.isLogin):
            self.isLogin = True
            code = constants.SUCESS_USER_LOGIN_USERNAME

        try:
            dat = self.arraysCites.confirm
            await self.sendesplegableButton(update,
                                            dat, 14, code, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))
            traceback.print_exc()
            
        if error:
            self.optionValidat_Text = ""
            self.optionValidate = 4

            if self.chaIds != -1:
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 5)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def confirm_password(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False

        if(not await utilis.utils.validate_password(self,self.optionValidat_Text)):
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_PASSWORD_FORMAT, -1,parseMode="html")
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 5)
                return False

        code = constants.SUCESS_USER_REGISTER_PASSWORD

        if(self.isLogin):
            self.isLogin = True
            code = constants.SUCESS_USER_LOGIN_PASSWORD

        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 15, code, 2, 1, self.optionValidat_Text, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 5)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def validateReference(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        try:
            await self.sendMessageTelChatId(chat_id, update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT, -1)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if error:
            await self.validateReference()

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def start(self, update: telegram.Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        error = False
        chat_id = -1
        messageId = -1

        # self.logger.info("Update:%s",json.dumps(update.to_dict()), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

        if(update.message.chat_id is not None):
            chat_id = update.message.chat_id
            chat_id = chat_id

            if(self.data.get(chat_id) is None):
                self.data.update({chat_id: {constants.DATA_CHAT_ID: chat_id}})
                self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params).update(
                    {constants.DATA_CHAT_ID: chat_id})

        await self.setTokenUser(chat_id)

        self.logger.info(self.data, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        self.logger.info("Chat id usuario:%s", chat_id,
                         extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        self.logger.info("data:%s", self.data,
                         extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        update = update
        self.context = context

        # if 'clave2' in mi_diccionario:
        # .get(
        #        constants.CHAT_MSG_USER, []).append([chat_id, messageId])

        await self.setUserTelegram(update, chat_id)

        self.data.get(chat_id).update({constants.HIDDEN_MENU: True})
        await self.persistentBtns(update, True, chat_id)

        chatMsgUser = self.data.get(chat_id).get(constants.TOKEN_ASILO,"")
        # self.data.get(chat_id).get(constants.CHAT_MSG_USER, [])

        self.logger.info(chatMsgUser, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        # return

        self.logger.info("*********************************************************************************************************************************************************************** CHAT ID " + str(
            chat_id) + " ***********************************************************************************************************************************************************************", extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        user = ""

        try:
            user = update.message.from_user
            self.user = user
            self.usernameTelegram = self.user.username
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        try:
            update = update
            self.context = context
            """Sends a message with three inline buttons attached."""

            await update.message.reply_text(
                f"✋🏼 Hola {user['first_name']}, Saludos y bienvenido al bot de automatización web para la gestión de sistema de administración pública."
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
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))

        if(error):
            await self.start(update, context)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        error = False
        chat_id=update.message.chat_id
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        
        try:
            """Displays info on how to use the bot."""
            await update.message.reply_text("Use /start to test this bot.")

        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            await self.help_command()
        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            await self.help_command()
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                constants.EXTRA_PARAMS, self.extra_params))
            await self.help_command()

        if(error):
            await self.help_command(update, context)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

        # updateReceiber = json.dumps(update.to_dict())
        # self.logger.info(updateReceiber, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

        query = update.callback_query

        chat_id = update.callback_query.message.chat.id

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        await asyncio.create_task(self.clearMsgText(True,update,chat_id=chat_id))

        await self.persistentBtns(update, False, chat_id)

        self.logger.info("data in query:%s", query.data,
                         extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        json_object = {}
        try:
            json_object = json.loads(query.data)
        except Exception as errors:
            self.logger.warning(errors, extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            index, _actions = query.data.split("-")
            _index = int(index)
            _actions = int(_actions)
            json_object = {"action": _actions, "page": 0,
                           "text": "", "page": 0, "index": _index}

        self.logger.info(json_object, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

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

        if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault) is None):
            self.data.get(chat_id).update(
                constants.CHAT_DATA_PERFIL, self.datDefault)

        if json_object["action"] == constants.SUCESS_PROVINCE:
            error = False
            try:

                _text = self.arraysCites.provinces[json_object["index"]]
                _index = json_object["index"]
                # self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PROVINCIAGENERAL,-1) = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.PROVINCIAGENERAL: _index})

                await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_OFICINE:
            error = False
            try:

                _text = self.arraysCites.oficines[json_object["index"]]
                _index = json_object["index"]
                # self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SEDE,-1) = _index

                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.SEDE: _index})

                # await self.oficine(update,chat_id)
                await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_OFICINE_EXTRANJERA:
            error = False
            try:

                _text = self.arraysCites.tramite_oficine_extrajera[json_object["index"]]
                _index = json_object["index"]
                # self.dat["tramite_oficina"] = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.TRAMITE_OFICINA: _index})
                await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_TRAMITE_CUERPO_POLICIAL:
            error = False
            try:

                _text = self.arraysCites.tramite_cuerpo_nacional_policial[json_object["index"]]
                _index = json_object["index"]
                # self.dat["tramite_cuperto_policial"] = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.TRAMITE_CUERPO_POLICIAL: _index})

                await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_TIPO_DOC:
            error = False
            try:
                _text = self.arraysCites.tipo_doc[json_object["index"]]
                _index = json_object["index"]
                # self.dat["typeDoc"] = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.TYPEDOC: _index})

                await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_CONFIRM_DOCUMENT:
            error = False
            try:
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                    # self.dat["doc"] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.DOC: self.optionValidat_Text})
                    await self.validateFieldTextUser(update, chat_id)
                else:
                    await self.validateFieldTextUser(update, chat_id)

                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_CONFIRM_NAME:
            error = False
            try:
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                    # self.dat["name"] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.NAME: self.optionValidat_Text})
                    self.optionValidat_Text = ""
                    await self.validateFieldTextUser(update, chat_id)
                else:
                    await self.validateFieldTextUser(update, chat_id)

                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_CONFIRM_BIRTH:
            error = False
            try:
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                    # self.dat["birth"] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.BIRTH: self.optionValidat_Text})
                    await self.validateFieldTextUser(update, chat_id)
                else:
                    await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_COUNTRY:
            error = False
            try:

                _index = json_object["index"]
                _text = self.arraysCites.countrys[json_object["index"]]
                # self.dat["country"] = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.COUNTRY: _index})
                await self.validateFieldTextUser(update, chat_id)
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_USER_REGISTER_USERNAME:
            error = False
            try:
                _index = json_object["index"]
                _text = self.arraysCites.confirm[_index]
                if _text == constants.YES:
                    # self.dat[constants.USERNAME] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.USERNAME:self.optionValidat_Text})
                    await self.validateFieldTextUser(update, chat_id)
                    return
                else:
                    await self.validateFieldTextUser(update, chat_id)

                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_USER_REGISTER_PASSWORD:
            error = False
            try:

                _index = json_object["index"]
                _text = self.arraysCites.confirm[_index]
                if _text == constants.YES:
                    # self.dat[constants.PASSWORD] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.PASSWORD:self.optionValidat_Text})
                    await self.validateFieldTextUser(update, chat_id)
                else:
                    await self.validateFieldTextUser(update, chat_id)

                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_CONFIRM_PLANS:
            error = False
            try:

                _text = self.arraysCites.plans[json_object["index"]]
                _index = json_object["index"]

                # self.dat["plans"] = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.PLANS: _index})
                
                self.data.get(chat_id).update(
                        {constants.HIDDEN_MENU: True})
                await self.persistentBtns(update, True, chat_id)
                
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_CONFIRM_MENU_PLANS:
            error = False
            try:

                _index = json_object["index"]
                _text = self.arraysCites.plans[_index]
                # self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PLANS,-1) = _index
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                    {constants.PLANS: _index})

                rspUpdatePerfil = await self.updatePerfil(update,chat_id)  

                if(rspUpdatePerfil):
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_PLANS_SELECTMENU_TEXT, -1)
                else:
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_PLANS_FAIL_TEXT, -1)
                    

                
                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT_METHOD:
            error = False
            try:
                _index = json_object["index"]
                _text = self.arraysCites.payment_method[_index]

                if _text != "":
                    # self.dat["typePayment"] = _index
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.PAYMENT: _index})
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_METHOD_PAYMENT_SELECTMENU_TEXT.replace("{}", _text))
                    self.data.get(chat_id).update(
                        {constants.HIDDEN_MENU: True})
                    await self.persistentBtns(update, True, chat_id)
                    return True
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))
                self.logger.error(
                    constants.WARNING_USER_PAYMENT_FAIL_TEXT, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_PAYMENT_FAIL_TEXT)

        elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT:
            error = False
            try:
                _text = self.arraysCites.payment_method[json_object["index"]]
                _index = json_object["index"]

                _value = False

                if(_index == 0):
                    _value = True

                if(_index == 1):
                    _value = False

                if _text != "":
                    # self.dat["payment"] = _value
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.PAYMENT: _value})
                    self.optionValidate = 3
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_REFERENCE_PAYMENT_FAIL_TEXT, False)
                self.data.get(chat_id).update({constants.HIDDEN_MENU: True})
                await self.persistentBtns(update, True, chat_id)

        elif json_object["action"] == constants.SUCESS_REFERENCE_PAYMENT:
            error = False
            try:
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                    # self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.REFERENCE_PAYMENT,"") = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.REFERENCE_PAYMENT: self.optionValidat_Text})
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_REFERENCE_PAYMENT_SELECTMENU_TEXT, False)
                    self.data.get(chat_id).update(
                        {constants.HIDDEN_MENU: True})
                    await self.persistentBtns(update, True, chat_id)

            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        elif json_object["action"] == constants.SUCESS_REFERENCE_MENU_PAYMENT:
            error = False
            try:
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                    # self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.REFERENCE_PAYMENT,"") = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                        {constants.REFERENCE_PAYMENT: self.optionValidat_Text})
                    await self.sendMessageTelChatId(chat_id, update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT)
                else:
                    await self.setReferenceMenu(update, chat_id)

            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.setReferenceMenu(update, chat_id)

        elif json_object["action"] == constants.SUCESS_USER_LOGIN_USERNAME or json_object["action"] == constants.SUCESS_USER_LOGIN_PASSWORD:
            error = False
            try:
                _text = self.arraysCites.confirm[json_object["index"]]
                if _text == constants.YES:
                    if(json_object["action"] == constants.SUCESS_USER_LOGIN_USERNAME):
                       # self.dat[constants.USERNAME] = self.optionValidat_Text
                        self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                            {constants.USERNAME: self.optionValidat_Text})

                    if(json_object["action"] == constants.SUCESS_USER_LOGIN_PASSWORD):
                        # self.dat[constants.PASSWORD] = self.optionValidat_Text
                        self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                            {constants.PASSWORD: self.optionValidat_Text})
                    await self.validateLoginUser(update, chat_id)
                else:
                    await self.validateLoginUser(update, chat_id)

                return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateLoginUser(update, chat_id)

        elif json_object["action"] == constants.SELECT_INPUT_MODIFY_PERFIL:
            error = False
            try:
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                            {constants.USERNAME: self.optionValidat_Text})
                    
                    result = self.arraysCites.data_perfil.get("data")
                    item = result[_index]
                    lbl = item.get("lbl")
                    code = item.get("code")
                    default = item.get("default")
                    array = item.get("array")
                    caseTitle = item.get("caseTitle")

                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update(
                            {lbl: default})
                    #asyncio.create_task(my_async_function())

                    fieldOptional = [constants.PLANS,constants.TYPE_PAYMENT,constants.REFERENCE_PAYMENT]

                    

                    if lbl in fieldOptional:
                        optionalDat = [lbl,code,array,default,caseTitle]
                        await self.validateFieldTextUser(update, chat_id,optionalDat)
                    else:
                        await self.validateFieldTextUser(update, chat_id)
            

                    return
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

            if error:
                await self.validateFieldTextUser(update, chat_id)

        else:
            self.logger.error("Actiones sin seleccion.",
                              extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            await query.answer()

            if text == "first":

                self.newSelect.page += 1
                await self.newSelect.select(update, 0, action, self.newSelect.page)

            if text == "after":

                self.newSelect.page -= 1
                await self.newSelect.select(update, 0, action, self.newSelect.page)

            if text == "paginatorP" and action == 2:

                self.page = json_object["page"]
                action = 2
                self.newSelect._paginatorActive = True
                await self.newSelect.select(update, 0, action, self.newSelect.page)
            else:
                if text == "pageselect" and action == 3:
                    action = 3
                    # print(f"JSON PAGE:{json_object['page']}")
                    self.page = json_object["page"]
                    self.newSelect._paginatorActive = True
                    await self.newSelect.select(update, 0, action, newPage)

        # print(f"query.message====={query.message}")
        # print(f"query.message.chat.message_id:{query.message.message_id}")
        # print(f"query.message:{query.message}")

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def clearMsgText(self, clearChatHistoryButtos, update, chat_id):

        if(chat_id == -1 or chat_id is None):
            self.logger.error("chat_id is None", extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            return
        
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False
        # updateReceiber = json.dumps(update.to_dict())
        # self.logger.info(self.data, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))
        

        chat_msgs = self.data.get(chat_id).get(constants.CHAT_MSG_USER, [])
        arryTemp = chat_msgs
        delete_sucess = []

        self.logger.info("✉️ Mensajes del usuario:%s, total:%s",
                                         str(chat_msgs),str(len(chat_msgs)), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        error = False
        error_str = ""

        if len(arryTemp) > 0:
            count = 0
            try:
                for x in arryTemp:

                    chat_ids = chat_id
                    message_id = x[1]
                    if(chat_ids != "" and message_id != ""):
                        self.logger.info("🧹 Eliminando msg id:%s",
                                         arryTemp[count], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                        deleteMsg = await self.bot.delete_message(chat_id=chat_ids, message_id=message_id)


                        time.sleep(1)
                        if(deleteMsg):
                            self.logger.info("🗑 Mensaje Eliminado: msg id: %s,resp:%s", arryTemp[count],deleteMsg, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                            delete_sucess.append(message_id)
                                
                        else:
                            self.logger.info(
                                " 🗑❌ El mensaje no se logro eliminar: msg id: %s,resp:%s", arryTemp[count],deleteMsg, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                    else:
                        del chat_msgs[count]
                        self.logger.info("🩹 Mensaje vacio o invalido:%s",
                                         chat_msgs[count], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                    
                    count += 1

                new_arrayMsgs = []
                arr_orden =[]

                for x in arryTemp:
                    arr_orden.append(x[1])

                for item in arr_orden:
                    if(delete_sucess.index(item) == -1):
                        self.logger.info("🩹 Mensaje pendiente por eliminar:%s",
                                         chat_msgs[count], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                        new_arrayMsgs.append([chat_id,item])

                self.data.get(chat_id).update(
                    {constants.CHAT_MSG_USER: new_arrayMsgs})
                
                if(len(new_arrayMsgs) > 0):
                    self.logger.info("😲 Todavia quedan mensajes por eliminar:%s",
                                         len(new_arrayMsgs), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                    new_arrayMsgs.append([chat_id,item])
                else:
                    self.logger.info("🧹🧹 Todos los mensajes fueron eliminados.", extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                    new_arrayMsgs.append([chat_id,item])



            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                error_str = timedOutError
            except NetworkError as networkError:
                self.logger.info(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                if(str(networkError).find("not found") != -1):
                    self.logger.warning(networkError, extra=self.data.get(
                        chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                    del chat_msgs[count]
                else:
                    error = True
                    self.logger.error(networkError, extra=self.data.get(
                        chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

                error_str = networkError

            except Exception as errors:
                error_str = errors
                self.logger.info(errors, self.extra_params)
                if(str(errors).find("Message to delete not found") != -1):
                    self.logger.warning(errors, extra=self.data.get(
                        chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                else:
                    error = True
                    self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                        constants.EXTRA_PARAMS, self.extra_params))

            if(error):
                time.sleep(1)

        count = + 1
        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def persistentBtns(self, update, updates=False, chat_id=-1):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        error = False

        if(chat_id == -1 or chat_id == None):
            self.logger.warning('⚠️ Sin chat id', extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            return False

        hidden_menu = self.data.get(chat_id).get(constants.HIDDEN_MENU, False)
        menuDat = self.data.get(chat_id).get(constants.MENU_DAT, [])
        msgsMenuShowAndHide = self.data.get(chat_id).get(
            constants.DATA_MSGS_MENU_SHOW_AN_DHIDE, [])

        self.logger.info("📘 msgsMenuShowAndHide:%s",
                         msgsMenuShowAndHide, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        self.logger.info("📘 hidden_menu:%s", hidden_menu,
                         extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        self.logger.info("📘 Total items en menuDat:%s",
                         len(menuDat), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        if(msgsMenuShowAndHide is None or hidden_menu is None or menuDat is None):
            self.logger.error("Error not key in %s", self.data.get(
                chat_id), extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            return False

        try:
            if(len(menuDat) > 0 and not updates):
                self.logger.info(
                    "No se requiere actualizar el menu.", extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                return

            arrBtnsPersistent = []

            signup = InlineKeyboardButton(
                constants.SIGNUP, callback_data='/signup')
            login = InlineKeyboardButton(
                constants.ENTRAR, callback_data='/login')
            plans = InlineKeyboardButton(
                constants.PLANS_TEX, callback_data='/plans')
            setReference = InlineKeyboardButton(
                constants.SET_MENU_REFERENCE_PAYMENT, callback_data='/setReference')
            setMethoPayment = InlineKeyboardButton(
                constants.SET_MENU_METHOD_PAYMENT, callback_data='/setMethoPayment')
            history = InlineKeyboardButton(
                'Historial', callback_data='/history')
            logout = InlineKeyboardButton(
                constants.CERRAR_SESION, callback_data='/logout')
            hidde = InlineKeyboardButton(
                constants.HIDDEN, callback_data='/hidden')
            show = InlineKeyboardButton(
                constants.SHOW, callback_data='/hidden')
            information = InlineKeyboardButton(
                constants.INFORMATION, callback_data='/information')
            
            update_information = InlineKeyboardButton(
                constants.UPDATE_INFORMATION, callback_data='/updateInformation')

            self.data.get(chat_id).update(
                {constants.DATA_MSGS_MENU_SHOW_AN_DHIDE: []})

            if(len(menuDat) > 10000):

                menu = menuDat[0]

                self.logger.info(menu, extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

                chat_id = menu.chat.id
                message_id = menu.message_id

                self.logger.info("❌ Quitando menu con message_id:%s en chat:%s",
                                 message_id, chat_id, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

                await self.bot.delete_message(chat_id=chat_id, message_id=message_id)

                self.data.get(chat_id).update({constants.MENU_DAT: []})
                menuDat = []

            if(not hidden_menu):
                self.logger.info(constants.HIDDEN_MENU_TEXT,
                                 extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                arrBtnsPersistent = []
                arrBtnsPersistent.append([show])
                reply_markup = ReplyKeyboardMarkup(
                    arrBtnsPersistent, resize_keyboard=True, one_time_keyboard=False)
                menu = await self.bot.send_message(chat_id=chat_id, text="🖋", reply_markup=reply_markup)
                
                
                self.data.get(chat_id).get(constants.CHAT_MSG_USER,[]).append([chat_id,menu.message_id])
                
                self.logger.info(menu, extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

                self.data.get(chat_id).update(
                    {constants.MENU_DAT: [menu, update]})

                self.logger.info("💬 Agregando menu en chat:%s",
                                 menu.chat.id, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

                return

            else:
                if(self.data.get(chat_id).get(constants.TOKEN_ASILO, "") != ""):
                    if(not self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PAYMENT,False) and not self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SUCESS,False)):
                        if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PLANS,-1) == -1 or self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.REFERENCE_PAYMENT,"") == ""):
                            self.logger.info(
                                constants.SHOW_MENU_NOT_PAYMENT_TEXT, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                            arrBtnsPersistent.append(
                                [update_information,logout,hidde])

                        else:
                            if(self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.PLANS,-1) != -1 and self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.REFERENCE_PAYMENT,"") != "" and not self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).get(constants.SUCESS,False)):
                                self.logger.info(
                                    constants.SHOW_MENU_NOT_PAYMENT_TEXT, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
                                await self.sendMessageTelChatId(chat_id, update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT, -1)
                                arrBtnsPersistent.append([update_information, logout])

                else:
                    arrBtnsPersistent.append([signup, login, hidde])

                reply_markup = ReplyKeyboardMarkup(
                    arrBtnsPersistent, resize_keyboard=True, one_time_keyboard=False)
                # reply_markup = ReplyKeyboardRemove()

                receiber = await self.context.bot.send_message(chat_id=chat_id, text="...", reply_markup=reply_markup)

                self.data[chat_id].update(
                    {constants.MENU_DAT: [receiber, update]})

        except TimedOut as timedOutError:
            if(str(timedOutError).find("not found") != -1):
                self.logger.warning(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            else:
                error = True
                self.logger.error(timedOutError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except NetworkError as networkError:
            if(str(networkError).find("not found") != -1):
                self.logger.warning(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            else:
                error = True
                self.logger.error(networkError, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
        except Exception as errors:
            if(str(errors).find("not found") != -1):
                self.logger.warning(errors, extra=self.data.get(
                    chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            else:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.data.get(chat_id).get(
                    constants.EXTRA_PARAMS, self.extra_params))

        if(error):
            time.sleep(3)


        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def handle_text(self, update, context):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(update.message.chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        # self.logger.info(update,extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))
        chat_id = update.message.chat_id
        text = update.message.text
        messageId = update.message.message_id

        self.context = context

        if(chat_id is None):
            self.logger.error("Sin chat id.", extra=self.data.get(
                chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            return

        await self.setIdChat(update, chat_id)

        await self.setTokenUser(chat_id)

        await self.setUserTelegram(update, chat_id)

        await self.persistentBtns(update, False, chat_id)

        selfUpdate = json.dumps(update.to_dict())
        # self.logger.info(selfUpdate,extra= self.extra_params)

        text = ""

        messageId = -1

        if(update.message.chat_id is not None):
            text = update.message.text
            chat_id = update.message.chat_id
            messageId = update.message.message_id
            chat_id = chat_id
            # self.logger.info("text:%s, chat id:%s, message id:%s",text,chat_id,messageId,extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS,self.extra_params))

        if (chat_id is not None):
            if text.find(".") != -1:
                text = text.replace(".", "\.")

            self.chatUserSend = chat_id
            chatUserMsgId = messageId
            self.optionValidat_Text = text
            validateFormText = True

            self.logger.info("Text User:%s,optionValidate:%s,chat_id:%s,messageId:%s",
                             text, self.optionValidate, chat_id, messageId, extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))
            
            if(text == constants.ENTRAR  or text == constants.CERRAR_SESION or text == constants.HIDDEN.replace("\u00fa", "ú") or text == constants.SHOW.replace("\u00fa", "ú") or text == constants.PLANS_TEX or text == constants.SET_MENU_REFERENCE_PAYMENT or text == constants.SET_MENU_METHOD_PAYMENT or text == constants.INFORMATION or text == constants.SIGNUP or text == constants.UPDATE_INFORMATION  or self.optionValidate == 7):
                asyncio.create_task(self.bot.delete_message(chat_id=chat_id, message_id=messageId))

            hidden_menu = self.data.get(chat_id).get(
                constants.HIDDEN_MENU, False)

            msgsMenuShowAndHide = self.data.get(chat_id).get(
                constants.DATA_MSGS_MENU_SHOW_AN_DHIDE, [])

            if(text == constants.ENTRAR):
                self.optionValidate = 8
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.USERNAME: ""})
                self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.PASSWORD: ""})
                self.data.get(chat_id).update({constants.TOKEN_ASILO: ""})
                self.data.get(chat_id).get(constants.EXTRA_PARAMS).update({constants.USERNAME_ASILO_BOT: ""})
                

            if(text == constants.CERRAR_SESION):
                self.optionValidate = 9
                

            if(text == constants.HIDDEN.replace("\u00fa", "ú") or text == constants.SHOW.replace("\u00fa", "ú")):

                hidden_menu = self.data.get(chat_id).get(
                    constants.HIDDEN_MENU, False)

                msgsMenuShowAndHide.append(hidden_menu)

                self.data.get(chat_id).update(
                    {constants.DATA_MSGS_MENU_SHOW_AN_DHIDE: msgsMenuShowAndHide})

                self.data.get(chat_id).update(
                    {constants.HIDDEN_MENU: not hidden_menu})

                validateFormText = False

                await self.persistentBtns(update, True, chat_id)

                try:
                    await self.bot.delete_message(chat_id=chat_id, message_id=messageId)
                except Exception:
                    print("")
            

            if(text == constants.PLANS_TEX):
                self.optionValidate = 12

            if(text == constants.SET_MENU_REFERENCE_PAYMENT):
                self.optionValidate = 14

            if(text == constants.SET_MENU_METHOD_PAYMENT):
                self.optionValidate = 16

            if(text == constants.INFORMATION):
                self.optionValidate = 17

            if(text == constants.SIGNUP):
                self.optionValidate = 18

            if(text == constants.UPDATE_INFORMATION):
                self.optionValidate = 19


            if validateFormText:
                if self.optionValidate == 0:
                    await self.confirm_document(update, chat_id)
                elif self.optionValidate == 1:
                    await self.confirm_name(update, chat_id)
                elif self.optionValidate == 2:
                    await self.confirm_birth(update, chat_id)
                elif self.optionValidate == 3:
                    await self.confirm_reference_payment(update, chat_id)
                elif self.optionValidate == 4:
                    await self.confirm_username(update, chat_id)
                elif self.optionValidate == 5:
                    await self.confirm_password(update, chat_id)
                elif self.optionValidate == 6:
                    # self.dat[constants.USERNAME] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.USERNAME:self.optionValidat_Text})
                    await self.validateLoginUser(update, chat_id)
                elif self.optionValidate == 7:
                    # self.dat[constants.PASSWORD] = self.optionValidat_Text
                    self.data.get(chat_id).get(constants.CHAT_DATA_PERFIL,self.datDefault).update({constants.PASSWORD:self.optionValidat_Text})
                    
                    await self.validateLoginUser(update, chat_id)
                elif self.optionValidate == 8:
                    await self.LoginUser(update, self.context, chat_id)
                elif self.optionValidate == 9:
                    await self.LogoutUser(update, self.context, chat_id)
                elif self.optionValidate == 12:
                    await self.plansMenu(update, chat_id)
                elif self.optionValidate == 13:
                    msg = await self.sendMessageTelChatId(chat_id, update, constants.USER_PLANS_SELECTMENU_TEXT)
                elif self.optionValidate == 14:
                    await self.setReferenceMenu(update, chat_id)
                elif self.optionValidate == 15:
                    await self.confirm_reference_Menu_payment(update, chat_id)
                elif self.optionValidate == 16:
                    await self.payment_method(update, chat_id)
                elif self.optionValidate == 17:
                    await self.getPerfil(update, chat_id)
                elif self.optionValidate == 18:
                    await self.signup(update, context)
                elif self.optionValidate == 19:
                    await self.listButtonsModifiedPerfil(update, chat_id)

                else:
                    await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_TEXT,add_clearList=True)
                    self.data.get(chat_id).update({constants.HIDDEN_MENU: True})
                    await self.persistentBtns(update, True, chat_id)
                    time.sleep(1)

        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    async def testtable(self, update, context):
       await self.clearMsgText(True,update,update.message.chat_id)


    async def menu(self, update, context):
        update = update
        update = update

        chat_id = update.message.chat_id

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

        hidden_menu = getattr(self.data, 'hidden_menu', [])
        hidden_menu = not hidden_menu
        setattr(self.data, "hidden_menu", hidden_menu)

        await self.persistentBtns(update, True, chat_id)
        self.logger.info(constants.END, extra=self.data.get(
            chat_id).get(constants.EXTRA_PARAMS, self.extra_params))

    def main(self) -> None:
        error = False
        try:
            # persistence = PicklePersistence(filepath="conversationbot")
            
            


            self.application = Application.builder().token(self.token).build()
            # self.application = Application.builder().token(self.token).persistence(persistence).build()

            self.application.add_handler(CommandHandler("start", self.start))

            self.application.add_handler(CommandHandler("signup", self.signup))

            self.application.add_handler(
                CommandHandler("testtable", self.testtable))

            self.application.add_handler(
                CommandHandler("login", self.LoginUser))

            self.application.add_handler(
                CommandHandler("logout", self.LogoutUser))

            self.application.add_handler(CommandHandler("menu", self.menu))

            self.application.add_handler(CallbackQueryHandler(self.button))

            self.application.add_handler(
                MessageHandler(filters.TEXT, self.handle_text))

            self.application.run_polling()

        except Exception:
            error = True

        if(error):
            time.sleep(5)
            nest_asyncio.apply()
            citaAsilobot().main()


if __name__ == "__main__":
    nest_asyncio.apply()
    citaAsilobot = citaAsilobot()
    citaAsilobot.main()
