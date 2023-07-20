# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
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
import base64
import re
from telegram.error import TimedOut
from telegram.error import NetworkError
import requests
import time
import datetime
import time
import inspect
import threading
import asyncio
from signup import signup
from validate_user import validate_user
from utilis import utils
from datatemps import datatemps
from menu import menu

CHOOSING, TYPING_REPLY, TYPING_CHOICE, BIO, SIGNUP, DOCUMENT, SIGNUP, TOKEN = range(
    8)


class citaAsilobot:
    token = "5940401924:AAHUZEP6BtTOWPk2Zvy5uQOatI8b8JySVu8"
    bot = telegram.Bot(token=token)
    arraysCites = datArray_cites.array_cites()
    data = {}
    url = "http://localhost:3004/server"
    isLogin = False
    
    def __init__(self):
        data={}
        # self.data = threading.local()
        # setattr(self.data, 'menuDat', [])
        a = 1
        self._text_intentns = ["Primera", "Segunda", "Tercera y ultima"]
        self.timeout_seconds = 10
        self.text_Loading = "🔤🔤🔤🔤🔤🔤🔤🔤"
        self.cita_asilobot = None
        
        self.data = {}

        self.chaIds = -1
        self.usernameTelegram = "-"
        self.usernameAsiloBot = "-"
        self.chatSend = ""
        self.chatMsgUser = []
        self.chatMsgMenu = []

        self.url = "http://localhost:3004/server"

        responseSingup = ''
        self.blockUser = False
        self.isErrorFormulary = False
        
    
    
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

    

    print(" -*- Inicio asiloBot -*- ")

    async def LogoutUser(self, update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=-1) -> None:
        if(chat_id == -1):
            chat_id = update.message.chat_id
            self.logger.info(constants.START + ":" + inspect.stack()
                             [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        
        

        if(dataUser.get(constants.TOKEN_ASILO, "") == ""):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_NOT_LOGIN_TEXT, -1)
        else:
            self.logger.info("Cerrando sesion de usuario",extra=constants.extra_params.copy())
            self.data = {chat_id:{constants.CHAT_DATA_PERFIL:constants.datDefault.copy()}}
            citaAsilobot.data = {chat_id:{constants.CHAT_DATA_PERFIL:constants.datDefault.copy()}}
            
            await self.sendMessageTelChatId(chat_id, update, constants.SUCESS_USER_LOGOUT_SUCESS_TEXT,-1,False)
           
            self.logger.info(self.data.get(chat_id), extra=dataUser.get(constants.EXTRA_PARAMS))
            self.logger.info(citaAsilobot.data.get(chat_id), extra=dataUser.get(constants.EXTRA_PARAMS))

            await self.cancelProcess(update,chat_id)
            
            self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def loginAsiloBot(self, update, chat_id):
        code_response = -1
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        _error = False

        if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, '') != "" and dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PASSWORD, '') != ""):
            payload = "username=" + \
                dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, '')+"&password=" + \
                dataUser.get(constants.CHAT_DATA_PERFIL,
                                           constants.datDefault.copy()).get(constants.PASSWORD, '')
            headers = {"Content-Type": "/x-www-form-urlencoded"}

            try:
                response = requests.request(
                    "POST", self.url + "/login", headers=headers, data=payload
                )
                _response = json.loads(response.text)
                code_response = response.status_code

                self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", response.text), extra=dataUser.get(constants.EXTRA_PARAMS))
                self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", str(response.status_code)), extra=dataUser.get(constants.EXTRA_PARAMS))
                
                if(code_response == -1):
                    _error = True
                    
            except Exception as error:
                self.logger.error(str(error) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))
                _error = True
                
            if(not _error):
                dataUser.update(
                    {constants.ACTIONS_USER: constants.ACTION_USER_BOT_LOGIN})
                await self.registerUser_validate(update, response, chat_id)
            else:
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT,-1)
        else:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGOUT_SUCESS_TEXT,-1,False)
            dataUser.update({constants.ISLOGIN:True})
            await self.validateLoginUser(update, False, chat_id)

        
        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))
        return _error

    async def updatePerfil(self, update, chat_id):

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        _error = False

        if(len(dataUser.get(constants.CHAT_DATA_PERFIL, {})) > 10):

            headers = {"Content-Type": "/x-www-form-urlencoded",
                       "Authorization": "Bearer " + dataUser.get(constants.TOKEN_ASILO)}

            payload = dataUser.get(constants.CHAT_DATA_PERFIL)

            self.logger.info("Request:" + str(payload), extra=dataUser.get(constants.EXTRA_PARAMS))

            try:
                response = requests.request(
                    "PATCH", self.url + "/profile", headers=headers, data=payload
                )
                response_json = json.loads(response.text)

                if(len(response_json) > 0):
                    await self.sendMessageTelChatId(chat_id, update, constants.USER_PERFIL_UPTADATE_SUCESS_TEXT, -1,False)

                self.logger.info(constants.RESPONSE_API_CORE.replace(
                    "{msg}", response.text), extra=dataUser.get(constants.EXTRA_PARAMS))
                return True
            except Exception as error:
                self.logger.error(str(error) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))
                _error = True
            finally:
                await self.listButtonsModifiedPerfil(update, chat_id)
                if(_error):
                    await self.sendMessageTelChatId(chat_id, update, constants.WARNING_PERFIL_UPDATE_TEXT_GENERAL_TEXT, -1)

        else:
            self.logger.error("No se encontro perfil o no cumple con los campos requeridos: Perfil:%s, Campos:%s", dataUser.get(constants.CHAT_DATA_PERFIL, {}), str(len(dataUser.get(constants.CHAT_DATA_PERFIL, {}))), extra=dataUser.get(constants.EXTRA_PARAMS))
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_PERFIL_UPDATE_TEXT_GENERAL_TEXT, -1)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def validateLoginUser(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        dataUser.update({constants.ISLOGIN:True})
        

        try:
            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, '') == "" or dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PASSWORD, '') == ""):
                if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, '') == "":
                    await self.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 6,False)
                    return False

                if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PASSWORD, '') == "":
                    await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 7,False)
                    return False
            else:
                if(not error):
                    isErrorLogin = await self.loginAsiloBot(update, chat_id)
                    if(isErrorLogin):
                        await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT, -1,False)
                        dataUser.update(
                            {constants.HIDDEN_MENU: True})
                        await self.cancelProcess(update,chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True

            _finError = str(errors).find("Failed to establish")
            if(_finError != -1):
                self.logger.warning(errors, extra=dataUser.get(constants.EXTRA_PARAMS))
            else:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_ERROR_GENERAL, -1)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def clearUpdatePerfil(self, update, chat_id):

        try:
            msgOld = dataUser.get(
                constants.UPDATE_PERFIL_MESSAGE_ID, -1)
            msgReadyOld = dataUser.get(
                constants.READY_UPDATE_PERFIL_MESSAGE_ID, -1)

            if(msgOld != -1):
                await self.bot.delete_message(chat_id=chat_id, message_id=msgOld)

            if(msgReadyOld != -1):
                await self.bot.delete_message(chat_id=chat_id, message_id=msgReadyOld)

        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            self.logger.error(errors, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def listButtonsModifiedPerfil(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        # await self.clearMsgText(True,update,chat_id)
        await self.clearUpdatePerfil(update, chat_id)
        dataPerfil = await self.getPerfil(update, chat_id)

        self.logger.info(dataPerfil, extra=dataUser.get(constants.EXTRA_PARAMS))

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
                     #self.logger.info("%s,%s",clave,str(valor), extra=dataUser.get(constants.EXTRA_PARAMS))
                    if(len(item.get("array", [])) > 0):
                        if(valor == -1 or (type(valor) == str and str(valor).strip() == "")):
                            dat.append(text + "--")
                        else:
                            dat.append(text + item.get("array", [])[valor])
                    else:
                        if(valor == -1 or (type(valor) == str and str(valor).strip() == "")):
                            dat.append(text + "--")
                        else:
                            dat.append(text + str(valor))

        if(len(dat) > 0):

            dataUser.update(
                {constants.ACTIONS_USER: constants.ACTION_USER_BOT_UPDATE_PERFIL})

            msg = await self.sendesplegableButton(update, dat, 17, constants.SELECT_INPUT_MODIFY_PERFIL, 1, 20, chat_id=chat_id, delete=False)

            dataUser.update(
                {constants.UPDATE_PERFIL_MESSAGE_ID: msg.message_id})

            msg_ready = await self.sendesplegableButton(update, self.arraysCites.finishUpdateProdifle, 19, constants.FINISH_UPDATE, 1, 20, chat_id=chat_id, delete=False)

            dataUser.update(
                {constants.READY_UPDATE_PERFIL_MESSAGE_ID: msg_ready.message_id})

            dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                {constants.OPTIONVALIDAT_TEXT: ""})
            dataUser.get(constants.CHAT_DATA_PERFIL,
                          constants.datDefault.copy()).update({constants.OPTIONVALIDATE: -1})

        else:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_GET_PERFIL_NOT_DATA_TEXT, -1)

    async def getDataText(self, data, chat_id):
        json = {}

        if(data.get(constants.PLANS) is not None and data.get(constants.PLANS) != -1):
            json.update(
                {constants.PLANS: self.arraysCites.plans[data.get(constants.PLANS)]})

        if(data.get(constants.ACTION) is not None and data.get(constants.ACTION) != -1):
            json.update(
                {constants.ACTION: self.arraysCites.actions[data.get(constants.ACTION)]})

        if(data.get(constants.PAYMENT) is not None and data.get(constants.PAYMENT) == 1):
            json.update({constants.PAYMENT: "Pago realizado con exito"})
        else:
            json.update({constants.PAYMENT: "En espera de su pago"})

        if(data.get(constants.METHOD_PAYMENT) is not None and data.get(constants.METHOD_PAYMENT) != -1):
            json.update({constants.METHOD_PAYMENT: self.arraysCites.payment_method[data.get(
                constants.METHOD_PAYMENT)]})

        if(data.get(constants.REFERENCE_PAYMENT) is not None and data.get(constants.REFERENCE_PAYMENT) != ""):
            json.update({constants.REFERENCE_PAYMENT: data.get(
                constants.REFERENCE_PAYMENT)})
        else:
            json.update({constants.REFERENCE_PAYMENT: "Sin referencia"})

        if(data.get(constants.USERNAME) is not None and data.get(constants.USERNAME) != ""):
            json.update({constants.USERNAME: data.get(constants.USERNAME)})

        if(data.get(constants.PROVINCIAGENERAL) is not None and data.get(constants.PROVINCIAGENERAL) != -1):
            json.update({constants.PROVINCIAGENERAL: self.arraysCites.provinces[data.get(
                constants.PROVINCIAGENERAL)]})

        if(data.get(constants.TRAMITE_CUERPO_POLICIAL) is not None and data.get(constants.TRAMITE_CUERPO_POLICIAL) != -1):
            json.update({constants.TRAMITE_CUERPO_POLICIAL: self.arraysCites.tramite_cuerpo_nacional_policial[data.get(
                constants.TRAMITE_CUERPO_POLICIAL)]})

        if(data.get(constants.TYPEDOC) is not None and data.get(constants.TYPEDOC) != -1):
            json.update(
                {constants.TYPEDOC: self.arraysCites.tipo_doc[data.get(constants.TYPEDOC)]})

        if(data.get(constants.DOC) is not None and data.get(constants.DOC) != ""):
            json.update({constants.DOC: data.get(constants.DOC)})

        if(data.get(constants.NAME) is not None and data.get(constants.NAME) != ""):
            json.update({constants.NAME: data.get(constants.NAME)})

        if(data.get(constants.BIRTH) is not None and data.get(constants.BIRTH) != ""):
            json.update({constants.BIRTH: data.get(constants.BIRTH)})

        if(data.get(constants.COUNTRY) is not None and data.get(constants.COUNTRY) != ""):
            json.update(
                {constants.COUNTRY: self.arraysCites.countrys[data.get(constants.COUNTRY)]})

        if(data.get(constants.SEDE) is not None and data.get(constants.SEDE) != ""):
            json.update(
                {constants.SEDE: self.arraysCites.oficines[data.get(constants.SEDE)]})

        self.logger.info(json, extra=dataUser.get(
            constants.EXTRA_PARAMS, constants.extra_params.copy()))

        return json

    async def getPerfil(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        _response = {}
        error = False
       # token = dataUser.get(constants.TOKEN_ASILO)
       # self.logger.info(token, self, extra=dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy()))

        headers = {"Content-Type": "/x-www-form-urlencoded",
                   "Authorization": "Bearer " + dataUser.get(constants.TOKEN_ASILO)}

        dataUser.update(
            {constants.ACTIONS_USER: constants.ACTION_USER_BOT_UPDATE_PERFIL})

        try:
            response = requests.request(
                "GET", self.url + "/profile", headers=headers
            )
            _response = json.loads(response.text)

            dataUser.update(
                {constants.CHAT_DATA_PERFIL: _response})

            self.logger.info(constants.RESPONSE_API_CORE.replace(
                "{msg}", response.text), extra=dataUser.get(constants.EXTRA_PARAMS))

            self.logger.info(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()),
                             extra=dataUser.get(constants.EXTRA_PARAMS))

            # terminar metodo
            self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
        finally:
            if(error):
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_GET_PERFIL_FAIL_TEXT, -1)

            return _response

    async def LoginUser(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        #await self.valid_user_chat(update)
        
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.data.get(update.message.chat_id).get(constants.EXTRA_PARAMS))
        update = update
        
        chat_id = update.message.chat_id

        if(chat_id == -1):
            chat_id = update.message.chat_id

        if(self.blockUser):
            await self.sendMessageTelChatId(chat_id, update, constants.BLOCKED_USER_TEXT, -1)

        dataUser.update({constants.ISLOGIN:True})

        if(dataUser.get(constants.TOKEN_ASILO, "") != "" and dataUser.get(constants.EXTRA_PARAMS).get(constants.USERNAME_ASILO_BOT) != ""):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_ALREADY_LOGIN, -1)
            return

        if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, '') == "" or dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PASSWORD, '') == ""):
            dataUser.update(
            {constants.ACTIONS_USER: constants.ACTION_USER_BOT_LOGIN})
            await self.persistentBtns(update, True, chat_id)
            await self.validateLoginUser(update, chat_id)
        else:
            isErrorLogin = await self.loginAsiloBot(update, chat_id)
            if(isErrorLogin):
                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT, -1)
                dataUser.update({constants.HIDDEN_MENU: True})
                await self.persistentBtns(update, True, chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

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

    async def registerUser_validate(self, update, response, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        sucess = True
        valid = True
        
        try:
            _json = json.loads(response.text)
            code_response = response.status_code
            
            self.logger.info(str(code_response), extra=dataUser.get(constants.EXTRA_PARAMS))
            token = _json.get("token")
            
            if(code_response == constants.httpOk or code_response == constants.httpOkreply):
                if(token is not None):
                    dataUser.update({constants.TOKEN_ASILO: token})

                    
                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_LOGIN):

                        await self.sendMessageTelChatId(chat_id, update, constants.SUCESS_USER_LOGIN_TEXT, -1, False)
                        
                        await self.setUserBot(update,chat_id)
                        
                        dataUser.update(
                            {constants.HIDDEN_MENU: True})
                        await self.persistentBtns(update, True, chat_id)
                        await self.getPerfil(update, chat_id)

                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_SIGNUP):
                                await self.sendMessageTelChatId(chat_id, update, constants.USER_REGISTER_SUCESS_TEXT, -1,False)
                                dataUser.update({constants.CHAT_DATA_PERFIL:constants.datDefault.copy()})
                                await menuBot.clearMsgText()
                                self.logger.info(
                                    constants.USER_REGISTER_SUCESS_TEXT, extra=dataUser.get(constants.EXTRA_PARAMS))
                                await self.persistentBtns(update, update, chat_id=chat_id)
            if(code_response == 422):
                    msg_api = _json.get("message","")
                    if(msg_api == constants.WARNING_API_WRONG_PASSWORD):
                                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_API_WRONG_PASSWORD_TEXT, -1,False)
                                await self.cancelProcess(update, chat_id)

                    if msg_api == constants.BLOCKED_USER:
                                self.isErrorFormulary = True
                                self.timBlockUser()
                                self.blockUser = True
                                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_API_WRONG_PASSWORD_TEXT, -1,False)
                                await self.sendMessageTelChatId(chat_id, update, constants.BLOCKED_USER_TEXT, -1,False)
                                valid = False
                                await self.cancelProcess(update, chat_id)
                                return False
                        
                    error_msg = _json.get("errors", {"msg": []}).get("msg")
                    if(len(error_msg) > 0):
                        if(type(error_msg) == "list"):
                            for error in error_msg:
                                if(error.get("msg") == constants.MISSING):
                                    await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_INTENTS_TEXT, -1)
                                    valid = False
                    else:   
                        error_msg = _json.get("errors",{"msg": ""}).get("msg","")
                        if(error_msg != ""):
                            valid = False
                            if error_msg == constants.WARNING_API_USERNAME_ALREADY_EXIST:
                                dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                                    {constants.USERNAME: ""})
                                await self.sendMessageTelChatId(chat_id, update, constants.WARNING_API_USERNAME_ALREADY_EXIST_TEXT, -1)
                                self.isErrorFormulary = True
                                await validate_data.validateFieldTextUser(update)

                        
            dataUser.update({constants.HIDDEN_MENU: True})

            return valid

        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
            sucess = False
        except NetworkError as networkError:
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            sucess = False
        except Exception as errors:
            sucess = False
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

            return False





    async def registerUser(self, update, chat_id) -> int:
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        headers = {"Content-Type": "/x-www-form-urlencoded",
                   "Accept-Language": "en"}
        _payload = ""
        try:
            # $.message.chat.id
            # self.logger.info(update_json, extra=dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy()))

            # message_id = update.callback_query.message.message_id

            if(chat_id == '' or chat_id is None):
                update_jsonStr = json.dumps(update.callback_query.to_dict())
                update_json = json.loads(update_jsonStr)
                chat_id = update_json['message']['chat']['id']

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, "") != ''):
                _payload += "username=" + dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.USERNAME, '') + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.USERNAME), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PROVINCIAGENERAL, -1) != -1):
                _payload += "provinciaGeneral=" + \
                    str(dataUser.get(constants.CHAT_DATA_PERFIL,
                        constants.datDefault.copy()).get(constants.PROVINCIAGENERAL, -1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.PROVINCIAGENERAL), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.SEDE, -1) != -1):
                _payload += "sede=" + str(dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.SEDE, -1)) + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.SEDE), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.TRAMITE_OFICINA, -1) != -1):
                _payload += "tramite_oficina=" + \
                    str(dataUser.get(constants.CHAT_DATA_PERFIL,
                        constants.datDefault.copy()).get(constants.TRAMITE_OFICINA, -1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.TRAMITE_OFICINA), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.TRAMITE_CUERPO_POLICIAL, -1) != -1):
                _payload += "tramite_cuperto_policial=" + \
                    str(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(
                        constants.TRAMITE_CUERPO_POLICIAL, -1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.TRAMITE_CUERPO_POLICIAL), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.TYPEDOC, -1) != -1):
                _payload += "typeDoc=" + str(dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.TYPEDOC, -1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.TRAMITE_CUERPO_POLICIAL), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.DOC, '') != ''):
                _payload += "doc=" + dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.DOC, '') + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.DOC), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.NAME, '') != ''):
                _payload += "name=" + dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.NAME, '') + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.NAME), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.BIRTH, '') != ''):
                _payload += "birth=" + str(dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.BIRTH, '')) + "&"
            else:
                self.logger.error(
                    constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace("{}", constants.BIRTH), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.COUNTRY, -1) != -1):
                _payload += "country=" + str(dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.COUNTRY, -1)) + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.COUNTRY), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PASSWORD, '') != ''):
                _payload += "password=" + dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PASSWORD, '') + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.PASSWORD), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.EMAIL, '') != ''):
                _payload += "email=" + dataUser.get(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.EMAIL, '') + "&"
            else:
                self.logger.error(constants.WARNING_FIELD_EMPTY_OR_INVALID_TEXT.replace(
                    "{}", constants.EMAIL), extra=dataUser.get(constants.EXTRA_PARAMS))
                await validate_data.validateFieldTextUser(update)
                return False

            _payload += "role=" + "user" + "&" + \
                "chat_id=" + str(chat_id) + "&"

            payload = _payload
            caracter_remove = payload[-1:len(payload)]
            if(caracter_remove == '&'):
                payload = payload[:-1]

            self.logger.info(payload, extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

            await self.sendMessageTelChatId(chat_id, update, constants.USER_REGISTER_PROCESS_TEXT, -1,False)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        sucess_Singup = False
        timetOut = False

        try:
            errorRequest = False
            responseSingup = requests.request(
                "POST", self.url + "/register", headers=headers, data=payload)

            responseSingoToJson = json.loads(responseSingup.text)

            self.logger.info(responseSingoToJson, extra=dataUser.get(constants.EXTRA_PARAMS))

            dataUser.update(
                {constants.ACTIONS_USER: constants.ACTION_USER_BOT_SIGNUP})

            sucess_Singup = await self.registerUser_validate(update, responseSingup, chat_id)

            if(sucess_Singup):
                return True

        except TimedOut as timedOutError:
            errorRequest = True
            timetOut = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            errorRequest = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            errorRequest = True
           # if(str(error).find("NoneType")):
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if(timetOut):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_LOGIN_TEXT_GENERAL_TEXT, -1)
            dataUser.update({constants.HIDDEN_MENU: True})
            await self.persistentBtns(update, True, chat_id)
        else:
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_INTENTS_TEXT.replace("{}", ""), -1)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def setLogger(self):
        self.formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(tokeUser)s %(name)s %(funcName)s %(filename)s %(lineno)d %(message)s"
        )
        self.handler.setFormatter(self.formatter)

                   
    async def setUserBot(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:
            user = dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.USERNAME)
            
            dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy()).update(
                {constants.USERNAME_ASILO_BOT: user})
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))


            
    
    async def oficine(self, update, chat_id) -> int:
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.SEDE, -1) != -1:
            await self.oficine_extrajera(update, chat_id)
        else:
            try:
                dat = self.arraysCites.oficines
                await self.sendesplegableButton(update,
                                                dat, 2, constants.SUCESS_OFICINE, 1, 8, chat_id=chat_id)

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
            except NetworkError as networkError:
                error = True
                self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            except Exception as errors:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))

            if(error):
                await self.oficine(update, chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def oficine_extrajera(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False

        if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.TRAMITE_OFICINA, -1) != -1:
            await self.tramite_cuerpo_policial(update, chat_id)
        else:
            try:

                dat = self.arraysCites.tramite_oficine_extrajera

                await self.sendesplegableButton(update,
                                                dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8, chat_id=chat_id)
            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
            except NetworkError as networkError:
                self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
                error = True
            except Exception as errors:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))
                error = True
            if(error):
                await self.oficine_extrajera(update, chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    

    async def tramite_cuerpo_policial(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.TRAMITE_CUERPO_POLICIAL, -1) != -1:
            await self.tipo_doc(update, chat_id)
        else:
            try:
                dat = self.arraysCites.tramite_cuerpo_nacional_policial

                await self.sendesplegableButton(update,
                                                dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8, chat_id=chat_id)

            except TimedOut as timedOutError:
                self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
                await self.tramite_cuerpo_policial(update, chat_id)
            except NetworkError as networkError:
                self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
                await self.tramite_cuerpo_policial(update, chat_id)
            except Exception as errors:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))
                await self.tramite_cuerpo_policial(update, chat_id)
        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def tipo_doc(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        await validate_data.validateFieldTextUser(update)
        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_document(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:

            if(not await utilis.utils.validateDoc(self, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""))):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_DOC_FORMAT, -1, parseMode="html")
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.ENTER_DOCUMENT_TEXT, 0)
                return False

            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update, dat, 7, constants.SUCESS_CONFIRM_DOCUMENT, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            self.confirm_document(update, chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_name(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        if(not await utilis.utils.validateName(self, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""))):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_NAME_FORMAT, -1, parseMode="html")
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_NAME_TEXT, 1)
            return False

        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 8, constants.SUCESS_CONFIRM_NAME, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

    async def confirm_birth(self, update, chat_id):
        error = False
        self.logger.error(constants.START, extra=dataUser.get(constants.EXTRA_PARAMS))
        try:

            if(not await utilis.utils.validate_Birt(self, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""))):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_BIRT_FORMAT, -1, parseMode="html")
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.ENTER_CONFIRM_BIRTH_TEXT, 2)
                return False

            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 9, constants.SUCESS_CONFIRM_BIRTH, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

    async def country(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:
            dat = self.arraysCites.countrys

            await self.sendesplegableButton(update,
                                            dat, 6, constants.SUCESS_COUNTRY, 3, 15, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            dat = self.arraysCites.countrys

            await self.sendesplegableButton(update,
                                            dat, 6, constants.SUCESS_COUNTRY, 3, 15, chat_id=chat_id)

    async def actions(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:
            dat = self.arraysCites.actions

            await self.sendesplegableButton(update,
                                            dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            dat = self.arraysCites.actions

            await self.sendesplegableButton(update,
                                            dat, 10, constants.SUCESS_CONFIRM_ACTIONS, 3, 15, chat_id=chat_id)

    async def plans(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(update,
                                            dat, 11, constants.SUCESS_CONFIRM_PLANS, 1, 1, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(update,
                                            dat, 11, constants.SUCESS_CONFIRM_PLANS, 1, 1, chat_id=chat_id)

    async def plansMenu(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:
            dat = self.arraysCites.plans

            await self.sendesplegableButton(update,
                                            dat, 11, constants.SUCESS_CONFIRM_MENU_PLANS, 1, 1, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            time.sleep(3)
            self.plansMenu(update, chat_id)

    async def payment_method(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        try:
            dat = self.arraysCites.payment_method

            await self.sendesplegableButton(update,
                                            dat, 12, constants.SUCESS_CONFIRM_PAYMENT_METHOD, 3, 10, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            self.logger.warn(
                constants.WARNING_USER_PAYMENT_FAIL_TEXT, extra=dataUser.get(constants.EXTRA_PARAMS))
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_PAYMENT_FAIL_TEXT, -1)

    async def confirm_payment(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5, chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            dat = self.arraysCites.confirm
            
            newSelect = dataUser.get(constants.NEWSELECT)

            await newSelect.select(update, 0, 0, 0)

            await self.sendesplegableButton(update,
                                            dat, 16, constants.SUCESS_CONFIRM_PAYMENT, 2, 5, chat_id=chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def readyUser(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        await self.sendMessageTelChatId(chat_id, update, constants.WARNING_MESSAGE_VERIFIED_TEXT.replace("{}", self.usernameAsiloBot, -1))

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def paymentReference(self, update, chat_id):
        error = False
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PAYMENT, False):
            await self.readyUser()

        if dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.REFERENCE_PAYMENT, False):
            await self.readyUser()

        else:
            try:
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 3)

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
            except NetworkError as networkError:
                error = True
                self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            except Exception as errors:
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))
                error = True

            if(error):
                await self.sendMessageTelChatId(chat_id, update, constants.USER_REFERENCE_PAYMENT_NOT_SAVE_TEXT)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_reference_payment(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        try:

            if(not await utilis.utils.validateReference(self, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""))):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_REFERENCE_FORMAT, -1, parseMode="html")
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 3)
                return False

            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 13, constants.SUCESS_REFERENCE_PAYMENT, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except NetworkError as networkError:
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            error = True

        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            error = True

        if(error):
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_email(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        try:

            if(not await utilis.utils.validate_email(self, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""))):
                await self.sendMessageTelChatId(update.message.chat_id, update, constants.WARNING_MAIL_FORMAT, -1, parseMode="html")
                await self.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_EMAIL_TEXT, 20,False)

                return False

            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 20, constants.SUCESS_CONFIRM_EMAIL, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except NetworkError as networkError:
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            error = True

        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            error = True

        if(error):
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))
        
    async def cancelProcess(self, update, dataUser):
        chat_id = dataUser.get(constants.DATA_CHAT_ID)
        menuBot = menu(self.logger,self.dataUser,self.bot) 
        
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        try:
           dataUser.update({constants.ACTIONS_USER:-1})
           dataUser.update({constants.CHAT_DATA_PERFIL:constants.datDefault.copy()})
           
           await menuBot.clearMsgText()
           dataUser.update({constants.HIDDEN_MENU: True})
           await self.persistentBtns(update, True, chat_id)
           
           self.logger.info(self.data.get(chat_id), extra=dataUser.get(constants.EXTRA_PARAMS))
           
           
        except NetworkError as networkError:
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            error = True

        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            error = True

        if(error):
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_reference_Menu_payment(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        dat = self.arraysCites.confirm

        await self.sendesplegableButton(update,
                                        dat, 13, constants.SUCESS_REFERENCE_PAYMENT, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def setReferenceMenu(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        await self.sendMessageTelChatId(chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 15)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_username(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False
        code = constants.SUCESS_USER_REGISTER_USERNAME
        username = dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.OPTIONVALIDAT_TEXT, "")
        
        if not await utilis.utils.validate_username(self,username):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USERNAME_FORMAT, -1, parseMode="html")
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 4,False)
            return False

        if(dataUser.get(constants.ISLOGIN,self.isLogin)):
            dataUser.update({constants.ISLOGIN:True})
            code = constants.SUCESS_USER_LOGIN_USERNAME

        try:
            dat = self.arraysCites.confirm
            await self.sendesplegableButton(update,
                                            dat, 14, code, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            traceback.print_exc()

        if error:
            dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                {constants.OPTIONVALIDAT_TEXT: ""})
            dataUser.get(constants.CHAT_DATA_PERFIL,
                          constants.datDefault.copy()).update({constants.OPTIONVALIDATE: 4})

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def confirm_password(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        error = False

        if(not await utilis.utils.validate_password(self, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""))):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_PASSWORD_FORMAT, -1, parseMode="html")
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 5,False)
            return False

        code = constants.SUCESS_USER_REGISTER_PASSWORD

        if(dataUser.get(constants.ISLOGIN,self.isLogin)):
            dataUser.update({constants.ISLOGIN:True})
            code = constants.SUCESS_USER_LOGIN_PASSWORD

        try:
            dat = self.arraysCites.confirm

            await self.sendesplegableButton(update,
                                            dat, 15, code, 2, 1, dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, ""), chat_id=chat_id)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            await self.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 5,False)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def validateReference(self, update, chat_id):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        try:
            await self.sendMessageTelChatId(chat_id, update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT, -1)

        except TimedOut as timedOutError:
            error = True
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if error:
            await self.validateReference()

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def getDataUser(self,dataUser={},data={},chat_id=-1):
        if(chat_id != -1):
            if(len(data.get(chat_id,{})) > 0):
                return data.get(chat_id)
        
        if(dataUser.get(constants.DATA_CHAT_ID,-1)) != -1:
            datatemp = datatemps(dataUser.get(constants.LOGGER_USER),dataUser)
            searchResponse = await datatemp.get(dataUser.get(constants.DATA_CHAT_ID))
            print("LONGITUD:%s",str(len(searchResponse)))
            if(len(searchResponse) > 0):
                return searchResponse
            else:
                return dataUser
        else:
            return dataUser
        
    async def preparUserData(self,update: Update, context: ContextTypes.DEFAULT_TYPE,chat_id = -1):
        util = utils()
        dataUser = {}
        
        logger = await util.getlogger()
        dataUser.update({constants.LOGGER_USER:logger})
        
        validate_data = validate_user(self.bot,logger,dataUser)
        dataUser = await validate_data.valid_user_chat(update,chat_id)
        
        util.dataUser = dataUser
        
        await util.setUserTelegram(update)
        await util.setTokenUser()
        
        dataUser = util.dataUser
        
        logger.info(dataUser, extra=dataUser.get(constants.EXTRA_PARAMS))
        
        dataUser = await self.getDataUser(dataUser,self.data,dataUser.get(constants.DATA_CHAT_ID))
        
        return dataUser

        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        error = False
        chat_id = -1
        messageId = -1

        dataUser = await self.preparUserData(update,context,chat_id)
        logger = dataUser.get(constants.LOGGER_USER)
        
        logger.info(constants.START + ":" + inspect.stack()
                        [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        dataUser.update({constants.HIDDEN_MENU: True})
        
        menuBot = menu(logger,dataUser,self.bot)
        await menuBot.persistentBtns(update, True)

        user = "Anonimo"

        try:
            user = update.message.from_user
            self.user = user
            self.usernameTelegram = self.user.username
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))

        try:
            await update.message.reply_text(
                f"✋🏼 Hola {user['first_name']}, Saludos y bienvenido al bot de automatización web para la gestión de sistema de administración pública." + " \n\n NOTA: Este bot 🤖 no tiene nada que ver con el gobierno de España 🇪🇸  ni tampoco con algún ente publico, solo es un sistema realizado para la ayuda de todos, en las que su función nos trae Solicitar, verificar y Anular nuestra cita de asilo en el país de España de manera automática cada cierto tiempo."
            )
            #await update.message.reply_text(
            #    "Comandos: /signup para comenzar el proceso de registro o continuar en un proceso #no terminado."
            #)
        except TimedOut as timedOutError:
            error = True
            logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            error = True
            logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            error = True
            logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS))
            
        if(error):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_TIME_OUT, -1)

        logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        error = False
        chat_id = update.message.chat_id
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        try:
            """Displays info on how to use the bot."""
            await update.message.reply_text("Use /start to test this bot.")

        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=dataUser.get(constants.EXTRA_PARAMS))
            await self.help_command()
        except NetworkError as networkError:
            self.logger.error(networkError, extra=dataUser.get(constants.EXTRA_PARAMS))
            await self.help_command()
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            await self.help_command()

        if(error):
            await self.help_command(update, context)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        
        # updateReceiber = json.dumps(update.to_dict())
        # logger.info(updateReceiber, extra=dataUser.get(constants.EXTRA_PARAMS,constants.extra_params.copy()))

        query = update.callback_query

        chat_id = update.callback_query.message.chat.id
        
        util = utils()
        dataUser = await self.preparUserData(update,context,chat_id)
        logger = dataUser.get(constants.LOGGER_USER)
        chat_id = dataUser.get(constants.DATA_CHAT_ID)
        
        validate_data = validate_user(self.bot,logger,dataUser)
                
        if(self.data.get(chat_id) is None):
            await self.cancelProcess(update,chat_id=chat_id)
        
        logger.info("▶️ " + constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        logger.info("data in query:%s", query.data,
                         extra=dataUser.get(constants.EXTRA_PARAMS))
        
        

        json_object = {}
        try:
            try:
                json_object = json.loads(query.data)
            except Exception as errors:
                logger.warning(errors, extra=dataUser.get(constants.EXTRA_PARAMS))
                index, _actions = query.data.split("-")
                _index = int(index)
                _actions = int(_actions)
                json_object = {"action": _actions, "page": 0,
                               "text": "", "page": 0, "index": _index}

            logger.info(json_object, extra=dataUser.get(constants.EXTRA_PARAMS))

            # actions
            # 0:first
            # 1:after
            # 2:paginatorP
            # 3:paginationSelect

            text = json_object["text"]
            action = json_object["action"]
            newPage = json_object["page"]

            self.text_Loading = "🔤🔤🔤🔤🔤🔤🔤🔤"

            if(dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()) is None):
                dataUser.update(
                    constants.CHAT_DATA_PERFIL, constants.datDefault.copy())

            if json_object["action"] == constants.SUCESS_PROVINCE:
                error = False
                try:

                    _text = self.arraysCites.provinces[json_object["index"]]
                    _index = json_object["index"]
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.PROVINCIAGENERAL: _index})

                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_OFICINE:
                error = False
                try:

                    _text = self.arraysCites.oficines[json_object["index"]]
                    _index = json_object["index"]

                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.SEDE: _index})

                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_OFICINE_EXTRANJERA:
                error = False
                try:

                    _text = self.arraysCites.tramite_oficine_extrajera[json_object["index"]]
                    _index = json_object["index"]
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.TRAMITE_OFICINA: _index})
                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_TRAMITE_CUERPO_POLICIAL:
                error = False
                try:

                    _text = self.arraysCites.tramite_cuerpo_nacional_policial[json_object["index"]]
                    _index = json_object["index"]
                    # self.dat["tramite_cuperto_policial"] = _index
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.TRAMITE_CUERPO_POLICIAL: _index})

                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_TIPO_DOC:
                error = False
                try:
                    _text = self.arraysCites.tipo_doc[json_object["index"]]
                    _index = json_object["index"]
                    # self.dat["typeDoc"] = _index
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.TYPEDOC: _index})

                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_CONFIRM_DOCUMENT:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        # self.dat["doc"] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.DOC: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)
                        else:
                            await validate_data.validateFieldTextUser(update)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_CONFIRM_NAME:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        # self.dat["name"] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.NAME: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.OPTIONVALIDAT_TEXT: ""})
                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)
                        else:
                            await validate_data.validateFieldTextUser(update)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_CONFIRM_BIRTH:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        # self.dat["birth"] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.BIRTH: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)
                        else:
                            await validate_data.validateFieldTextUser(update)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_COUNTRY:
                error = False
                try:

                    _index = json_object["index"]
                    _text = self.arraysCites.countrys[json_object["index"]]
                    # self.dat["country"] = _index
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.COUNTRY: _index})
                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_USER_REGISTER_USERNAME:
                error = False
                try:
                    _index = json_object["index"]
                    _text = self.arraysCites.confirm[_index]
                    if _text == constants.YES:
                        # self.dat[constants.USERNAME] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update({constants.USERNAME: self.data.get(
                            chat_id).get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)
                        else:
                            await validate_data.validateFieldTextUser(update)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_USER_REGISTER_PASSWORD:
                error = False
                try:

                    _index = json_object["index"]
                    _text = self.arraysCites.confirm[_index]
                    if _text == constants.YES:
                        # self.dat[constants.PASSWORD] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update({constants.PASSWORD: self.data.get(
                            chat_id).get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)
                        else:
                            await validate_data.validateFieldTextUser(update)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_CONFIRM_PLANS:
                error = False
                try:

                    _text = self.arraysCites.plans[json_object["index"]]
                    _index = json_object["index"]

                    # self.dat["plans"] = _index
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.PLANS: _index})

                    if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                        await self.updatePerfil(update, chat_id)

                    dataUser.update(
                        {constants.HIDDEN_MENU: True})
                    await self.persistentBtns(update, True, chat_id)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_CONFIRM_PAYMENT_METHOD:
                error = False
                try:
                    _index = json_object.get("index")
                    _text = self.arraysCites.payment_method[_index]

                    if _text != "":
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.METHOD_PAYMENT: _index})

                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)

                        await self.persistentBtns(update, True, chat_id)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))
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
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.PAYMENT: _value})
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.OPTIONVALIDATE: 3})
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_REFERENCE_PAYMENT_FAIL_TEXT, False)
                    dataUser.update(
                        {constants.HIDDEN_MENU: True})
                    await self.persistentBtns(update, True, chat_id)

            elif json_object["action"] == constants.SUCESS_REFERENCE_PAYMENT:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        # dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.REFERENCE_PAYMENT,"") = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.REFERENCE_PAYMENT: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})

                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)

                        dataUser.update(
                            {constants.HIDDEN_MENU: True})
                        await self.persistentBtns(update, True, chat_id)
                    else:
                        await self.sendMessageTelChatId(chat_id, update, constants.USER_REFERENCE_PAYMENT_CANCELL, False)

                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.SUCESS_REFERENCE_MENU_PAYMENT:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        # dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.REFERENCE_PAYMENT,"") = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.REFERENCE_PAYMENT: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})

                        if(dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_UPDATE_PERFIL):
                            await self.updatePerfil(update, chat_id)

                        await self.sendMessageTelChatId(chat_id, update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT)
                    else:
                        await self.setReferenceMenu(update, chat_id)

                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await self.setReferenceMenu(update, chat_id)

            elif json_object["action"] == constants.SUCESS_USER_LOGIN_USERNAME or json_object["action"] == constants.SUCESS_USER_LOGIN_PASSWORD:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        if(json_object["action"] == constants.SUCESS_USER_LOGIN_USERNAME):
                            # self.dat[constants.USERNAME] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                            dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                                {constants.USERNAME: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})

                        if(json_object["action"] == constants.SUCESS_USER_LOGIN_PASSWORD):
                            # self.dat[constants.PASSWORD] = dataUser.get(constants.CHAT_DATA_PERFIL,constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")
                            dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                                {constants.PASSWORD: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        await self.validateLoginUser(update, chat_id)
                    else:
                        await self.validateLoginUser(update, chat_id)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await self.validateLoginUser(update, chat_id)

            elif json_object["action"] == constants.SUCESS_CONFIRM_EMAIL:
                error = False
                try:
                    _text = self.arraysCites.confirm[json_object["index"]]
                    if _text == constants.YES:
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                            {constants.EMAIL: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})
                        await validate_data.validateFieldTextUser(update)
                    else:
                        await validate_data.validateFieldTextUser(update)
                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)

            elif json_object["action"] == constants.FINISH_UPDATE:
                await self.clearUpdatePerfil(update, chat_id)

            elif json_object["action"] == constants.SELECT_INPUT_MODIFY_PERFIL:
                error = False
                try:
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.USERNAME: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT, "")})

                    result = self.arraysCites.data_perfil.get("data")
                    item = result[_index]
                    lbl = item.get("lbl")
                    code = item.get("code")
                    default = item.get("default")
                    array = item.get("array")
                    caseTitle = item.get("caseTitle")

                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {lbl: default})
                    # asyncio.create_task(my_async_function())

                    fieldOptional = [
                        constants.PLANS, constants.METHOD_PAYMENT, constants.REFERENCE_PAYMENT]

                    if lbl in fieldOptional:
                        optionalDat = [lbl, code, array, default, caseTitle]
                        await validate_data.validateFieldTextUser(update, optionalDat)
                    else:
                        await validate_data.validateFieldTextUser(update)

                except Exception as errors:
                    error = True
                    logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if error:
                    await validate_data.validateFieldTextUser(update)
            else:
                new_btns = ""
                newSelect = dataUser.get(constants.NEWSELECT)
                
                logger.info("Accione sin seleccion, acciones valida paginador o siguiente en un listado.",
                                  extra=dataUser.get(constants.EXTRA_PARAMS))
                
                await self.clearMsgText(True,update,chat_id)
                await query.answer()
                    
                if text == "first":
                    newSelect.page += 1
                    new_btns = await newSelect.select(update, 0, action, newSelect.page)

                if text == "after":
                    newSelect.page -= 1
                    new_btns = await newSelect.select(update, 0, action, newSelect.page)

                if text == "paginatorP" and action == 2:
                    self.page = json_object["page"]
                    action = 2
                    newSelect._paginatorActive = True
                    new_btns = await newSelect.select(update, 0, action, newSelect.page)
                else:
                    if text == "pageselect" and action == 3:
                        action = 3
                        # print(f"JSON PAGE:{json_object['page']}")
                        self.page = json_object["page"]
                        newSelect._paginatorActive = True
                        new_btns = await newSelect.select(update, 0, action, newPage)
                        
                if(new_btns != ""):
                    dataUser.get(constants.CHAT_MSG_USER,
                              []).append([chat_id, new_btns.message_id])
                        
                dataUser.update({constants.NEWSELECT:newSelect})
                
        except TimedOut as timedOutError:
            logger.error(str(timedOutError) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
        except NetworkError as networkError:
            logger.error(str(networkError) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
        except Exception as errors:
            logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            

        logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))


    async def handle_text(self, update, context):
        #chat_id = await self.valid_user_chat(update)
        chat_id=-1
        util = utils()
        dataUser = await self.preparUserData(update,context,chat_id)
        logger = dataUser.get(constants.LOGGER_USER)
        chat_id = dataUser.get(constants.DATA_CHAT_ID)
        
        logger.info("⌨️ " + constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        
        text = update.message.text
        messageId = update.message.message_id
            
        try:
            validateFormText = False
            
            if(chat_id is None):
                logger.error("Sin chat id.", extra=dataUser.get(constants.EXTRA_PARAMS))
                return

            dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                {constants.OPTIONVALIDAT_TEXT: text})
            validateFormText = True

            if(text == constants.ENTRAR or text == constants.CERRAR_SESION or text == constants.HIDDEN.replace("\u00fa", "ú") or text == constants.SHOW.replace("\u00fa", "ú") or text == constants.PLANS_TEX or text == constants.SET_MENU_REFERENCE_PAYMENT or text == constants.SET_MENU_METHOD_PAYMENT or text == constants.INFORMATION or text == constants.SIGNUP or text == constants.UPDATE_INFORMATION or dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDATE, -1) == 7 or dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDATE, -1) == 4 or dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDATE, -1) == 2 or text == constants.CANCELAR):
                     #await self.bot.delete_message(chat_id=chat_id, message_id=messageId)
                dataUser.get(constants.CHAT_MSG_USER,
                              []).append([chat_id, messageId])
                

            hidden_menu = dataUser.get(
                    constants.HIDDEN_MENU, False)

            msgsMenuShowAndHide = dataUser.get(
                    constants.DATA_MSGS_MENU_SHOW_AN_DHIDE, [])

            if(text == constants.ENTRAR):
                    dataUser.update({constants.OPTIONVALIDATE: 8})
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.USERNAME: ""})
                    dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                        {constants.PASSWORD: ""})
                    dataUser.update({constants.TOKEN_ASILO: ""})
                    dataUser.get(constants.EXTRA_PARAMS).update(
                        {constants.USERNAME_ASILO_BOT: ""})

            if(text == constants.CERRAR_SESION):
                    dataUser.update({constants.OPTIONVALIDATE: 9})

            if(text == constants.HIDDEN.replace("\u00fa", "ú") or text == constants.SHOW.replace("\u00fa", "ú")):

                    hidden_menu = dataUser.get(
                        constants.HIDDEN_MENU, False)

                    msgsMenuShowAndHide.append(hidden_menu)

                    dataUser.update(
                        {constants.DATA_MSGS_MENU_SHOW_AN_DHIDE: msgsMenuShowAndHide})

                    dataUser.update(
                        {constants.HIDDEN_MENU: not hidden_menu})

                    try:
                        await self.bot.delete_message(chat_id=chat_id, message_id=messageId)
                    except Exception:
                        print("")

            if(text == constants.PLANS_TEX):
                    dataUser.update({constants.OPTIONVALIDATE: 12})

            if(text == constants.SET_MENU_REFERENCE_PAYMENT):
                    dataUser.update({constants.OPTIONVALIDATE: 14})

            if(text == constants.SET_MENU_METHOD_PAYMENT):
                    dataUser.update({constants.OPTIONVALIDATE: 16})

            if(text == constants.INFORMATION):
                    dataUser.update({constants.OPTIONVALIDATE: 17})

            if(text == constants.SIGNUP):
                    dataUser.update({constants.OPTIONVALIDATE: 18})

            if(text == constants.UPDATE_INFORMATION):
                    dataUser.update({constants.OPTIONVALIDATE: 19})
                    
            if(text == constants.CANCELAR):
                    dataUser.update({constants.OPTIONVALIDATE: 21})
                    
            if validateFormText:
                    if dataUser.get(constants.OPTIONVALIDATE, -1) == 0:
                        await self.confirm_document(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 1:
                        await self.confirm_name(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 2:
                        await self.confirm_birth(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 3:
                        await self.confirm_reference_payment(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 4:
                        await self.confirm_username(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 5:
                        await self.confirm_password(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 6:
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update({constants.USERNAME: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")})
                        await self.validateLoginUser(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 7:
                        dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update({constants.PASSWORD: dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.OPTIONVALIDAT_TEXT,"")})

                        await self.validateLoginUser(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 8:
                        await self.LoginUser(update, context)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 9:
                        await self.clearUpdatePerfil(update,chat_id=chat_id)
                        await self.LogoutUser(update, context, chat_id=chat_id)
                        return True
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 12:
                        await self.plansMenu(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 13:
                        msg = await self.sendMessageTelChatId(chat_id, update, constants.USER_PLANS_SELECTMENU_TEXT)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 14:
                        await self.setReferenceMenu(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 15:
                        await self.confirm_reference_Menu_payment(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 16:
                        await self.payment_method(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 17:
                        await self.getPerfil(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 18:
                        await self.signup(update, context)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 19:
                        await self.listButtonsModifiedPerfil(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == constants.FINISH_UPDATE:
                        await self.clearUpdatePerfil(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 20:
                        await self.confirm_email(update, chat_id)
                    elif dataUser.get(constants.OPTIONVALIDATE, -1) == 21:
                        await self.cancelProcess(update, chat_id)
                    else:
                        await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_TEXT, add_clearList=True)
                        dataUser.update(
                            {constants.HIDDEN_MENU: True})
                        await self.persistentBtns(update, True, chat_id)
                        time.sleep(1)

        except TimedOut as timedOutError:
            logger.error(str(timedOutError) + str(traceback.print_exc()), extra=dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
        except NetworkError as networkError:
            logger.error(str(networkError) + str(traceback.print_exc()),
                              extra=dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            logger.error(str(errors) + str(traceback.print_exc()), extra=dataUser.get(constants.EXTRA_PARAMS))
        finally:
            logger.info("Text User:%s,optionValidate:%s,chat_id:%s,messageId:%s",
                               text, dataUser.get(constants.OPTIONVALIDATE, -1), chat_id, messageId, extra=dataUser.get(constants.EXTRA_PARAMS))
            logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))
            

    async def testtable(self, update, context):
        chat_id = update.message.chat_id
        #await self.clearMsgText(True, update, update.message.chat_id)
        dataUser.update({constants.CHAT_DATA_PERFIL:constants.datDefault.copy()})
        
    async def statusVar(self, update, context):
            chat_id = update.message.chat_id
            self.logger.info("* DATA:%s",self.data, extra=dataUser.get(constants.EXTRA_PARAMS))
            
    async def menu(self, update, context):
        update = update
        update = update

        chat_id = update.message.chat_id

        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))

        dataUser.update(
            {constants.HIDDEN_MENU: True})
        await self.persistentBtns(update, True, chat_id)

        self.logger.info(constants.END, extra=dataUser.get(constants.EXTRA_PARAMS))
        
    async def signup(self, update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=-1) -> None:
        dataUser = await self.preparUserData(update,context,chat_id)
        logger = dataUser.get(constants.LOGGER_USER)
        
        logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=dataUser.get(constants.EXTRA_PARAMS))
        
        newSignup = signup(logger,dataUser,self.bot)
        result = await newSignup.signup(update,context)
        
        datatemp = datatemps(logger,dataUser)
        datatemp.update()
        
        return result
        
    def main(self) -> None:
        error = False
        
        try:
            
            persistence = PicklePersistence(filepath="conversationbot")

            #application = Application.builder().token(self.token).build()
            application = Application.builder().token(self.token).persistence(persistence).build()

            application.add_handler(CommandHandler("start", self.start))

            application.add_handler(CommandHandler("signup", self.signup))

            application.add_handler(
                CommandHandler("testtable", self.testtable))

            application.add_handler(
                CommandHandler("login", self.LoginUser))

            application.add_handler(
                CommandHandler("logout", self.LogoutUser))

            application.add_handler(CommandHandler("menu", self.menu))
            application.add_handler(CommandHandler("statusVar", self.statusVar))

            application.add_handler(CallbackQueryHandler(self.button))

            application.add_handler(
                MessageHandler(filters.TEXT, self.handle_text))

            application.run_polling()
            
            
            
        except Exception as errors:
            error = True
            print(str(errors) + str(traceback.print_exc()))

        if(error):
            time.sleep(5)


if __name__ == "__main__":
    nest_asyncio.apply()
    citaAsilobot = citaAsilobot()
    citaAsilobot.main()
    
