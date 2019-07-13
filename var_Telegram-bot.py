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

  if command.startswith('/var'):
    admins = bot.getChatAdministrators(chat_id)
    call_var_msg = ''
    for a in admins:
      call_var_msg += ' @' + str(a['user']['username'])

    bot.sendMessage(chat_id, 'Estan pidiendo VAR'+ call_var_msg)

bot = telepot.Bot(token) ## Poner el Token mas arriba
bot.message_loop(handle)

while 1:
  try:
    time.sleep(0.5)

  except KeyboardInterrupt:
    #LOG - Deja registro de que se freno el programa
    log = open("log.txt", "a")
    log.write('[ ' + time.ctime() + ' ] >>> Stoping...\n')
    log.close()
    print('\n Program interrupted')
    exit()