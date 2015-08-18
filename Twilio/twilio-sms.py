# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:10:43 2015

@author: Preto
"""

import twilio
import twilio.rest
 
account_sid = ""
auth_token  = ""


try:
    client = twilio.rest.TwilioRestClient(account_sid, auth_token)
 
    message = client.messages.create(
        body="Alerta de Prueba.",
        to="+34666666666",
        from_="+1500000000"
    )
    
except twilio.TwilioRestException as e:
    print(e)
    
