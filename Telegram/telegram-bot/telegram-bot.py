# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:10:22 2015

https://pypi.python.org/pypi/python-telegram-bot

@author: preto
"""

import telegram
import time

tbot = telegram.Bot(token="", debug=False)


def update():
    """ Comprueba si hay mensajes nuevos y si los hay les responde con el mismo texto.  """
    off = tbot.getUpdates()[0].update_id
    msgid = 0
    #print(off, "offset")

    while off != 0:
        msg = tbot.getUpdates(offset=off)
        #print(msg[-1].update_id, "  ", off)
        
        if msg[-1].update_id > off:
            
            for m in msg:
                if m.message.message_id > msgid:
                    print(m.message.chat_id, " - ", m.message.chat.first_name, " - ", m.message.text)
                    tbot.sendMessage(m.message.chat_id, "Eco, eco")
                    tbot.sendMessage(m.message.chat_id, m.message.text, reply_to_message_id=m.message.message_id)
                    msgid = m.message.message_id
                
            off = tbot.getUpdates()[-1].update_id
            
        else:
            time.sleep(30)

update()
