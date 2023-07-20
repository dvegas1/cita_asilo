
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

import constants
import inspect
import json
from utilsMensajeTelegram import utilsMensajeTelegram
import datArray_cites

class validate_user:
    def __init__(self,bot,logger, dataUser={}):
        self.dataUser = dataUser
        self.logger = logger
        self.bot = bot
        self.arraysCites = datArray_cites.array_cites()

    async def valid_user_chat(self, update, chat_id=-1):
        chatId = -1

        if len(self.dataUser) > 0 and chat_id != -1:
            if (self.dataUser.get(constants.DATA_CHAT_ID, -1) != -1):
                if (chat_id == self.dataUser.get(constants.DATA_CHAT_ID)):
                    return self.dataUser

        if (update.message and update.message.chat.id):
            chatId = update.message.chat_id

        if update.callback_query and update.callback_query.message.chat.id:
            chatId = update.callback_query.message.chat.id

        if (chatId != -1):
            print("ACTUALIZANDO:%s", str(chatId))
            if (len(self.dataUser.get(constants.CHAT_DATA_PERFIL, {})) == 0):
                self.dataUser.update(
                    {constants.CHAT_DATA_PERFIL: constants.datDefault.copy()})

            self.dataUser.update({constants.HIDDEN_MENU: True})
            self.dataUser.update({constants.DATA_CHAT_ID: chatId})

            extra_params = self.dataUser.get(
                constants.EXTRA_PARAMS, constants.extra_params.copy())
            extra_params.update({constants.DATA_CHAT_ID: chatId})
            self.dataUser.update({constants.EXTRA_PARAMS: extra_params})

        return self.dataUser

   
    async def validateFieldTextUser(self, update, fieldOptional=[]):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))
        chat_id = self.dataUser.get(constants.DATA_CHAT_ID,-1)
        
        if (chat_id == -1):
            self.logger.error("Error en parametro chat_id",
                              extra=self.dataUser.get(constants.EXTRA_PARAMS))
            return False

        error = False
        
        validate_data = utilsMensajeTelegram(self.logger,self.dataUser,self.bot)

        if (len(fieldOptional) > 0):
            if (fieldOptional[0] == constants.REFERENCE_PAYMENT):
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_REFERENCE_PAYMENT_TEXT, 3, False)
            else:
                if self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(fieldOptional[0], -1) == -1:

                    dat = fieldOptional[2]
                    await validate_data.sendesplegableButton(update,
                                                    dat, fieldOptional[4], fieldOptional[1], 1, 10, chat_id=chat_id)
        else:

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.PROVINCIAGENERAL, -1) == -1:
                dat = self.arraysCites.provinces
                await validate_data.sendesplegableButton(update,
                                                dat, 1, constants.SUCESS_PROVINCE, 3, 10, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.SEDE, -1) == -1:
                dat = self.arraysCites.oficines
                await validate_data.sendesplegableButton(update,
                                                dat, 2, constants.SUCESS_OFICINE, 1, 8, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.TRAMITE_OFICINA, -1) == -1:
                dat = self.arraysCites.tramite_oficine_extrajera
                await validate_data.sendesplegableButton(update,
                                                dat, 3, constants.SUCESS_OFICINE_EXTRANJERA, 1, 8, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.TRAMITE_CUERPO_POLICIAL, -1) == -1:
                dat = self.arraysCites.tramite_cuerpo_nacional_policial
                await validate_data.sendesplegableButton(update,
                                                dat, 4, constants.SUCESS_TRAMITE_CUERPO_POLICIAL, 1, 8, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.TYPEDOC, -1) == -1:
                dat = self.arraysCites.tipo_doc
                await validate_data.sendesplegableButton(update,
                                                dat, 5, constants.SUCESS_TIPO_DOC, 3, 1, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.DOC, '') == "":
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_DOCUMENT_TEXT, 0, False)
                await self.clearMsgText(True, update, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.NAME, '') == "":
                self.dataUser.get(constants.CHAT_DATA_PERFIL).update(
                    {constants.OPTIONVALIDATE: 1})
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_NAME_TEXT, 1, False)
                await self.clearMsgText(True, update, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.BIRTH, '') == '':
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_BIRTH_TEXT, 2, False)
                await self.clearMsgText(True, update, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.COUNTRY, -1) == -1:
                self.dataUser.get(constants.CHAT_DATA_PERFIL).update(
                    {constants.OPTIONVALIDATE: -1})
                dat = self.arraysCites.countrys
                await validate_data.sendesplegableButton(update, dat, 6, constants.SUCESS_COUNTRY, 3, 15, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.EMAIL, '') == "":
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_CONFIRM_EMAIL_TEXT, 20, False)
                await self.clearMsgText(True, update, chat_id=chat_id)
                return False

        if (self.dataUser.get(constants.ACTIONS_USER, -1) != constants.ACTION_USER_BOT_UPDATE_PERFIL):
            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.USERNAME, '') == "":
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_USERNAME_TEXT, 4, False)
                await self.clearMsgText(True, update, chat_id=chat_id)
                return False

            if self.dataUser.get(constants.CHAT_DATA_PERFIL).get(constants.PASSWORD, '') == "":
                await validate_data.sendMessageTelChatId(chat_id, update, constants.ENTER_PASSWORD_TEXT, 5, False)
                await self.clearMsgText(True, update, chat_id=chat_id)
                return False

        if (self.dataUser.get(constants.ACTIONS_USER, -1) == constants.ACTION_USER_BOT_SIGNUP):
            await self.registerUser(update, chat_id)

        if (self.dataUser.get(constants.TOKEN_ASILO, "") == ""):
            return False

        if error:
            await self.validateFieldTextUser(update)

        self.logger.info(constants.END, extra=self.dataUser.get(
            chat_id).get(constants.EXTRA_PARAMS))
        return True