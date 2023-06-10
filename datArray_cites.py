# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 21:12:47 2023

@author: PC
"""

import constants

class array_cites():
        
    plans= ["Gratis: 3 veces al día (8:00 am, 15:00 pm, 21:00 pm).","Cada 5 minutos: 25 usd/Semanal","Cada 10 minutos: 23 usd/Semanal","Cada 20 minutos: 18 usd/Semanal","Cada 1 hora: 15 usd/Mensual","Cada 4 hora: 14 usd/Mensual","Cada 8 hora: 12 usd/Mensual","Cada 12 hora: 10 usd/Mensual","Cada 24 hora: 8 usd/Mensual"]
    

    finishUpdateProdifle= ["Realizado"]
    cancelProcess= ["Cancelar"]

    payment_method= ["Paypal","Btc","Usdt","Usdc","Zinli"]
    price_plans=[0,20,15,10,8,5,3,1,0.5]
    
    actions= ["Solicitar Cita","Consultar Citas Confirmadas","Anular Cita"]    
    confirm= ["Si","No"]
    countrys= [
            'AFGANISTAN',
            'ALBANIA',
            'ALEMANIA',
            'ANDORRA',
            'ANGOLA',
            'ANGUILLA',
            'ANTIGUA Y BARBUDA',
            'ANTILLAS NL.',
            'APATRIDA',
            'ARABIA SAUDI',
            'ARGELIA',
            'ARGENTINA',
            'ARMENIA',
            'ARUBA',
            'AUSTRALIA',
            'AUSTRIA',
            'AZERBAYAN',
            'BAHAMAS',
            'BAHREIN',
            'BANGLADESH',
            'BARBADOS',
            'BELGICA',
            'BELICE',
            'BENIN',
            'BHUTAN',
            'BIELORRUSIA O BELARUS',
            'BOLIVIA',
            'BOSNIA-HERZEGOVINA',
            'BOTSWANA',
            'BRASIL',
            'BRUNEI DARUSSALAM',
            'BULGARIA',
            'BURKINA FASO',
            'BURUNDI',
            'CABO VERDE',
            'CAMBOYA',
            'CAMERUN',
            'CANADA',
            'CENTROAFRICA REPUBLICA',
            'CHAD',
            'CHILE',
            'CHINA',
            'CHIPRE',
            'COLOMBIA',
            'COMORES',
            'CONGO BRAZZAVILLE',
            'COREA, REP. POP. DEMOC.',
            'COREA, REPUBLICA',
            'COSTA DE MARFIL',
            'COSTA RICA',
            'CROACIA',
            'CUBA',
            'DINAMARCA',
            'DJIBOUTI',
            'DOMINICA',
            'DOMINICANA REPUBLICA',
            'ECUADOR',
            'EEUU',
            'EGIPTO',
            'EL SALVADOR',
            'EL VATICANO',
            'EMIRATOS ARABES UNIDOS',
            'ERITREA',
            'ESLOVAQUIA',
            'ESLOVENIA',
            'ESPAÑA',
            'ESTONIA',
            'ETIOPIA',
            'FIDJI',
            'FILIPINAS',
            'FINLANDIA',
            'FRANCIA',
            'GABON',
            'GAMBIA',
            'GEORGIA',
            'GHANA',
            'GRANADA REPUBLICA',
            'GRECIA',
            'GUATEMALA',
            'GUAYANA',
            'GUINEA ECUATORIAL',
            'GUINEA REPUBLICA',
            'GUINEA-BISSAU',
            'HAITI',
            'HOLANDA',
            'HONDURAS',
            'HUNGRIA',
            'INDIA',
            'INDONESIA',
            'IRAK',
            'IRAN',
            'IRLANDA',
            'ISLANDIA',
            'ISLAS MARSCHALL',
            'ISRAEL',
            'ITALIA',
            'JAMAICA',
            'JAPON',
            'JORDANIA',
            'KAZAJSTAN',
            'KENIA',
            'KIRGUISTAN',
            'KIRIBATI',
            'KUWAIT',
            'LAOS',
            'LAS MALDIVAS',
            'LESOTHO',
            'LETONIA',
            'LIBANO',
            'LIBERIA',
            'LIBIA',
            'LIECHTENSTEIN',
            'LITUANIA',
            'LUXEMBURGO',
            'MACAO',
            'MACEDONIA',
            'MADAGASCAR',
            'MALASIA',
            'MALASIA - GRAN BRETAÑA',
            'MALAWI',
            'MALI',
            'MALTA',
            'MARRUECOS',
            'MAURICIO',
            'MAURITANIA',
            'MEJICO',
            'MICRONESIA',
            'MOLDAVIA',
            'MONACO',
            'MONGOLIA',
            'MONTENEGRO',
            'MOZAMBIQUE',
            'MYANMAR',
            'NAMIBIA',
            'NAURU',
            'NEPAL',
            'NICARAGUA',
            'NIGER',
            'NIGERIA',
            'NORUEGA',
            'NUEVA ZELANDA',
            'OMAN',
            'PAKISTAN',
            'PALESTINA EONU',
            'PANAMA',
            'PAPUA NUEVA GUINEA',
            'PARAGUAY',
            'PERU',
            'POLONIA',
            'PORTUGAL',
            'PUERTO RICO',
            'QATAR',
            'REINO UNIDO',
            'REP. DEMOCRATICA DEL CONGO (EX-ZAIRE)',
            'REPUBLICA CHECA',
            'REUNION-COMO',
            'RUANDA',
            'RUMANIA',
            'RUSIA',
            'SALOMON',
            'SAMOA OCCIDENTAL',
            'SAN CRISTOBAL Y NEVIS',
            'SAN MARINO',
            'SAN VICENTE',
            'SANTA LUCIA',
            'SANTO TOME Y PRINCIPE',
            'SEICHELLES',
            'SENEGAL',
            'SENEGAMBIA',
            'SERBIA',
            'SIERRA LEONA',
            'SINGAPUR',
            'SIRIA',
            'SOMALIA',
            'SRI LANKA',
            'SUDAFRICA',
            'SUDAN',
            'SUECIA',
            'SUIZA',
            'SURINAM',
            'SWAZILANDIA',
            'TADJIKISTAN',
            'TAIWAN',
            'TANZANIA',
            'THAILANDIA',
            'TIMOR ORIENTAL',
            'TOGO',
            'TONGA',
            'TRINIDAD Y TOBAGO',
            'TUNEZ',
            'TURKMENIA',
            'TURQUIA',
            'TUVALU',
            'UCRANIA',
            'UGANDA',
            'URUGUAY',
            'UZBEKISTAN',
            'VANUATU',
            'VENEZUELA',
            'VIETNAM',
            'YEMEN',
            'ZAMBIA',
            'ZIMBABWE']
        
    provinces = ['ACoruña',
                  'Albacete',
                  'Alicante',
                  'Almería',
                  'Araba',
                  'Asturias',
                  'Ávila',
                  'Badajoz',
                  'Barcelona',
                  'Bizkaia',
                  'Burgos',
                  'Cáceres',
                  'Cádiz',
                  'Cantabria',
                  'Castellón',
                  'Ceuta',
                  'CiudadReal',
                  'Córdoba',
                  'Cuenca',
                  'Gipuzkoa',
                  'Girona',
                  'Granada',
                  'Guadalajara',
                  'Huelva',
                  'Huesca',
                  'IllesBalears',
                  'Jaén',
                  'LaRioja',
                  'LasPalmas',
                  'León',
                  'Lleida',
                  'Lugo',
                  'Madrid',
                  'Málaga',
                  'Melilla',
                  'Murcia',
                  'Navarra',
                  'Ourense',
                  'Palencia',
                  'Pontevedra',
                  'Salamanca',
                  'S.CruzTenerife',
                  'Segovia',
                  'Sevilla',
                  'Soria',
                  'Tarragona',
                  'Teruel',
                  'Toledo',
                  'Valencia',
                  'Valladolid',
                  'Zamora',
                  'Zaragoza']
    
    oficines = ['Cualquier oficina',
            'CNP AVDA POBLADOS, Avda. de los Poblados, S/N',
            'CNP Comisaría de Alcalá de Henares, Avda. de Meco, s/n',
            'CNP Comisaría de Alcobendas, Avda. de España, 52',
            'CNP Comisaría de Alcorcón, Alfredo Nobel, 10',
            'CNP Comisaría de Aranjuez, Avda. Príncipe, 40',
            'CNP Comisaría de Arganda del Rey, Av.Mediterraneo(PoliciaLocal), 7',
            'CNP Comisaría de Collado Villalba, SAN FERNANDO, 27',
            'CNP Comisaría de Coslada, Guadalquivir, 16',
            'CNP Comisaría de Fuenlabrada, Calle de los Ángeles, 9',
            'CNP Comisaría de Getafe, Churruca, 6',
            'CNP Comisaría de Leganés, Avda. de Universidad, 27',
            'CNP Comisaría de Majadahonda, Ctra.Villanueva del Pardillo, 3',
            'CNP Comisaría de Móstoles, Granada, 9',
            'CNP Comisaría de Parla, Avda. Juan Carlos I, 2',
            'CNP Comisaría de Pozuelo de Alarcón, Camino de las Huertas, 36',
            'CNP Comisaría de Rivas Vaciamadrid, José Hierro, 82',
            'CNP Comisaría de Torrejón de Ardoz, Hilados, 15',
            'CNP Comisaría de Valdemoro, Avda. de España, 97',
            'CNP OFICINA AQUILES 2, Aquiles, 2',
            'CNP Padre Piquer, Padre Piquer, 18',
            'CNP SANTA ENGRACIA, SANTA ENGRACIA, 18',
            'Comisaría de Getafe 2, churruca, 6',
            'CREADE POZUELO, Paseo de la Casa Campo, 1',
            'García de Paredes, García de Paredes, 65',
            'Leganés, San Nicasio, 31',
            'Oficina de Asilo y Refugio, C/ Pradillo, 40',
            'Silva, Silva, 19']
    
    tramite_oficine_extrajera = [
                             'AUT. RES. TEMPORAL POR CIRCUNSTANCIAS EXCEPCIONALES POR RAZONES HUMANITARIAS, PROTECCIÓN INTERNACIONAL (art. 125) y DISP.',
                             'AUTORIZACIÓN DE RESIDENCIA TEMPORAL POR CIRCUNSTANCIAS EXCEPCIONALES POR ARRAIGO',
                             'AUTORIZACIÓN DE RESIDENCIA Y TRABAJO INICIAL POR CUENTA AJENA',
                             'AUTORIZACIÓN DE RESIDENCIA Y TRABAJO INICIAL POR CUENTA PROPIA',
                             'AUTORIZACIÓN DE TRABAJO PARA ESTUDIANTES',
                             'AUTORIZACIÓN RESIDENCIA TEMPORAL DE MENORES NACIDOS EN ESPAÑA, HIJOS DE EXTRANJEROS RESIDENTES LEGALES',
                             'AUTORIZACIÓN RESIDENCIA TEMPORAL DE MENORES NO NACIDOS EN ESPAÑA, HIJOS DE EXTRANJEROS RESIDENTES LEGALES',
                             'AUTORIZACIÓN RESIDENCIA Y TRABAJO POR CIRCUNSTANCIAS EXCEPCIONALES POR VIOLENCIA DE GÉNERO',
                             'REAGRUPACIÓN FAMILIAR INICIAL',
                             'RECUPERACIÓN DE LA RESIDENCIA DE LARGA DURACIÓN',
                             'TARJETA INICIAL DE RESIDENCIA DE FAMILIAR DE CIUDADANO COMUNITARIO']
    
    tramite_cuerpo_nacional_policial = [
                                    'ASILO - OFICINA DE ASILO\n Y  REFUGIO. Entrevista Telefónica Trabajador/a  Social. Calle Pradillo',
                                    'ASILO - PRIMERA CITA-provincia de Madrid',
                                    'ASILO-OFIC. DE ASILO Y REFUGIO.EXP/REN TIE Protección Internacional y Documentos Viaje.c/Pradillo 40',
                                    'ASILO-OFICINA DE ASILO Y REFUGIO."nueva normalidad” Expedición/Renovación Documentos.C/ Pradillo 40',
                                    'AUTORIZACIÓN DE REGRESO',
                                    'POLICIA - RECOGIDA DE TARJETA DE IDENTIDAD DE EXTRANJERO (TIE)',
                                    'POLICIA-ASIGNACIÓN DE N.I.E.',
                                    'POLICIA-CARTA DE INVITACIÓN',
                                    'POLICIA-CERTIFICADO DE REGISTRO DE CIUDADANO DE LA U.E.',
                                    'POLICIA-CERTIFICADOS (DE RESIDENCIA, DE NO RESIDENCIA Y DE CONCORDANCIA)',
                                    'POLICIA-INFORMACION DE TRÁMITES DE LA COMISARÍA DE POLICIA',
                                    'POLICIA-TOMA DE HUELLA (EXPEDICIÓN DE TARJETA), RENOVACIÓN DE TARJETA DE LARGA DURACIÓN Y DUPLICADO',
                                    'POLICIA-TOMA DE HUELLA POR IMPOSIBILIDAD DE DESPLAZAMIENTO',
                                    'POLICÍA - CÉDULA DE INSCRIPCIÓN',
                                    'POLICÍA - RECOGIDA DE LA T.I.E. CUYA AUTORIZACIÓN RESUELVE LA DIRECCIÓN GENERAL DE MIGRACIONES',
                                    'POLICÍA TARJETA CONFLICTO UCRANIA–ПОЛІЦІЯ -КАРТКА ДЛЯ ПЕРЕМІЩЕНИХ ОСІБ ВНАСЛІДОК КОНФЛІКТУ В УКРАЇНІ',
                                    'POLICÍA-EXP.TARJETA ASOCIADA AL ACUERDO DE RETIRADA CIUDADANOS BRITÁNICOS Y SUS FAMILIARES (BREXIT)',
                                    'POLICÍA-EXPEDICIÓN DE TARJETAS CUYA AUTORIZACIÓN RESUELVE LA DIRECCIÓN GENERAL DE MIGRACIONES']
    
    
    tipo_doc=["N.I.E","D.N.I","PASAPORTE"]
    
    data_perfil= {"data":[{"text":"Provincia General: ","code":constants.SUCESS_PROVINCE,"lbl":constants.PROVINCIAGENERAL,"default":-1,"array":provinces},{"text":"Oficina: ","code":constants.SUCESS_OFICINE,"lbl":constants.SEDE,"default":-1,"array":oficines},{"text":"Oficina extranjera: ","code":constants.SUCESS_OFICINE_EXTRANJERA,"lbl":constants.TRAMITE_OFICINA,"default":-1,"array":tramite_oficine_extrajera},{"text":" Oficina para Tramite Cuerpo Policial: ","code":constants.SUCESS_TRAMITE_CUERPO_POLICIAL,"lbl":constants.TRAMITE_CUERPO_POLICIAL,"default":-1,"array":tramite_cuerpo_nacional_policial},{"text":"Tipo de documento: ","code":constants.SUCESS_TIPO_DOC,"lbl":constants.TYPEDOC,"default":-1,"array":tipo_doc},{"text":"Documento de Identidad: ","code":constants.SUCESS_CONFIRM_DOCUMENT,"lbl":constants.DOC,"default":'',"array":[]},{"text":"Nombre y Apellido: ","code":constants.SUCESS_CONFIRM_NAME,"lbl":constants.NAME,"default":'',"array":[]},{"text":"Año de Nacimiento: ","code":constants.SUCESS_CONFIRM_BIRTH,"lbl":constants.BIRTH,"default":'',"array":[]},{"text":"Pais: ","code":constants.SUCESS_COUNTRY,"lbl":constants.COUNTRY,"default":-1,"array":countrys},{"text":"Plan: ","code":constants.SUCESS_CONFIRM_PLANS,"lbl":constants.PLANS,"default":-1,"array":plans,"caseTitle":11},{"text":"Tipo de pago: ","code":constants.SUCESS_CONFIRM_PAYMENT_METHOD,"lbl":constants.TYPE_PAYMENT,"default":-1,"array":payment_method,"caseTitle":12},{"text":"Regencia de pago: ","code":constants.SUCESS_REFERENCE_PAYMENT,"lbl":constants.REFERENCE_PAYMENT,"default":'',"array":[],"caseTitle":18}]}

    def getCountrys(self):
            return self.countrys
        
    def getProvinces(self):
            return self.provinces
        
    def getOficines(self):
            return self.oficines
        
    def getTramite_oficine_extrajera(self):
            return self.tramite_oficine_extrajera
        
    def getTramite_cuerpo_nacional_policial(self):
            return self.tramite_cuerpo_nacional_policial    

    

