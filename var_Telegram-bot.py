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
  g = telepot.glance(msg)

  if g[0] ==  'left_chat_member':
    if msg['left_chat_participant']['username'] != '':
      arroba = ' (@' + str(msg['left_chat_participant']['username'].encode('ascii', 'ignore').decode('ascii')) + ')'
    else :
     arroba = ''

    bot.sendMessage(chat_id, 'Que entre la camilla para ' + str(msg['left_chat_participant']['first_name'].encode('ascii', 'ignore').decode('ascii')) + arroba + ' que se va lesionado.')
    #print(msg)
    command = ''
  else :
    command = msg['text']
  

  if command.startswith('/var'):
    admins = bot.getChatAdministrators(chat_id)
    call_var_msg = ''
    for a in admins:
      try:
        call_var_msg += ' @' + str(a['user']['username'])
      except KeyError:
        call_var_msg += ' ' + str(a['user']['first_name'].encode('ascii', 'ignore').decode('ascii')) + ','

    bot.sendMessage(chat_id, 'Estan pidiendo VAR'+ call_var_msg)

  if command.startswith('/id'):
    bot.sendMessage(chat_id, chat_id)

  if command.startswith('ah') or command.startswith('ahre'):
    bot.deleteMessage(telepot.message_identifier(msg))


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