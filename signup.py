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
from validate_user import validate_user
from menu import menu

class signup:
    def __init__(self,logger,dataUser,bot):
        self.logger = logger
        self.dataUser = dataUser
        self.bot = bot
        
    async def signup(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.logger.info(constants.START + ":" + inspect.stack()
                         [1][3], extra=self.dataUser.get(constants.EXTRA_PARAMS))        

        self.logger.info(self.dataUser.get(constants.CHAT_DATA_PERFIL),extra=self.dataUser.get(constants.EXTRA_PARAMS))
        
        await update.message.reply_text(constants.STAR_SIGNUP_USER_MSG_TEXT)
        
        self.dataUser.update({constants.ISLOGIN:False})
        
        if(self.dataUser.get(constants.TOKEN_ASILO, "")):
            await self.sendMessageTelChatId(chat_id, update, constants.WARNING_USER_ALREADY_LOGIN.replace("{username}", self.dataUser.get(constants.EXTRA_PARAMS).get(constants.USERNAME_ASILO_BOT), "--"))
            return

        chat_id = self.dataUser.get(constants.DATA_CHAT_ID)
               
        self.dataUser.update(
            {constants.ACTIONS_USER: constants.ACTION_USER_BOT_SIGNUP})
        
        menuBot = menu(self.logger,self.dataUser,self.bot)
        await menuBot.persistentBtns(update, True)
        
        validate_data = validate_user(self.bot,self.logger,self.dataUser)
        
        #await validate_data.validateFieldTextUser(update)
        
        rerult = await validate_data.validateFieldTextUser(update)
        
        self.logger.info("Result:%s",str(rerult), extra=self.dataUser.get(constants.EXTRA_PARAMS))
        
        self.logger.info(constants.END, extra=self.dataUser.get(constants.EXTRA_PARAMS))
