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
from telegram.error import TimedOut
from telegram.error import NetworkError
from telegram.constants import ParseMode
import testListDesplegable
from menu import menu

class utilsMensajeTelegram():
    
    def __init__(self,logger,dataUser,bot):
        self.logger = logger
        self.dataUser = dataUser
        self.bot = bot
        
        
        print("Clase utilis")
        
        
    async def sendMessageTelChatId(self, chat_id, update, optionValidat_Text="", optionValidate=-1, add_clearList=True, parseMode=""):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))
        sucess = True
        error_str = ""
        msg = ""
        try:
            self.dataUser.update(
                {constants.OPTIONVALIDATE: optionValidate})

            self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).update(
                {constants.OPTIONVALIDAT_TEXT: optionValidat_Text})

            if(parseMode == "html"):
                msg = await self.bot.sendMessage(
                    chat_id=chat_id, text=optionValidat_Text, parse_mode=ParseMode.HTML
                )

            else:
                msg = await self.bot.send_message(chat_id=chat_id, text=optionValidat_Text)

            if(add_clearList):
                self.logger.info("✅ Agregando mensaje del chat: %s a pendiente por eliminar con message_id: %s y contiene el texto:%s",
                                 chat_id, msg.message_id, msg.text, extra=self.dataUser.get(constants.EXTRA_PARAMS))

                msgsUser = self.dataUser.get(
                    constants.CHAT_MSG_USER, [])
                msgsUser.append(
                    [chat_id, msg.message_id])

                self.dataUser.update(
                    {constants.CHAT_MSG_USER: msgsUser})

            self.chatSend = ""
        except TimedOut as timedOutError:
            self.logger.error(timedOutError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
            error_str = str(timedOutError)
            sucess = False
        except NetworkError as networkError:
            self.logger.error(networkError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
            error_str = str(networkError)
            sucess = False
        except Exception as errors:
            self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()))
            error_str = str(errors)
            sucess = False

        self.logger.info("Message:%s,send sucess:%s",
                         optionValidat_Text, sucess, extra=self.dataUser.get(constants.EXTRA_PARAMS))

        if(not sucess and error_str.find("not found") == -1):
            await self.sendMessageTelChatId(update, optionValidat_Text, optionValidate, add_clearList)

        self.logger.info(constants.END, extra=self.dataUser.get(constants.EXTRA_PARAMS))    
        
        
    async def sendesplegableButton(self, update, dat=[], case=-1, sucess_code=-1, _paginatorLisColumm=2, _paginatorGeneral=10, _add_title_text="", actions=0, page=-1, chat_id=None, delete=True):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))
        
        chat_id = self.dataUser.get(constants.DATA_CHAT_ID)
        menuBot = menu(self.logger,self.dataUser,self.bot)
        
        await menuBot.clearMsgText()

        self.logger.info("Desplegando menu con codigo:%s", str(sucess_code), extra=self.dataUser.get(constants.EXTRA_PARAMS))

        if(chat_id is None):
            self.logger.error("chat_id is None.", extra=self.dataUser.get(constants.EXTRA_PARAMS))
            return
        error = False

        newSelect = testListDesplegable.testList(
            constants.token_acilotBot,
            update,
            dat,
            case,
            sucess_code,
            _paginatorLisColumm,
            _paginatorGeneral,
            _add_title_text,
            logger=self.logger,
            extra_params=self.dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy()),
            chat_id=chat_id
        )

        msgBtns = await newSelect.select(update, 0, actions, page)
        
        self.dataUser.update({constants.NEWSELECT: newSelect})

        chatid = msgBtns.chat.id
        messageId = msgBtns.message_id

        if(delete):
            await menuBot.clearMsgText()
            self.logger.info("Agregando boton %s para futura eliminacion 👍.", case, extra=self.dataUser.get(constants.EXTRA_PARAMS))
            
            msgs = self.dataUser.get(constants.CHAT_MSG_USER, [])
            msgs.append([chatid, messageId])

            self.dataUser.update({constants.CHAT_MSG_USER: msgs})
            
            self.logger.info(self.dataUser.get(
                constants.CHAT_MSG_USER, []), extra=self.dataUser.get(constants.EXTRA_PARAMS))
            
            self.dataUser.update({constants.CHAT_MSG_USER: msgs})
            
        if(error):
            await self.sendesplegableButton(update=update, dat=dat, case=case, sucess_code=sucess_code, _paginatorLisColumm=_paginatorLisColumm, _paginatorGeneral=_paginatorGeneral, _add_title_text=_add_title_text, chat_id=chat_id)

        self.logger.info(constants.END + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))

        return msgBtns