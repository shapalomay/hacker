from config import *
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

client = Client('ghoul-session', api_id, api_hash)

client.start()

client.stop()

print('иди давай пизды')


@client.on_message(filters.regex('тг 1000-7|ПИЗДА ВАМ') & filters.me)
def ghoul_spam_handler(client, message):
    i = 1000
    while i > 0:
        try:
            client.send_message(message.chat.id, f'{i} ya ghoul = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(1/messages_per_second)        

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


@client.on_message(filters.command(ghoul_table_command, prefixes=command_prefixes) & filters.me)
def ghoul_table_handler(client, message):
    i = ('Я СЛОМАЛ ТГ') 
    while i > 62:
        try:
            text = f'{i} - 7 = {i-7}'
            for j in range(1,10):
                text += f'\n{i-7*j} - 7 = {i-7*(j+1)}'
            message.edit_text(f'`{text}`')
            sleep(sleep_time_ghoul)
        except FloodWait as e:
            sleep(e.x)

        i -= 7

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


client.run()
