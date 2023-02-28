# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:14:10 2023

@author: PC
"""
END="Fin."
START="Inicio."

ERROR_RUN_MAIN_SECONDS =5
ERROR_RUN_MAIN_FAILE="No se logro iniciar cita_asilo, se intentara luego de: " + str(ERROR_RUN_MAIN_SECONDS) + " Segundos."

SUCESS_COUNTRY = 100
SUCESS_COUNTRY_TEXT = "Seleccione su país de nacionalidad:"


SUCESS_PROVINCE = 101
SUCESS_PROVINCE_TEXT = "Seleccione una Provincia:"


SUCESS_OFICINE = 102
SUCESS_OFICINE_TEXT = "Seleccione una Oficina:"

SUCESS_OFICINE_EXTRANJERA = 103
SUCESS_OFICINE_EXTRANJERA_TEXT = "Seleccione una Oficina Extranjera:"

SUCESS_TRAMITE_CUERPO_POLICIAL = 104
SUCESS_TRAMITE_CUERPO_POLICIAL_TEXT = "Seleccione una Oficina para Tramite Cuerpo Policial:"


SUCESS_TIPO_DOC = 105
SUCESS_TIPO_DOC_TEXT = "Seleccione un Tipo de documento:"


SUCESS_CONFIRM_DOCUMENT = 106
SUCESS_CONFIRM_DOCUMENT_TEXT = "Ingrese su Documento de Identidad:"
SUCESS_CONFIRM_DOCUMENT_CONFIRM = "Confirme su Documento de Identidad:"


SUCESS_CONFIRM_NAME = 107
SUCESS_CONFIRM_NAME_TEXT = "Ingrese su Nombre y Apellido:"
SUCESS_CONFIRM_NAME_CONFIRM = "Confirme su Nombre y Apellido:"

SUCESS_CONFIRM_BIRTH = 108
SUCESS_CONFIRM_BIRTH_TEXT = "Ingrese su Año de Nacimiento:"
SUCESS_CONFIRM_BIRTH_CONFIRM = "Confirme su Año de Nacimiento:"


SUCESS_CONFIRM_ACTIONS = 109
SUCESS_CONFIRM_ACTIONS_TEXT = "Seleccione una acción:"


SUCESS_CONFIRM_PLANS = 110
SUCESS_CONFIRM_PLANS_TEXT = "Seleccione una Plan:"



SUCESS_CONFIRM_PAYMENT_METHOD = 111
SUCESS_CONFIRM_PAYMENT_METHOD_TEXT = "Confirme método de pago:"

SUCESS_REFERENCE_PAYMENT = 112
SUCESS_REFERENCE_PAYMENT_TEXT = "Ingrese el Nro de referencia:"
SUCESS_REFERENCE_PAYMENT_CONFIRM = "Confirma Nro de referencia:"
SUCESS_REFERENCE_PAYMENT_WAITING = "Validando referencia este proceso puede del pago tardar de 1 a 2 horas, luego de esto se le hará llegar una notificación con las Horas/Minutos en la que se realizara el proceso"

SUCESS_USER_REGISTER_USERNAME = 113
SUCESS_USERNAME_TEXT = "Ingrese un nombre de usuario:"
SUCESS_USERNAME_CONFIRM = "Confirme un nombre de usuario:"


SUCESS_USER_REGISTER_PASSWORD = 114
SUCESS_PASSWORD_TEXT = "Ingrese una contraseña:"
SUCESS_PASSWORD_CONFIRM = "Confirme su contraseña:"

SUCESS_CONFIRM_PAYMENT = 115
SUCESS_CONFIRM_PAYMENT_TEXT = "Confirme pago realizado"


SUCESS_USER_REGISTER_PROCESS = "Se esta realizando el registro de su usuario 🔑"
SUCESS_USER_REGISTER_SUCESS = "Registro realizado con éxito 👏🏼"
SUCESS_USER_LOGOUT_SUCESS = "Cierre de sesión realizado con éxito 🔐"
WARNING_USER_EMAIL_ALREADY_EXISTS = "El nombre de usuario ya existe"
WARNING_USER_GENERAL = "No se logro registrar el usuario, por favor intente de nuevo"


WARNING_USER = "🤔 No conozco ese comando, consulte /help para obtener ayuda"
WARNING_FIELD_EMPTY_OR_INVALID = "🔎 Campo {} inválido o faltante se solicitara nuevamente para corregir los datos"


WARNING_MESSAGE_VERIFIED = "Muchas gracias {}, apenas su pago sea verificado se le estara notificando"