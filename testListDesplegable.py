#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Feb  8 15:30:55 2023

@author: PC
"""
import nest_asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from itertools import zip_longest
import telegram
import json
import constants
import utilis
import unicodedata
import base64
import logging


class testList:
    application = ""
    token = "5940401924:AAHUZEP6BtTOWPk2Zvy5uQOatI8b8JySVu8"
    _message_id = []
    update, context, application, dats, dat = range(5)
    page = 0
    pageLast = 0
    _init_ = 0
    _fn_ = 0
    _chats_btn = []
    _paginatorActive = False
    case = "S/C"
    sucess_code = ""
    _paginatorLisColumm = 3
    _paginatorGeneral = 20
    _reply_text = []
    _add_title_text = ""
    extra_params={"tokeUser": "S/T"}

    # 0:COYNTRY
    # 1:PROVINCE
    # 2:OFICINE

    def __init__(
        self,
        token,
        update,
        context,
        dat,
        case,
        sucess_code,
        paginatorLisColumm=_paginatorLisColumm,
        paginatorGeneral=_paginatorGeneral,
        add_title_text="",
        logger=None,
        extra_params=None
    ):
        self.token = token
        self.update = update
        self.context = context
        self.dat = dat
        self.case = case
        self.sucess_code = sucess_code
        self._paginatorLisColumm = paginatorLisColumm
        self._paginatorGeneral = paginatorGeneral
        self._add_title_text = add_title_text
        self.logger = logger
        self.extra_params = extra_params

    async def group_by_3(self, lst, num):
        return [list(g) for g in zip(*[iter(lst)] * num)]

    async def group_elements(self, n, iterable, padvalue="x"):
        return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)

    def final_list(self, test_list, x):
        return [test_list[i : i + x] for i in range(0, len(test_list), x)]

    async def select(self, default=0, actions=0, page=-1):
        self.logger.info("Inicio.", extra=self.extra_params)
        if page != -1:
            self.page = page

        keyboard2 = []

        tempPage = self.page + 1

        # print(f"self.dat:{self.dat}")
        n = 0
        for option in self.dat:
            _temp = option
            while len(_temp.encode("utf-8")) > 60:
                # print(f"LOGINTUD EXCEDIDA:{option}::::::::::{len(_temp.encode('utf-8'))}")
                # print(f"Cadena original:{_temp}")
                _total = len(_temp.encode("utf-8")) - 60
                _temp = _temp[:-_total]
            # self.dat[n] = _temp
            # print(f"Cadena modificada:{_temp}")
            # print(f"LOGINTUD:{len(_temp.encode('utf-8'))}")
            # print("_________________")

            _actions = str(n) + "-" + str(self.sucess_code)

            # if len(_actions.encode("utf-8")) > 64:
            #     print(
            #         f"**************************************************************************************pendiente aqui:{len(_actions.encode('utf-8'))})"
            #     )

            keyboard2.append(InlineKeyboardButton(_temp, callback_data=_actions))
            n += 1

        # print(f"keyboard2:{keyboard2}")

        output = self.final_list(keyboard2, self._paginatorLisColumm)
        self.dats = self.final_list(output, self._paginatorGeneral)

        # print(f"self.dats:{self.dats}")

        nextButton = []

        _callbackTo_after = json.dumps({"action": actions, "page": self.page, "text": "after"})
        _callbackTo_first = json.dumps({"action": actions, "page": self.page, "text": "first"})
        _callbackTo_paginatorP = json.dumps({"action": 2, "page": self.page, "text": "paginatorP"})

        if tempPage <= len(self.dats) and (tempPage > 1) and (len(self.dats) > 1):
            nextButton.append(InlineKeyboardButton("⬅️", callback_data=_callbackTo_after))

        if len(self.dats) > 1:
            nextButton.append(
                InlineKeyboardButton(
                    str(tempPage) + "-" + str(len(self.dats)), callback_data=_callbackTo_paginatorP
                )
            )

        if self._paginatorActive:
            n = 0
            for option in self.dats:
                dat = json.dumps({"action": 3, "page": n, "text": "pageselect"})
                nextButton.append(InlineKeyboardButton(str(n + 1), callback_data=dat))
                n += 1

        if tempPage < len(self.dats):
            nextButton.append(InlineKeyboardButton("➡️", callback_data=_callbackTo_first))

        # print(f"dats:{self.dats}")

        self.dats[self.page].append(nextButton)

        # print(f"page:{self.page}")
        # print(f"nextButton:{nextButton}")
        # print(f"Longitud:{len(self.dats)}")

        marku_countrys = InlineKeyboardMarkup(self.dats[self.page])

        # print(f"marku_countrys:{marku_countrys}")

        _title_list = ""

        if self.case == 1:
            _title_list = constants.SUCESS_PROVINCE_TEXT
        elif self.case == 2:
            _title_list = constants.SUCESS_OFICINE_TEXT
        elif self.case == 3:
            _title_list = constants.SUCESS_OFICINE_EXTRANJERA_TEXT
        elif self.case == 4:
            _title_list = constants.SUCESS_TRAMITE_CUERPO_POLICIAL_TEXT
        elif self.case == 5:
            _title_list = constants.SUCESS_TIPO_DOC_TEXT
        elif self.case == 6:
            _title_list = constants.SUCESS_COUNTRY_TEXT
        elif self.case == 7:
            _title_list = constants.SUCESS_CONFIRM_DOCUMENT_CONFIRM + self._add_title_text
        elif self.case == 8:
            _title_list = constants.SUCESS_CONFIRM_NAME_CONFIRM + self._add_title_text
        elif self.case == 9:
            _title_list = constants.SUCESS_CONFIRM_BIRTH_CONFIRM + self._add_title_text
        elif self.case == 10:
            _title_list = constants.SUCESS_CONFIRM_ACTIONS_TEXT
        elif self.case == 11:
            _title_list = constants.SUCESS_CONFIRM_PLANS_TEXT
        elif self.case == 12:
            _title_list = constants.SUCESS_CONFIRM_PAYMENT_METHOD_TEXT
        elif self.case == 13:
            _title_list = constants.SUCESS_REFERENCE_PAYMENT_CONFIRM + self._add_title_text
        elif self.case == 14:
            _title_list = constants.SUCESS_USERNAME_CONFIRM + self._add_title_text
        elif self.case == 15:
            _title_list = constants.SUCESS_PASSWORD_CONFIRM + self._add_title_text
        elif self.case == 16:
           _title_list = constants.SUCESS_CONFIRM_PAYMENT_TEXT
        else:
            _title_list = "Seleccione:"

        self._reply_text.append(
            await self.update.message.reply_text(
                _title_list, reply_markup=marku_countrys, parse_mode="MarkdownV2"
            )
        )

        self.logger.info("Fin.", extra=self.extra_params)