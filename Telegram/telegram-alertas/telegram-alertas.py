# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:10:22 2015

Usamos esta api
https://pypi.python.org/pypi/python-telegram-bot

@author: preto
"""

import telegram
import time
import sys

status = False
err = 0

while status == False:

    try:
        tbot = telegram.Bot(token="", debug=False)
        status = True
        
    except:
        print("Error al inicializar el bot, se va a reintentar en 3 segundos.")
        err = err + 1
        print("Errores: " + str(err))
        time.sleep(3)
        if err > 3:
            print("No se ha podido iniciar el sistema de mensajería.")
            time.sleep(10)
            sys.exit()
        

def configurar():
    """Carga los datos de configuración del fichero config.txt"""
    
    try:
        with open("config.txt", "r", encoding='utf-8') as config:
            datos = config.readlines()
            msg = datos[4]
            servicio = datos[3]        
    except:
        print("No se ha podido cargar el fichero de configuración - config.txt/n Asegurese de que está dentro del directorio del programa.")
        time.sleep(10)
        sys.exit()
        
    return(msg, servicio)
        

def mensaje():
    """Envía un mensaje con los datos del fichero de configuración"""
     
    status = False
    datos = configurar()
    chatid = 0000000  # ID del chat que va a recibir el mensaje.
    
    while status == False:
        
        try:
            tbot.sendMessage(chatid,datos[0] + " Lugar: " + datos[1])
            status = True
        except:
            print("El proceso ha fallado. Se va a reintentar en 3 segundos.")        
            time.sleep(3)


mensaje()