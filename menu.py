import constants
import inspect
import json
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
from telegram import __version__ as TG_VER
from typing import Dict
import json
import constants
from telegram.error import TimedOut
from telegram.error import NetworkError
import time
import time
import inspect
from utilis import utils
from datatemps import datatemps

class menu:
    def __init__(self, logger, dataUser,bot):
        a = 1
        self.logger = logger
        self.dataUser =dataUser
        self.bot = bot

    async def clearMsgText(self):

        chat_id = self.dataUser.get(constants.DATA_CHAT_ID)
        
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))
        error = False

        chat_msgs = self.dataUser.get(constants.CHAT_MSG_USER, [])
        arryTemp = chat_msgs
        delete_sucess = []

        self.logger.info("✉️ Mensajes del usuario:%s, total:%s",
                         str(chat_msgs), str(len(chat_msgs)), extra=self.dataUser.get(constants.EXTRA_PARAMS))

        error = False
        error_str = ""

        if len(arryTemp) > 0:
            count = 0
            try:
                for x in arryTemp:

                    chat_ids = chat_id
                    message_id = x[1]
                    if (chat_ids != "" and message_id != ""):
                        self.logger.info("🧹 Eliminando msg id:%s",
                                         arryTemp[count], extra=self.dataUser.get(constants.EXTRA_PARAMS))
                        deleteMsg = await self.bot.delete_message(chat_id=chat_ids, message_id=message_id)

                        time.sleep(1)
                        if (deleteMsg):
                            self.logger.info("🗑 Mensaje Eliminado: msg id: %s,resp:%s", arryTemp[count], deleteMsg, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                            delete_sucess.append(message_id)

                        else:
                            self.logger.info(
                                " 🗑❌ El mensaje no se logro eliminar: msg id: %s,resp:%s", arryTemp[count], deleteMsg, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                    else:
                        del chat_msgs[count]
                        self.logger.info("🩹 Mensaje vacio o invalido:%s",
                                         chat_msgs[count], extra=self.dataUser.get(constants.EXTRA_PARAMS))

                    count += 1

                new_arrayMsgs = []
                arr_orden = []

                for x in arryTemp:
                    arr_orden.append(x[1])

                for item in arr_orden:
                    if (delete_sucess.index(item) == -1):
                        self.logger.info("🩹 Mensaje pendiente por eliminar:%s",
                                         chat_msgs[count], extra=self.dataUser.get(constants.EXTRA_PARAMS))
                        new_arrayMsgs.append([chat_id, item])

                self.dataUser.update(
                    {constants.CHAT_MSG_USER: new_arrayMsgs})

                if (len(new_arrayMsgs) > 0):
                    self.logger.info("😲 Todavia quedan mensajes por eliminar:%s",
                                     len(new_arrayMsgs), extra=self.dataUser.get(constants.EXTRA_PARAMS))
                    new_arrayMsgs.append([chat_id, item])
                else:
                    self.logger.info("🧹🧹 Todos los mensajes fueron eliminados.", extra=self.dataUser.get(constants.EXTRA_PARAMS))
                    new_arrayMsgs.append([chat_id, item])

            except TimedOut as timedOutError:
                error = True
                self.logger.error(timedOutError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                error_str = timedOutError
            except NetworkError as networkError:
                self.logger.info(networkError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                if (str(networkError).find("not found") != -1):
                    self.logger.warning(networkError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                    del chat_msgs[count]

                else:
                    error = True
                    self.logger.error(networkError, extra=self.dataUser.get(constants.EXTRA_PARAMS))

                error_str = networkError

            except Exception as errors:
                error_str = errors
                self.logger.info(errors, constants.extra_params.copy())
                if (str(errors).find("Message to delete not found") != -1):
                    self.logger.warning(errors, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                else:
                    error = True
                    self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.dataUser.get(
                        constants.EXTRA_PARAMS, constants.extra_params.copy()))

            if (error):
                time.sleep(1)

        count = + 1
        self.logger.info(constants.END, extra=self.dataUser.get(constants.EXTRA_PARAMS))

    async def persistentBtns(self, update, updates=False):
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))

        error = False
        chat_id = self.dataUser.get(constants.DATA_CHAT_ID)

        if (chat_id == -1 or chat_id == None):
            self.logger.warning('⚠️ Sin chat id', extra=self.dataUser.get(constants.EXTRA_PARAMS))
            return False

        hidden_menu = self.dataUser.get(constants.HIDDEN_MENU, False)
        menuDat = self.dataUser.get(constants.MENU_DAT, [])
        msgsMenuShowAndHide = self.dataUser.get(
            constants.DATA_MSGS_MENU_SHOW_AN_DHIDE, [])

        self.logger.info("📘 msgsMenuShowAndHide:%s,📘 hidden_menu:%s,📘 Total items en menuDat:%s",
                         msgsMenuShowAndHide, hidden_menu, len(menuDat), extra=self.dataUser.get(constants.EXTRA_PARAMS))

        if (msgsMenuShowAndHide is None or hidden_menu is None or menuDat is None):
            self.logger.error("Error not key",extra=self.dataUser.get(constants.EXTRA_PARAMS))
            return False

        try:
            if (len(menuDat) > 0 and not updates):
                self.logger.info(
                    "No se requiere actualizar el menu.", extra=self.dataUser.get(constants.EXTRA_PARAMS))
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
            cancelProcess = InlineKeyboardButton(
                constants.CANCELAR, callback_data='/cancelProcess')

            update_information = InlineKeyboardButton(
                constants.UPDATE_INFORMATION, callback_data='/updateInformation')

            self.dataUser.update(
                {constants.DATA_MSGS_MENU_SHOW_AN_DHIDE: []})

            if (len(menuDat) > 10000):

                menu = menuDat[0]

                self.logger.info(menu, extra=self.dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))

                chat_id = menu.chat.id
                message_id = menu.message_id

                self.logger.info("❌ Quitando menu con message_id:%s en chat:%s",
                                 message_id, chat_id, extra=self.dataUser.get(constants.EXTRA_PARAMS))

                self.dataUser.update({constants.MENU_DAT: []})
                menuDat = []

            if (not hidden_menu):
                self.logger.info("Entrando, ya que hidden_menu es false",
                                 extra=self.dataUser.get(constants.EXTRA_PARAMS))
                arrBtnsPersistent = []
                arrBtnsPersistent.append([show])

                reply_markup = ReplyKeyboardMarkup(
                    arrBtnsPersistent, resize_keyboard=True, one_time_keyboard=False)

                menu = await self.bot.send_message(chat_id=chat_id, text="...", reply_markup=reply_markup)

                menuJson = json.dumps(menu.to_dict())

                self.logger.info(menuJson, extra=self.dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))

                if (menuJson.get("message_id", -1) != -1):
                    await self.bot.delete_message(menuJson.get("message_id", -1))
                    self.dataUser.get(constants.CHAT_MSG_USER,
                                 []).append([chat_id, menu.message_id])

                    self.dataUser.update(
                        {constants.MENU_DAT: [menu, update]})

                self.logger.info("💬 Agregando menu en chat:%s",
                                 menu.chat.id, extra=self.dataUser.get(constants.EXTRA_PARAMS))

            else:
                if (self.dataUser.get(constants.TOKEN_ASILO, "") != ""):
                    if (not self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PAYMENT, False) and not self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.SUCESS, 0)):

                        if (self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PLANS, -1) == -1 or self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.REFERENCE_PAYMENT, "") == ""):
                            self.logger.info(
                                constants.SHOW_MENU_NOT_PAYMENT_TEXT, extra=self.dataUser.get(constants.EXTRA_PARAMS))

                            arrBtnsPersistent.append(
                                [update_information, logout])

                        else:
                            if (self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.PLANS, -1) != -1 and self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.REFERENCE_PAYMENT, "") != "" and not self.dataUser.get(constants.CHAT_DATA_PERFIL, constants.datDefault.copy()).get(constants.SUCESS, 0)):
                                self.logger.info(
                                    constants.SHOW_MENU_NOT_PAYMENT_TEXT, extra=self.dataUser.get(constants.EXTRA_PARAMS))
                                await self.sendMessageTelChatId(chat_id, update, constants.VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT, -1)
                                arrBtnsPersistent.append(
                                    [update_information, logout])

                else:
                    if (self.dataUser.get(constants.ACTIONS_USER, -1) == 0 or self.dataUser.get(constants.ACTIONS_USER, -1) == 1):
                        arrBtnsPersistent = [[cancelProcess]]
                    else:
                        arrBtnsPersistent.append([signup, login])

                self.logger.info("💬 Agregando menu en chat..",
                                 extra=self.dataUser.get(constants.EXTRA_PARAMS))

                reply_markup = ReplyKeyboardMarkup(
                    arrBtnsPersistent, resize_keyboard=True, one_time_keyboard=False)
                # reply_markup = ReplyKeyboardRemove()

                receiber = ""
                if (len(menuDat) > 0):
                    updateOld = menuDat[1]
                    message_id = -1

                    if updateOld.message and updateOld.message.message_id:
                        message_id = updateOld.message.message_id
                        await updateOld.message.reply_text(
                            "..", reply_markup=reply_markup)

                    if updateOld.callback_query and updateOld.callback_query.message.message_id:
                        message_id = updateOld.callback_query.message.message_id
                        await updateOld.callback_query.message.reply_text(
                            "\.\.\.", reply_markup=reply_markup, parse_mode="MarkdownV2"
                        )

                    if (message_id != -1):
                        self.logger.info("Editanto messageid:%s", message_id, extra=self.dataUser.get(
                            constants.EXTRA_PARAMS, constants.datDefault.copy()))

                        # receiber = await self.bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=reply_markup)
                    else:
                        self.logger.info("ERROR AL ACTUALIZAR EL MENU", extra=self.dataUser.get(
                            constants.EXTRA_PARAMS, constants.datDefault.copy()))

                else:
                    receiber = await self.bot.send_message(chat_id=chat_id, text="..", reply_markup=reply_markup)

                self.dataUser.update({constants.MENU_DAT: [receiber, update]})

        except TimedOut as timedOutError:
            if (str(timedOutError).find("not found") != -1):
                self.logger.warning(timedOutError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
            else:
                error = True
                self.logger.error(timedOutError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
        except NetworkError as networkError:
            if (str(networkError).find("not found") != -1):
                self.logger.warning(networkError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
            else:
                error = True
                self.logger.error(networkError, extra=self.dataUser.get(constants.EXTRA_PARAMS))
        except Exception as errors:
            if (str(errors).find("not found") != -1):
                self.logger.warning(errors, extra=self.dataUser.get(constants.EXTRA_PARAMS))
            else:
                error = True
                self.logger.error(str(errors) + str(traceback.print_exc()), extra=self.dataUser.get(
                    constants.EXTRA_PARAMS, constants.extra_params.copy()))

        if (error):
            time.sleep(3)

        self.logger.info(constants.END, extra=self.dataUser.get(constants.EXTRA_PARAMS))
