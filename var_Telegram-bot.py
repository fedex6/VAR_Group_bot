#
#   Telegram: @fedex6
#   BOT: @VAR_Group_bot
#
#---------------------#

## Basic imports & configuration
import os
import sys
import time
import requests
import json
import datetime
import telepot

## Bot data
token       =   '-- TOKEN --'

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

if command.startwith('/var'):
    admins = getChatAdministrators(chat_id)
    for a in admins:
        call_var_msg += admins

    bot.sendMessage(chat_id, 'Estan pidiendo VAR '+ call_var_msg)

bot = telepot.Bot(token) ## El Token esta al principio
bot.message_loop(handle)

while 1:
    try:
        time.sleep(0.5)

    except KeyboardInterrupt:
        ##LOG - Deja registro de que se freno el programa
        log = open("log.txt", "a")
        log.write('[ ' + time.ctime() + ' ] >>> Stoping...\n')
        log.close()
        print('\n Program interrupted')
        exit()