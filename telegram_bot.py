import telebot
import auto_data 
from telebot import types
from instagram_oop import InstagramBot

bot = telebot.TeleBot(auto_data.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton("/search", callback_data='search')

    markup.add(item)

    bot.send_message(message.chat.id,'Добро пожаловать,  {0.first_name}!\nЯ - <b>{1.first_name}</b>!, c моей помощью ты сможешь быстро получить и скачать аватарку из любого профиля в Instagram!'.format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=markup)

#@bot.message_handler(content_types=['text'])
#def send_message(message):
        #bot.send_message(message.chat.id, message.text)
        

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'search':
                bot.send_message(call.message.chat.id, '/search')
            else:
                bot.send_message(call.message.chat.id, "Нажми пожалуйста на поиск пидор")
 
            #bot.send_message(call.message.chat.id, call.message.text)
            
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                reply_markup=None)
        


    except Exception as _ex:
        print(repr(_ex))
            

@bot.message_handler(commands=['search'])
def handle_text(message):
    cid = message.chat.id
    msgPrice = bot.send_message(cid, 'Укажите никнейм:')
    bot.register_next_step_handler(msgPrice , step_Set_Price)

def step_Set_Price(message):
    cid = message.chat.id
    user = message.text
    bot.send_message(cid, f'your nickname is {user}')
    
    my_bot = InstagramBot(auto_data.username, auto_data.password)
    my_bot.save_img(user)

    bot.send_photo(cid, photo=open(f'img_instagram/{user}.jpeg','rb'))


# RUN
bot.polling(none_stop=True)
