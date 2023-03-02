# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:14:10 2023

@author: PC
"""
END="Fin."
START="Inicio."
YES="Si"
USERNAME="username"
PASSWORD="password"


ERROR_RUN_MAIN_SECONDS =5
ERROR_RUN_MAIN_FAILE="No se logro iniciar cita_asilo, se intentara luego de: " + str(ERROR_RUN_MAIN_SECONDS) + " Segundos."

SUCESS_COUNTRY = 100
SELECT_COUNTRY_TEXT = "Seleccione su país de nacionalidad:"


SUCESS_PROVINCE = 101
SELECT_PROVINCE_TEXT = "Seleccione una Provincia:"


SUCESS_OFICINE = 102
SELECT_OFICINE_TEXT = "Seleccione una Oficina:"

SUCESS_OFICINE_EXTRANJERA = 103
SELECT_OFICINE_EXTRANJERA_TEXT = "Seleccione una Oficina Extranjera:"

SUCESS_TRAMITE_CUERPO_POLICIAL = 104
SELECT_TRAMITE_CUERPO_POLICIAL_TEXT = "Seleccione una Oficina para Tramite Cuerpo Policial:"


SUCESS_TIPO_DOC = 105
SELECT_TIPO_DOC_TEXT = "Seleccione un Tipo de documento:"


SUCESS_CONFIRM_DOCUMENT = 106
ENTER_DOCUMENT_TEXT = "Ingrese su Documento de Identidad:"
CONFIRM_DOCUMENT_CONFIRM_TEXT = "Confirme su Documento de Identidad:"


SUCESS_CONFIRM_NAME = 107
ENTER_CONFIRM_NAME_TEXT = "Ingrese su Nombre y Apellido:"
CONFIRM_CONFIRM_NAME_TEXT = "Confirme su Nombre y Apellido:"


SUCESS_CONFIRM_BIRTH = 108
ENTER_CONFIRM_BIRTH_TEXT = "Ingrese su Año de Nacimiento:"
CONFIRM_CONFIRM_BIRTH_CONFIRM_TEXT = "Confirme su Año de Nacimiento:"

SUCESS_CONFIRM_ACTIONS = 109
SELECT_CONFIRM_ACTIONS_TEXT = "Seleccione una acción:"


SUCESS_CONFIRM_PLANS = 110
SELECT_CONFIRM_PLANS_TEXT = "Seleccione una Plan:"


SUCESS_CONFIRM_PAYMENT_METHOD = 111
CONFIRM_CONFIRM_PAYMENT_METHOD_TEXT = "Confirme método de pago:"

SUCESS_REFERENCE_PAYMENT = 112
ENTER_REFERENCE_PAYMENT_TEXT = "Ingrese el Nro de referencia:"
CONFIRM_REFERENCE_PAYMENT_TEXT = "Confirma Nro de referencia:"
VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT = "Validando referencia este proceso puede del pago tardar de 1 a 2 horas, luego de esto se le hará llegar una notificación con las Horas/Minutos en la que se realizara el proceso"

SUCESS_USER_REGISTER_USERNAME = 113
ENTER_USERNAME_TEXT = "Ingrese un nombre de usuario:"
CONFIRM_USERNAME_TEXT = "Confirme su nombre de usuario:"



SUCESS_USER_REGISTER_PASSWORD = 114
ENTER_PASSWORD_TEXT = "Ingrese una contraseña:"
CONFIRM_PASSWORD_TEXT = "Confirme su contraseña:"

SUCESS_CONFIRM_PAYMENT = 115
CONFIRM_CONFIRM_PAYMENT_TEXT = "Confirme pago realizado"

SUCESS_USER_LOGIN_TEXT = "Usuario ingresado con éxito."
SUCESS_USER_LOGIN_VALIDATE_TEXT = "Usuario validado con éxito."



SUCESS_USER_LOGIN_USERNAME = 116
SUCESS_USER_LOGIN_PASSWORD = 117

USER_REGISTER_PROCESS_TEXT = "Se esta realizando el registro de su usuario 🔑."
USER_REGISTER_SUCESS_TEXT = "✔️ Registro realizado con éxito."
SUCESS_USER_LOGOUT_SUCESS_TEXT = "✔️ Cierre de sesión realizado con éxito."
WARNING_USER_TEXT_GENERAL_TEXT = "⛔️ No se logro registrar el usuario, por favor intente de nuevo en unos minutos."
WARNING_USER_LOGOUT_SUCESS_TEXT = "Por favor ingrese su nombre de usuario y contraseña."

WARNING_USER_INTENTS_TEXT = "😔 Hubo un problema realizando su registro, intentando nuevamente por {} vez, si el problema persiste espere unos minutos e intente nuevamente."

WARNING_USER_NOT_LOGIN_TEXT = "No dispone de cuenta iniciada por favor valla a /login."

WARNING_USER_TEXT = "🤔 No conozco ese comando, consulte /help para obtener ayuda"
WARNING_FIELD_EMPTY_OR_INVALID_TEXT = "🔎 Campo {} inválido o faltante se solicitara nuevamente para corregir los datos"

WARNING_MESSAGE_VERIFIED_TEXT = "Muchas gracias {}, apenas su pago sea verificado se le estara notificando"

WARNING_API_USERNAME_ALREADY_EXIST_TEXT = '⛔️ El nombre de usuario ya se existe (👤👤).'

WARNING_API_WRONG_PASSWORD_TEXT = 'Nombre de usuario o contraseña incorrecta.'

BLOCKED_USER_TEXT1 = 'EL usuario se encuentra bloqueado, para desbloquear/recuperar su usuario por favor ingrese /recovery.'

BLOCKED_USER_MINUTES_BLOCK=5
BLOCKED_USER_TEXT = "Límite de intentos excedidos, Por favor espere "+str(BLOCKED_USER_MINUTES_BLOCK)+" minutos e intente nuevamente."

SUCESS_USER_LOGIN_TEXT = '✔️ Inicio con su cuenta exitosamente.'

WARNING_USER_ALREADY_LOGIN = '⚠️ Ya existe una cuenta iniciada con {username}, Cierre session con /close y registre una nueva.'

#API
WARNING_API_USERNAME_ALREADY_EXIST = 'USERNAME_ALREADY_EXISTS'
WARNING_API_USER_DOES_NOT_EXIST = 'USER_DOES_NOT_EXIST'
WARNING_API_WRONG_PASSWORD = 'WRONG_PASSWORD'
BLOCKED_USER = 'BLOCKED_USER'
