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
PROVINCIAGENERAL="provinciaGeneral"
SEDE="sede"
TRAMITE_OFICINA="tramite_oficina"
TRAMITE_CUERPO_POLICIAL="tramite_cuperto_policial"
TYPEDOC="typeDoc"
DOC="doc"
NAME="name"
BIRTH="birth"
COUNTRY="country"


#FORMULARY
PAYMENT = "payment"
SUCESS = "sucess"
PLANS = "plans"
REFERENCE_PAYMENT = "reference_payment"
PLANS_TEX = "Planes"


ENTRAR = "Entrar"
CERRAR_SESION = "Cerrar sesión"
HIDDEN = "Ocultar Menú"
SHOW = "Mostrar Menú"
LOGOUT="logout"
INFORMATION="Mis Datos"
SIGNUP="Registrarse"

SET_MENU_REFERENCE_PAYMENT="Referencia de pago"
SET_MENU_METHOD_PAYMENT="Metodo de pago"
TOKEN_ASILO="tokenAsiloBot"
EXTRA_PARAMS="extra_params"
USERNAME_ASILO_BOT="usernameAsiloBot"
USERNAME_TELEGRAM="usernameTelegram"


DATA_CHAT_ID = 'chat_id'
DATA_TOKEN_USER = 'token_user'
DATA_MSGS_MENU_SHOW_AN_DHIDE = 'msgsMenuShowAndHide'
HIDDEN_MENU = 'hidden_menu'
MENU_DAT = 'menuDat'
DATA_USERTELEGRAM = 'usernameTelegram'
CHAT_MSG_USER = 'chatMsgUser'
CHAT_MSG_USER_BTN = 'chatMsgUserBtn'
CHAT_DATA_PERFIL = 'chat_data_perfil'



ACTION_USER_BOT_SIGNUP = 0
ACTION_USER_BOT_LOGIN = 1
ACTION_USER_BOT_LOGOUT = 2
ACTION_USER_BOT_HELP = 3
ACTION_USER_BOT_HELP = 3

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
SELECT_CONFIRM_PLANS_TEXT = "Seleccione un Plan:"


SUCESS_CONFIRM_PAYMENT_METHOD = 111
CONFIRM_CONFIRM_PAYMENT_METHOD_TEXT = "Confirme método de pago:"

SUCESS_REFERENCE_PAYMENT = 112
ENTER_REFERENCE_PAYMENT_TEXT = "Ingrese el Nro de referencia:"
CONFIRM_REFERENCE_PAYMENT_TEXT = "Confirma Nro de referencia:"
VALIDATING_REFERENCE_PAYMENT_WAITING_VALIDATING_TEXT = "Validando referencia este proceso puede del pago tardar de 24 horas o menos dependiendo de las solicitudes en nuestro sistema, luego de esto se le hará llegar una notificación con el cronograma de ejecuciones de acuerdo a su plan, !!! Muchas Gracias !!!"

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

SUCESS_CONFIRM_MENU_PLANS = 118
SUCESS_CONFIRM_MENU_PLANS_TEXT = "Seleccione un Plan:"


SUCESS_REFERENCE_MENU_PAYMENT = 119
ENTER_REFERENCE_PAYMENT_TEXT = "Ingrese el Nro de referencia:"

USER_REGISTER_PROCESS_TEXT = "Se esta realizando el registro de su usuario 🔑."
USER_REGISTER_SUCESS_TEXT = "✔️ Registro realizado con éxito."
SUCESS_USER_LOGOUT_SUCESS_TEXT = "✔️ Cierre de sesión realizado con éxito."
WARNING_USER_TEXT_GENERAL_TEXT = "⛔️ No se logro registrar el usuario, por favor intente de nuevo en unos minutos."
WARNING_USER_LOGIN_TEXT_GENERAL_TEXT = "⛔️ No se logro iniciar con su usuario, por favor intente de nuevo en unos minutos."
WARNING_USER_LOGOUT_SUCESS_TEXT = "Por favor ingrese su nombre de usuario y contraseña."
WARNING_USER_REFERENCE_PAYMENT_FAIL_TEXT = "⛔️ No se logró guardar su referencia de pago, por favor intente de nuevo."
WARNING_USER_PAYMENT_FAIL_TEXT = "⛔️ No se logró guardar su metodo de pago, por favor intente de nuevo."
WARNING_USER_LOGIN_FAIL_TEXT = "⛔️ No se logró iniciar sesion, por favor intente de nuevo."
WARNING_GET_PERFIL_FAIL_TEXT = "⛔️ No se logro obtener los datos de su perfil, por favor intente de nuevo."

WARNING_REFERENCE_FORMAT = "<b>La Referencia debe cumplir con los siguientes requisitos:</b>\n •<code><b>	Solo se permiten letras y números.</b></code>\n •<code><b> La longitud mínima es de 3 caracteres y la máxima de 40 caracteres.</b></code>"

WARNING_BIRT_FORMAT = "<b>El Año de nacimiento debe cumplir con los siguientes requisitos:</b>\n •<code><b>	Solo se permiten números.</b></code>\n •<code><b> La longitud debe ser de 4 numeros.</b></code>"

WARNING_DOC_FORMAT = "<b>El Numero de identificación debe cumplir con los siguientes requisitos:</b>\n •<code><b>	Solo se permiten letras y números.</b></code>\n •<code><b> La longitud mínima es de 6 caracteres y la máxima de 40 caracteres.</b></code>"

WARNING_USERNAME_FORMAT = "<b>El Nombre de usuario debe cumplir con los siguientes requisitos:</b>\n •<code><b>	Solo se permiten letras, números y guiones bajos.</b></code>\n •<code><b> La longitud mínima es de 4 caracteres y la máxima de 20 caracteres.</b></code>\n •<code><b> No pueden comenzar ni terminar con guiones bajos.</b></code>\n"

WARNING_NAME_FORMAT = "<b>El Nombre y Apellido debe cumplir con los siguientes requisitos:</b>\n •<code><b>	Solo se permiten letras.</b></code>\n •<code><b> La longitud mínima es de 7 caracteres y la máxima de 40 caracteres.</b></code>"




WARNING_USER_INTENTS_TEXT = "😔 Hubo un problema realizando su registro, intentando nuevamente por {} vez, si el problema persiste espere unos minutos e intente nuevamente."

WARNING_USER_NOT_LOGIN_TEXT = "No dispone de cuenta iniciada por favor valla a /login."

HIDDEN_MENU_TEXT = "👓 Ocultando menu."
SHOW_MENU_NOT_PAYMENT_TEXT = "👀 Agregando menu para usuario sin pago confirmado."

WARNING_USER_TEXT = "🤔 No conozco ese comando, consulte /help para obtener ayuda"
WARNING_FIELD_EMPTY_OR_INVALID_TEXT = "🔎 Campo {} inválido o faltante se solicitara nuevamente para corregir los datos"

USER_PLANS_SELECTMENU_TEXT = "✔️ Plan seleccionado con éxito."
USER_METHOD_PAYMENT_SELECTMENU_TEXT = "✔️ {} Como metodo de pago seleccionado con éxito."
USER_REFERENCE_PAYMENT_SELECTMENU_TEXT = "✔️ Referencia de pago guardada con éxito."
USER_REFERENCE_PAYMENT_NOT_SAVE_TEXT = "⛔️ No se logro guardar su referencia por favor intente de nuevo."

WARNING_MESSAGE_VERIFIED_TEXT = "Muchas gracias {}, apenas su pago sea verificado se le estara notificando"

WARNING_API_USERNAME_ALREADY_EXIST_TEXT = '⛔️ El nombre de usuario ya se existe (👤👤).'

WARNING_API_WRONG_PASSWORD_TEXT = '😣 Nombre de usuario o contraseña incorrecta.'

BLOCKED_USER_TEXT1 = 'EL usuario se encuentra bloqueado, para desbloquear/recuperar su usuario por favor ingrese /recovery.'

BLOCKED_USER_MINUTES_BLOCK=5
BLOCKED_USER_TEXT = "Límite de intentos excedidos, Por favor espere "+str(BLOCKED_USER_MINUTES_BLOCK)+" minutos e intente nuevamente."

SUCESS_USER_LOGIN_TEXT = '✔️ Inicio con su cuenta exitosamente.'

WARNING_USER_ALREADY_LOGIN = '⚠️ Ya existe una cuenta iniciada, Cierre session con /logout y registre una nueva.'

#API
WARNING_API_USERNAME_ALREADY_EXIST = 'USERNAME_ALREADY_EXISTS'
WARNING_API_USER_DOES_NOT_EXIST = 'USER_DOES_NOT_EXIST'
WARNING_API_WRONG_PASSWORD = 'WRONG_PASSWORD'
BLOCKED_USER = 'BLOCKED_USER'

WARNING_ERROR_GENERAL = 'Hubo un problema con su sulicitud Por favor intente de nuevo.'

RESPONSE_API_CORE = 'Respuesta de api:{msg}.'
