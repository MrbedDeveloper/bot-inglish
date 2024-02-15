# -*- coding: utf-8 -*-

import telebot
from telebot import types
import random


bot = telebot.TeleBot('6456827598:AAEikgqsnNphbYjyLsvUaFasGfRTeJurYQ8')

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
        
        bot.send_message(message.from_user.id, 'Привет! Please select a level', reply_markup=markup) #ответ бота

#легкий
    elif message.text == 'easy📗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("еда 🍉")#
        item2 = types.KeyboardButton("ВНЕШНОСТЬ ЧЕЛОВЕКА🤩")#
        item4 = types.KeyboardButton("ХарактеР🎭")#
        item7 = types.KeyboardButton("cпорт🏈")
        item10 = types.KeyboardButton("Дом🏠")
        item9 = types.KeyboardButton("ХоббИ🎨")
        item3 = types.KeyboardButton("ПРОФЕССИи📝")
        item8 = types.KeyboardButton("правило1🧩")
        back = types.KeyboardButton("Назад")
    
        markup.add(item1, item2, item4, item3,item8,item7, item9, item10, back)
        
        bot.send_message(message.from_user.id, 'easy📗', reply_markup=markup) #ответ бота

#средний 
    elif message.text == 'normal📙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("еДа 🍉")#
        item2 = types.KeyboardButton("Внешность ЧЕЛОВЕКА🤩")#
        item4 = types.KeyboardButton("Характер🎭")#
        item7 = types.KeyboardButton("Спорт🏈")
        item10 = types.KeyboardButton("дОм🏠")
        item9 = types.KeyboardButton("ХобБи🎨")
        item3 = types.KeyboardButton("ПРОФЕССиИ📝")
        item8 = types.KeyboardButton("правило2🧩")
        back = types.KeyboardButton("Назад")
    
        markup.add(item1, item2, item4, item3,item8,item7, item9, item10, back)
        bot.send_message(message.from_user.id, 'normal📙', reply_markup=markup) #ответ бота
#сложный
    elif message.text == 'hard📕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item1 = types.KeyboardButton("едА 🍉")#
        item2 = types.KeyboardButton("ВНЕШНОСТь ЧЕЛОВЕКА🤩")#
        item4 = types.KeyboardButton("характер🎭") #
        item7 = types.KeyboardButton("СпорТ🏈")
        item10 = types.KeyboardButton("доМ🏠")
        item9 = types.KeyboardButton("хоббИ🎨")
        item3 = types.KeyboardButton("ПрОФЕССИИ📝")
        item8 = types.KeyboardButton("правило3🧩")
        back = types.KeyboardButton("Назад")
    
        markup.add(item1, item2, item4, item3,item8,item7, item9, item10, back)
        bot.send_message(message.from_user.id, 'hard📕', reply_markup=markup) #ответ бота
       
    

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item0 = types.KeyboardButton("easy📗")
        item11 = types.KeyboardButton("normal📙")
        item33 = types.KeyboardButton("hard📕")
        item00 = types.KeyboardButton("инфо🔰")
    
    
        markup.add(item0, item11, item33,item00)
        
        bot.send_message(message.from_user.id, 'назад', reply_markup=markup) #ответ бота

######################################################################################
#легкий внешность
    elif message.text == 'ВНЕШНОСТЬ ЧЕЛОВЕКА🤩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back)
        bot.send_photo(message.chat.id, photo=open('s.png',  'rb'), caption='old [əʊld] старый \n, young [jʌŋ] молодой \n, pretty [ˈprɪti] красивая (только о женщинах), handsome [ˈhæn.səm] красивый (только о мужчинах) \n, slim [slɪm] стройный \n, fat [fæt] тучный с лишним весом \n, describe [dɪˈskraɪb] описывать \n,  tall [tɔːl] высокий, short [ʃɔːt] невысокий \n, hair [heə] волосы \n, eyes [aɪz] глаза \n, bald [bɔːld] лысый \n, look like [lʊk] [laɪk] выглядеть как \n, appearance [əˈpɪərəns] внешность, 1 appearance – внешность \n, 2 height [hait] — рост \n, middle — sized — среднего роста \n, 3 build — телосложение \n, thin – худой, fat — толстый \n, slim — стройный (о девушке) , athletic — мускулистый (спортивный) , 4 hair colour — цвет волос , fair — светлые , dark — темные \n, black — черные \n,  brown — коричневые \n, red — рыжие \n, blond — очень светлые \n, 5 hair  — волосы \n, short — короткие \n, long — длинные \n, straight — прямые \n, wavy — волнистые \n, curly — кудрявые \n, thick — густые \n, thin — редкие \n, 6 eyes — глаза \n, big — большие \n, little — маленькие \n, green — зеленые \n, blue — голубые')

    elif message.text == 'правило1🧩':
        bot.send_photo(message.chat.id,  photo=open('key.jpg',  'rb'), caption='Правило')
#средний внешность
    elif message.text == 'Внешность ЧЕЛОВЕКА🤩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back)
        bot.send_photo(message.chat.id,  photo=open('s.png',  'rb'), caption='Appearance	Внешность, Freckles	Веснушки, Snub	Курносый, Uneven	Неровный, Dimples	Ямочки на щеках, Figure	Фигура, Arched	Дугой (про брови), Forehead	Лоб, Cheekbones	Скулы, Ears	Уши, Blond	Белокурый, Auburn	Рыжеватый, Bald	Лысый, Red	Красный, Silky	Шелковистый, Golden	Золотистый, Hairstyle	Прическа, Braid	Коса, Curls	Кудри, Straight	Прямые, Lock	Прядь, Wavy	Волнистый, Jaw	Челюсть, Hazel	Ореховый (про цвет глаз)')
    elif message.text == 'правило2🧩':
        bot.send_photo(message.chat.id,  photo=open('2.jpg',  'rb'), caption='Правило')

#сложный внешность 
    elif message.text == 'ВНЕШНОСТь ЧЕЛОВЕКА🤩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок 
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back)
        bot.send_photo(message.chat.id,  photo=open('s.png',  'rb'), caption='Complexion	Цвет лица, Wrinkles	Морщины, Facial features	Черты лица, Chiseled	Точеный, Delicate	Тонкий, Sallow	Желтоватый, Disheveled	Взъерошенный, Forelock	Передняя прядь волос, Eyelashes	Ресницы, Graceful	Грациозный, Lathy	Долговязый, Lean	Худой, Plump	Полный, Chubby	Круглый (о фигуре), Slender	Стройный, Slim	Подтянутый, Prominent	Выдающийся, Turned up	Вздернутый, Unprepossessing	Неказистый, нераспологающий, Bony	Костлявый, Bearing	Осанка, Posture	Поза, Shaggy	Растрепанный, Glasz	Разноцветные или меняющие цвет глаза')
    elif message.text == 'правило3🧩':
        bot.send_photo(message.chat.id,  photo=open('3.jpg',  'rb'), caption='Правило')
#####################################################################################################



##############################################################################################
#еда легко
    elif message.text == 'еда 🍉':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('f.png',  'rb'), caption= '•  a sandwich — бутерброд, •  toast — поджаренный хлеб, •  a cake — торт, пирожное, •  a bun — булочка, •  tea — чай, •  coffee — кофе, •  sugar — сахар, •  porridge — каша, •  cheese — сыр, •  sausage — колбаса, •  sausages — сосиски, •  salt — соль, •  pepper — перец, •  salad — салат, •  soup  — суп, •  meat  — мясо, •  chiсken — курица, •  fish — рыба, •  cutlets — котлеты, •  potatoes — картошка, •  tomatoes — помидоры, •  vegetables — овощи, •  soup — суп, •  bread — хлеб, •  butter — масло, •  a drink — напиток, •  milk — молоко, •  juice — сок, •  coca-cola — кока-кола, •  mineral water — минеральная вода, •  an ice-cream — мороженое, •  fruit — фрукты ')

#еда средний уровень
    elif message.text == 'еДа 🍉':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('f.png',  'rb'), caption= 'Dairy	Молочные продукты, Grains	Зерна, зерновые, Beans	Фасоль, бобовые, Nuts	Орехи, Meat	Мясо, Seafood	Морепродукты, Dessert	Десерт, Grill	Гриль, блюда гриль, Fry	Жарить, Boil	Варить, Steam	Готовить на пару, Porridge	Каша, Cereal	Хлопья, Oatmeal	Овсянка, Ham	Ветчина, Beef	Говядина, Pork	Свинина, Garlic	Чеснок, Potato	Картофель, Pepper	Перец, Cucumber	Огурец, Carrot	Морковь, Berries	Ягоды, Diet	Диета')

# еда сложно
    elif message.text == 'едА 🍉':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('f.png',  'rb'), caption='Appetizer	Закуска, Cuisine	Кухня, принадлежащая какому-то региону (напр. итальянская кухня), Delicious	Вкусный, Flavour	Вкус, Nutritious	Питательный, Obesity	Ожирение, тучность, Tasteless	Безвкусный, Savoury	Соленая или острая еда (не сладкая), Pickled	Маринованный, Lean	Низкокалорийный, Bake	Выпекать, Casserole	Запеканка, Eggplant	Баклажан, Wheat	Пшеница, Groats	Крупы, Cottage cheese	Творог, Sour cream	Сметана, Noodles	Лапша, Overcooked	Переваренный, Meal	Прием пищи, Dish	Блюдо, Loaf	Буханка хлеба, Poultry	Птица, Dumplings	Пельмени')

#######################################################################################################
# Харктер легко 
    elif message.text == 'ХарактеР🎭':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_message(message.from_user.id, '•	ambitious — честолюбивый, •	amiable — приветливый, •	arrogant — надменный, заносчивый, •	boastful — хвастливый, •	boring — скучный, •	callous — нечуткий, черствый, •	calm — спокойный, •	capricious — капризный, своенравный, •	cheerful (merry) — веселый, жизнерадостный, •	complacent — самодовольный, •	composed — уравновешенный, •	conceited — высокомерный, •	cool — невозмутимый, •	defiant — непокорный, •	easy-going — беззаботный, легкомысленный, •	emotional — эмоциональный, •	envious — завистливый, •	irritable — раздражительный, •	neat — аккуратный, •	obedient — послушный, •	rational — разумный, рациональный, •	self-assured — самоуверенный, •	self-critical — самокритичный, •	self-denying — бескорыстный, •	selfless — самоотверженный, •	sensitive — чувствительный, •	serious — серьезный, •	sloppy — неряха, •	sober-minded — здравомыслящий, •	sullen — угрюмый, мрачный, •	superficial — поверхностный, •	touchy — обидчивый, •	trustworthy — надежный')

#характер средний
    elif message.text == 'Характер🎭':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_message(message.from_user.id, '•	Trait	Черта, Behaviour	Поведение, Loyal	Верный, Talkative	Разговорчивый, Patient	Терпеливый, Naive	Наивный, Mature	Зрелый, Hardworking	Трудолюбивый, Fearless	Бесстрашный, Greedy	Жадный, Mysterious	Загадочный, Ambitious	Честолюбивый, амбициозный, Jealous	Завистливый, ревнивый, Messy	Неряшливый, Adventurous	Авантюрный, Careful	Осторожный, Creative	Креативный, Selfish	Эгоистичный, Timid	Робкий, Intelligent	Умный, Generous	Великодушный, щедрый, Caring	Заботливый, Childish	Ребячливый, Brave	Храбрый ')

#характер сложно
    elif message.text == 'характер🎭':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_message(message.from_user.id, 'Personality	Личность, Personal qualities	Личные качества, Mischievous	Озорной, вредный, Prideful	Горделивый, Carefree	Беззаботный, Open-minded	Открытый, Understanding	Понимающий, Malicious	Злонамеренный, Jack of all trades	Мастер на все руки, Compassionate	Сострадательный, Devoted	Преданный (нап. делу), Witty	Остроумный, Cunning	Коварный, Ruthless	Беспощадный, Reckless	Безрассудный, Courageous	Отважный, Arrogant	Высокомерный, заносчивый, Indifferent	Безразличный, Rebellious	Бунтарь, Modest	Скромный, Short-tempered	Несдержанный, Sincere	Искренний, Passionate	Пылкий, Benevolent	Благожелательный, великодушный ')

#####################################################################################################



####################################################################################
# хоби легко 
    elif message.text == 'ХоббИ🎨':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('hob.jpg',  'rb'), caption='•  collect — собирать, •  collecting — коллекционирование, •  collection — коллекция, •  stamp collection — коллекция марок, •  consist of — состоять из, •  be fond of — увлекаться, •  be proud of — гордиться, •  be interested in — интересоваться, •  be good at — хорошо получаться, •  be keen on — сильно увлекаться, •  be crazy about — обожать, •  have fun — развлекаться, •  have a good time — хорошо проводить время, •  be popular with — быть популярным у, •  exciting — увлекательный, •  expensive — дорогой, •  do nothing — ничего не делать, •  go out – проводить время вне дома, •  stay at home — оставаться дома, •  surf the Internet — сидеть в интернете, •  rest/ have a rest — отдыхать, •  get bored — скучать, •  share pictures / photos — делиться фотографиями, •  play table games (chess, cards, etc.) — играть в настольные игры, •  arrange a party — устроить вечеринку, •  take up —  заняться')

#Хоби средний
    elif message.text == 'ХобБи🎨':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('hob.jpg',  'rb'), caption='Passion	Увлечение, Collecting	Коллекционирование, Knitting	Вязание, Graffiti	Граффити, Skateboarding	Скейтбординг, Parkour	Паркур, Tourism	Туризм, Surfing the Net	Сидеть в интернете, Pottery	Гончарное дело, Baking	Выпечка, Carving	Резьба по дереву, Yoga	Йога, Shopping	Шоппинг, Walking	Ходьба, прогулки, Camping	Кемпинг, Language learning	Изучение языков, Self-education	Самообразование, Table games	Настольные игры, Calligraphy	Каллиграфия, Handicraft	Рукоделие, Blogging	Ведение блога, Hiking	Пеший туризм, Astrology	Астрология, Concerts	Концерты ')

#хоби сложно
    elif message.text == 'хоббИ🎨':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('hob.jpg',  'rb'), caption='Personality	Личность, Personal qualities	Личные качества, Mischievous	Озорной, вредный, Prideful	Горделивый, Carefree	Беззаботный, Open-minded	Открытый, Understanding	Понимающий, Malicious	Злонамеренный, Jack of all trades	Мастер на все руки, Compassionate	Сострадательный, Devoted	Преданный (нап. делу), Witty	Остроумный, Cunning	Коварный, Ruthless	Беспощадный, Reckless	Безрассудный, Courageous	Отважный, Arrogant	Высокомерный, заносчивый, Indifferent	Безразличный, Rebellious	Бунтарь, Modest	Скромный, Short-tempered	Несдержанный, Sincere	Искренний, Passionate	Пылкий, Benevolent	Благожелательный, великодушный')


##############################################################################################################

#ПРОФЕССиИ легкий

    elif message.text == 'ПРОФЕССИи📝':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('prof.jpeg',  'rb'), caption='To work	Работать, Driver	Водитель, Cook	Повар, Doctor	Доктор, Writer	Писатель, Actor	Актер, Engineer	Инженер, Nurse	Медсестра, Teacher	Учитель, Artist	Художник, Pilot	Пилот, Soldier	Солдат, Astronaut	Астронавт, Farmer	Фермер, Miner	Шахтер, Singer	Певец, Musician	Музыкант, Cashier	Кассир  ')

#ПРОФЕССиИ средний
    elif message.text == 'ПРОФЕССиИ📝':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('prof.jpeg',  'rb'), caption='Job	Работа, Priest	Священник, Hairdresser	Парикмахер, Journalist	Журналист, Lawyer	Адвокат, Mayor	Мэр, Judge	Судья, Librarian	Библиотекарь, Scientist	Ученый, Tailor	Портной, Waiter	Официант, Baker	Пекарь, Dentist	Зубной врач, Firefighter	Пожарный, Police officer	Офицер полиции, Waitress	Официантка, Part-time job	Неполная занятость, Wage	Заработная плата, Salary	Зарплата, Employee	Работник, Employer	Работодатель, Politician	Политик, Postman	Почтальон, Architect	Архитектор ')

#ПРОФЕССиИ сложно
    elif message.text == 'ПрОФЕССИИ📝':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('prof.jpeg',  'rb'), caption='Occupation	Род деятельности, профессия, Plumber	Водопроводчик, сантехник, Factory worker	Рабочий, Lifeguard	Спасатель, Real estate agent	Агент по недвижимости, Construction worker	Строитель, Surgeon	Хирург, Unemployment	Безработица, Business owner	Владелец бизнеса, Recruiter	Рекрутер, Labour	Труд, работа, Babysitter	Няня, CEO	Генеральный директор, Chauffeur	Шофер, Bodyguard	Телохранитель, Deliveryman	Курьер, Editor	Редактор, Interpreter	Переводчик (устный), Legal expert	Юридический эксперт, Shop assistant	Консультант (в магазине), Accountant	Бухгалтер, Scriptwriter	Сценарист, TV presenter	Телеведущий, Computer specialist	Компьютерный специалист')


#################################################################################################################################



#Дом легкий

    elif message.text == 'Дом🏠':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('hous.jpg',  'rb'), caption='House	Жилой дом, Flat	Квартира, Room	Комната, Living room	Гостиная, Bathroom	Ванная, Bedroom	Спальня, Kitchen	Кухня, Dining room	Столовая, Garage	Гараж, Sofa	Диван, Bath	Ванна, Bed	Кровать, Table	Таблица, Chair	Кресло, стул, Desk	Письменный стол, Lamp	Лампа, Wall	Стена, Door	Дверь ')

#Дом средний
    elif message.text == 'дОм🏠':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('hous.jpg',  'rb'), caption='Block of flats	Жилой дом, Balcony	Балкон, Armchair	Кресло, Carpet	Ковер, Floor	Пол, этаж, Ceiling	Потолок, Wardrobe	Гардероб, Switch	Переключатель, Shower	Душ, Curtains	Шторы, Mirror	Зеркало, Vase	Ваза, Roof	Крыша, Stairs	Лестница, Fridge	Холодильник, Wallpaper	Обои на стену, Window	Окно, Stove	Плита, Shelf	Полка, Toilet	Туалет, Cupboard	Шкаф, Drawer	Выдвижной ящик, Sink	Раковина, Tap	Кран ')

#Дом сложно
    elif message.text == 'доМ🏠':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('hous.jpg',  'rb'), caption='Alarm clock	Будильник, Oven	Духовой шкаф, Fireplace	Камин, Chest of drawers	Комод, Furniture	Мебель, To move	Переезжать, Upstairs	Вверх по лестнице, Downstairs	Вниз по лестнице, Window sill	Подоконник, Dishwasher	Посудомоечная машина, Vacuum cleaner	Пылесос, Socket	Розетка, Washing machine	Стиральная машина, Dressing table	Туалетный столик, Coffee table	Журнальный столик, Bedside table	Прикроватный столик, Central heating	Центральное отопление, Attic	Чердак, Apartment	Квартира (ам.), Freezer	Морозилка, Stool	Табурет, Cottage	Коттедж, Mansion	Особняк, Water supply	Водоснабжение ')



########################################################################################################

#Спорт легкий

    elif message.text == 'cпорт🏈':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('sport.jpg',  'rb'), caption='Ball	Мяч, Football	Футбол, Basketball	Баскетбол, Foot	Нога, стопа, Basket	Корзина, Play	Играть, Game	Игра, Field	Поле, Match	Матч, Team	Команда, Coach	Тренер, Running	Бег, Swimming	Плавание, Skating	Катание на коньках, Score	Счет, Ring	Ринг, Skiing	Катание на лыжах, Stadium	Стадион')

#Спорт средний
    elif message.text == 'Спорт🏈':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('sport.jpg',  'rb'), caption='Athlete	Спортсмен, Champion	Чемпион, Compete	Соревноваться, Competition	Соревнование, Competitor	Конкурент, Contest	Соревнование, конкурс, Spectator	Зритель, Victory	Победа, Winner	Победитель, Record	Рекорд, Olympics	Олимпийские игры, Marathon	Марафон, Race	Гонка, забег, Sportswear	Спортивная одежда, Cycling	Езда на велосипеде, Training	Тренировка, Climbing	Скалолазание, Diving	Ныряние, Supporter	Болельщик, Referee	Судья, Court	Корт, Strength	Сила, Racket	Ракетка, Gym	Спортзал')

#Спорт сложно
    elif message.text == 'СпорТ🏈':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        item8 = types.KeyboardButton("правило1")
        back = types.KeyboardButton("Назад")
        markup.add(item8, back) 
        bot.send_photo(message.chat.id, photo=open('sport.jpg',  'rb'), caption='Amateur	Любитель, любительский, Defeat	Поражение, Defend	Защищать, Performance	Производительность, эффективность, Athleticism	Атлетизм, Physique	Телосложение, физические данные, Tournament	Турнир, Technique	Техника, Championship	Чемпионат, Contestant	Участник соревнования, Semifinal	Полуфинал, Rhythmic gymnastics	Художественная гимнастика, National team	Национальная сборная, Weightlifting	Тяжелая атлетика, Extreme sports	Экстремальные виды спорта, Martial arts	Боевые искусства, Track-and-field	Легкая атлетика, Workout	Тренировка, Wrestling	Борьба, Pole vault	Прыжки с шестом, Equipment	Экипировка, Racetrack	Беговая дорожка, Stroke	Стиль плавания ')


################################################################################################





    elif message.text == 'инфо🔰':
        
        bot.send_message(message.from_user.id, 'Pазработчики бота 😊 \n При разработке бота была использована библиотека telebot 🌎 \n Бот разработали Самсонова Дарья и Гафурова Диана 🎈 \n 131-21')


  
    


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
