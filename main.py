import telepot
token = '827034007:AAFYKyXf9By2cd1M2PG_Zrtim03pFN_mtoU'
bot = telepot.Bot(token)

def handle_text(message):
    content_type, cht_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  '/0' in command:
            bot.sendMessage(chat_id, "Комп не уйдёт в спящий режим")#А это ответ бота в чат.

        if  '/1' in command:
            bot.sendMessage(chat_id, "Комп уйдёт в спящий режим через одну минуту простоя")

        if  '/off pc' in command:
            bot.sendMessage(chat_id, "Выключаю комп")

    
        
bot.message_loop(handle_text)

