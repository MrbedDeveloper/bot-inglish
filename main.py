import telebot
from telebot import types

bot = telebot.TeleBot('6497029843:AAFuuBr4Frxg9zLHnY1ik-QMZCt-v11P4Q8')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "/start", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("easy📗")
        item2 = types.KeyboardButton("normal📙")
        item3 = types.KeyboardButton("hard📕")
        item5 = types.KeyboardButton("инфо🔰")
        back = types.KeyboardButton("Назад")
    
        markup.add(item1, item2, item3, back,item5)
        
        bot.send_message(message.from_user.id, 'Привет, {0.first_name}! Please select a level', reply_markup=markup) #ответ бота


    elif message.text == 'easy📗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("еда")
        item2 = types.KeyboardButton("ВНЕШНОСТЬ ЧЕЛОВЕКА")
        item3 = types.KeyboardButton("ПРОФЕССИИ")
        item8 = types.KeyboardButton("правило1🧩")
        back = types.KeyboardButton("Назад")
    
        markup.add(item1, item2, item3,item8,back)
        
        bot.send_message(message.from_user.id, 'easy📗', reply_markup=markup) #ответ бота


    elif message.text == 'normal📙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("еда")
        item2 = types.KeyboardButton("Внешность ЧЕЛОВЕКА")
        item3 = types.KeyboardButton("ПРОФЕССИИ")
        item8 = types.KeyboardButton("правило1🧩")
        back = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3,item8, back)
        bot.send_message(message.from_user.id, 'normal📙', reply_markup=markup) #ответ бота

    elif message.text == 'hard📕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("еда")
        item2 = types.KeyboardButton("ВНЕШНОСТЬ ЧЕЛОВЕКА")
        item3 = types.KeyboardButton("ПРОФЕССИИ")
        item8 = types.KeyboardButton("правило1🧩")
        back = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3,item8, back) 
        bot.send_message(message.from_user.id, 'hard📕', reply_markup=markup) #ответ бота
       
    

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item0 = types.KeyboardButton("easy📗")
        item11 = types.KeyboardButton("normal📙")
        item33 = types.KeyboardButton("hard📕")
        item00 = types.KeyboardButton("инфо🔰")
    
    
        markup.add(item0, item11, item33,item00)
        
        bot.send_message(message.from_user.id, 'назад', reply_markup=markup) #ответ бота

    elif message.text == 'ВНЕШНОСТЬ ЧЕЛОВЕКА':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back)
        bot.send_message(message.from_user.id, 'old - старый young - молодой pretty - красивая только о женщинах\n handsome - красивый (только о мужчинах) \n slim - стройный, \n fat - тучный, с лишним весом, \n describe - описывать, \n tall - высокий, \n short - невысокий, \n hair - волосы, \neyes - глаза, \nbald - лысый, \nlook like - выглядеть как, \nappearance - внешность, \nheight - рост, \nmiddle-sized - среднего роста, \nbuild - телосложение, \nthin - худой, \nathletic - мускулистый, \nhair colour - цвет волос, \nfair - светлые, \ndark - темные, \nblack - черные, \nbrown - коричневые, \nred - рыжие, \nblond - очень светлые, \nshort - короткие, \nlong - длинные, \nstraight - прямые, \nwavy - волнистые, \ncurly - кудрявые, \nthick - густые, \nthin - редкие, \nbig - большие, \nlittle - маленькие, \ngreen - зеленые, \nblue - голубые, \nbrown - карие, \noval - овальное, \nlong - длинный, \nstraight - прямой, \nturned up - вздернутый, \nmouth - рот, \nlips - губы, \nteeth - зубы,\nears - уши, \nforehead - лоб, \nneck - шея, \nbody - туловище, \narms - руки, \nhands - руки, \nlegs - ноги, \nknees - колени, \nfeet - ступни. ')

    elif message.text == 'правило1🧩':
        bot.send_photo(message.chat.id,  photo=open('key.jpg',  'rb'), caption='Правило')

    elif message.text == 'Внешность ЧЕЛОВЕКА':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back)
        bot.send_message(message.from_user.id, 'tall высокий \nshort низкий \npetite изящная, \nминиатюрная (о женщине) good bad shape хорошая плохая форма\n well-built хорошо сложенный \nslim/slender стройный \na delicate figure,\nconstitution хрупкое телосложение \nskinny худой, тощий \nfeeble weak хилый, \nслабый \nunderweight имеющий недостаточный вес \nlanky долговязый, \nхудой gangling/gangly неуклюжий, нескладный\n plump/stout полный\n portly тучный (о мужчинах средних лет) \nobese  толстый, страдающий ожирением \noverweight имеющий избыточный вес \npowerful мощный, \nсильный athletic атлетичный, физически сильный \nstrong muscular сильный, крепкий, мускулистый\n broad-shouldered широкоплечий \nnarrow-shouldered узкоплечий\n round-shouldered сутулый')


    elif message.text == 'еда':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_message(message.from_user.id, 'Dairy Молочные продукты \nGrains Зерна, зерновые\n Beans Фасоль, бобовые \nNuts Орехи\n Meat Мясо \nSeafood Морепродукты \nDessert Десерт \nGrill Гриль, блюда гриль \nFry Жарить \nBoil Варить \nSteam Готовить на пару \nPorridge Каша')

    elif message.text == 'инфо🔰':
        
        bot.send_message(message.from_user.id, 'разработчик бота  при разработке бота были использована библиотека telebot , плтёжная система для полного изучения англиского находится на данный момент в разработке')


    elif message.text == 'ПРОФЕССИИ':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Донат ", url='https://www.donationalerts.com/r/kerchi')
        markup.add(button1)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и если захочешь можешь кинуть донат)".format(message.from_user), reply_markup=markup)
    


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть