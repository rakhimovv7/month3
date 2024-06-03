from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from logging import basicConfig, INFO
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Товары'),
    types.KeyboardButton('Заказать'),
    types.KeyboardButton('Контакты'),
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

class OrderForm(StatesGroup):
    waiting_for_articul = State()
    waiting_for_contact = State()

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply(f"Здравствуйте, {message.from_user.full_name}!", reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about_us(message: types.Message):
    await message.reply("Tehno-shop - Это магазин смартфонов. Мы открылись в 2024г в городе Ош. В нашем магазине вы можете приобрести смартфон любой модели: iPhone, Samsung, Redmi и другие.")

product_buttons = [
    types.KeyboardButton("Samsung"),
    types.KeyboardButton("iPhone"),
    types.KeyboardButton("Redmi"),
    types.KeyboardButton("Назад")
]
product_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*product_buttons)

@dp.message_handler(text='Товары')
async def all_goods(message: types.Message):
    await message.answer("Вот наши товары", reply_markup=product_keyboard)

@dp.message_handler(text='Samsung')
async def samsung_info(message: types.Message):
    await message.answer_photo('https://3dnews.ru/assets/external/illustrations/2023/05/17/1086907/sm.06.800.jpg')
    await message.reply("Samsung - A54\nЦена - 50000\nАртикул - 13\nПамять - 240GB\nЦвет: черный")

@dp.message_handler(text='Redmi')
async def redmi_info(message: types.Message):
    await message.answer_photo('https://login.kg/image/cache/webp/catalog/new/Phones/Xiaomi/Note%2012%20Pro/1-500x400.webp')
    await message.reply("Redmi - Note 8\nЦена - 10000\nАртикул - 15\nПамять - 32GB\nЦвет: белый")

@dp.message_handler(text='iPhone')
async def iphone_info(message: types.Message):
    await message.answer_photo('https://ipiter.ru/upl/modules/shop/360/2q29vzo5ry.jpg')
    await message.reply("iPhone - 15 Pro Max\nЦена - 155900\nАртикул - 56\nПамять - 1TB\nЦвет: черный")

@dp.message_handler(text="Назад")
async def back_to_start(message: types.Message):
    await message.reply("Вы вернулись в главное меню", reply_markup=start_keyboard)

@dp.message_handler(text='Заказать')
async def order(message: types.Message):
    await message.reply("Пожалуйста, введите артикул товара, который хотите заказать:")
    await OrderForm.waiting_for_articul.set()

@dp.message_handler(state=OrderForm.waiting_for_articul)
async def process_articul(message: types.Message, state: FSMContext):
    await state.update_data(articul=message.text)
    await message.reply("Пожалуйста, поделитесь вашим контактом", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton("Поделиться контактом", request_contact=True)))
    await OrderForm.waiting_for_contact.set()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=OrderForm.waiting_for_contact)
async def process_contact(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    articul = user_data['articul']
    contact = message.contact.phone_number
    user_name = message.contact.full_name

    order_message = f"Новый заказ!\nАртикул: {articul}\nКонтакт: {contact}\nИмя: {user_name}"
    await bot.send_message(chat_id=-4269502098, text=order_message)

    await message.reply("Спасибо за заказ! Мы свяжемся с вами в ближайшее время.", reply_markup=start_keyboard)
    await state.finish()

@dp.message_handler(text='Контакты')
async def send_contact(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, вот наши контакты:')
    await message.answer_contact(phone_number="+996552847773", first_name="Tehno-shop")

# executor.start_polling(dp, skip_updates=True)


from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from logging import basicConfig, INFO
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

class OrderForm(StatesGroup):
    waiting_for_articul = State()
    waiting_for_contact = State()
    
start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Товары'),
    types.KeyboardButton('Заказать'),
    types.KeyboardButton('Контакты')
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

class OrderForm(StatesGroup):
    waiting_for_articul = State()
    waiting_for_contact = State()

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply(f"Здравствуйте, {message.from_user.full_name} !",
    reply_markup=start_keyboard)
    

@dp.message_handler(text = 'О нас')
async def text(message:types.Message):
    await message.reply('Tehno-shop - это онлайн магазин по продаже смартфонов')


courses = [
    types.KeyboardButton("iphone-15"),
    types.KeyboardButton("iphone-14"),
    types.KeyboardButton("iphone-13"),
    types.KeyboardButton("iphone-12"),
    types.KeyboardButton("iphone-11"),
    # types.KeyboardButton("Заказать", request_contact=True),
    types.KeyboardButton("Назад")
]

courses_keyboar = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses)

@dp.message_handler(text = 'Товары')
async def kurs(message:types.Message):
    await message.answer("Вот наши товары ", reply_markup=courses_keyboar)

@dp.message_handler(text='iphone-15')
async def iphone_15(messge:types.Message):
    await messge.answer('Описание.\n iPhone 15 Pro: новый король смартфонов с инновационными функциями! Встречайте мощный и стильный iPhone с передовыми технологиями! Представляем iPhone 15 Pro, новый флагман Apple, который изменит ваше представление о смартфонах. Он оснащен OLED-дисплеем с диагональю 6.1 дюйма и технологией Super Retina XDR для непревзойденной цветопередачи и яркости. В основе iPhone 15 Pro лежит мощнейший процессор A17 Pro, который гарантирует молниеносное быстродействие и плавную работу при любых нагрузках. Тройная камера с оптической стабилизацией обеспечивает потрясающие снимки и кинематографические видео. Технология Face ID гарантирует быструю и безопасную аутентификацию.\nАртикул - 15\nЦена телефона состовляет от 90.000 до 125.000 сомов')
    await messge.reply_photo('https://www.gizbot.com/img/2023/07/iphone-jp11-1688538115.jpg')

@dp.message_handler(text='iphone-14')
async def iphone_14(message:types.Message):
    await message.reply('Описание.\n Тонкий и легкий смартфон из новой линейки Apple iPhone 14 с высоким разрешением OLED-экрана, хорошим объемом памяти и запасом автономности во влагостойком корпусе. Продвинутые камеры позволят снимать фото и видео в отличном качестве даже при слабом освещении. Функция экстренной помощи со связью через спутник выручит, когда нет возможности выйти в интернет. Мощный процессор откроет новые возможности для игр и развлечений.\nАртикул - 14\nЦена телефона состовляет от 75.000 до 100.000 сомов')
    await message.reply_photo('https://ismartfon.ru/wp-content/uploads/2022/11/iphone-14-fiolet-6-1.png')

@dp.message_handler(text='iphone-13')
async def iphone_13(message:types.Message):
    await message.reply('Описание.\n Наша самая совершенная система двух камер. Особый взгляд на прочность дисплея. Чип, с которым всё супербыстро. Аккумулятор держится заметно дольше.iPhone 13 - сильный мира всего. Мы разработали совершенно новую схему расположения и развернули объективы на 45 градусов. Благодаря этому внутри корпуса поместилась наша лучшая система двух камер с увеличенной матрицей широкоугольной камеры. Кроме того, мы освободили место для системы оптической стабилизации изображения сдвигом матрицы. И повысили скорость работы матрицы на сверхширокоугольной камере.Новая сверхширокоугольная камера видит больше деталей в тёмных областях снимков. Новая широкоугольная камера улавливает на 47% больше света для более качественных фотографий и видео. Новая оптическая стабилизация со сдвигом матрицы обеспечит чёткие кадры даже в неустойчивом положении.\nАртикул -13\nЦена телефона состовляет от 65.000 до 90.000 сомов')
    await message.reply_photo('https://appleinsider.ru/wp-content/uploads/2021/09/qa.jpg')

@dp.message_handler(text='iphone-12')
async def iphone_12(message:types.Message):
    await message.reply('Описание.\nApple iPhone 12 — ультрамощный смартфон от престижного бренда. Девайс получил молниеносный процессор A14 Bionic и впечатляющий дисплей Super Retina XDR от края до края. Набор продвинутых камер эффективно работает даже в условиях слабого освещения. Видеоролики Dolby Vision завораживают реалистичностью. Фотовозможности гаджета колоссальны. Широкоугольный датчик теперь улавливает значительно больше света. Проработка нюансов очень точная днем и ночью. Портретный режим обеспечивает художественное размытие фона, выделяя самое главное. Смартфон объединяет прорывные возможности с легендарным дизайном. Apple iPhone 12 это выбор активного пользователя\nАртикул - 12\nцена состовляет от 28.000 до 40.000 сомов.')
    await message.reply_photo('https://avatars.mds.yandex.net/i?id=9d8e71c320aa8a6d61898facf9d4b62bc4274fb1-12385820-images-thumbs&n=13')

@dp.message_handler(text='iphone-11')
async def iphone_11(messge:types.Message):
    await messge.reply('Описание.\nФункциональный и стильный смартфон Apple iPhone 11 в металлическом корпусе способен обеспечить не только повседневное общение и развлечения, но и продуктивную работу. Для этого он оснащен мощным процессором Apple A13 Bionic из 6 ядер, поддерживающим слаженную работу всех комплектующих, а также модулем ОЗУ объемом в 4 ГБ, что предусматривает быстрое переключение между открытыми приложениями и возможность играть в игры. Основная (12;12 Мп) и фронтальная (12 Мп) камеры позволят создавать фотошедевры. Изображение на экране смартфона Apple iPhone 11 диагональю 6.1 дюйма обладает поразительной детализацией и цветопередачей. Олеофобное покрытие исключает сильное загрязнение экрана. Корпус смартфона имеет высокую степень пылевлагозащиты (IP68), благодаря чему обеспечивается эффективная и длительная работа устройства. Несъемный аккумулятор емкостью 3110 мА·ч поддерживает беспроводную зарядку, что сделает данный процесс более легким и быстрым\n Артикул - 11 \nЦена состовляет от 20.000 до 28.000 сомов.')
    await messge.reply_photo('https://avatars.mds.yandex.net/i?id=d65254dc84a9af88f4dc0c161e2a9ce0ab0baf9e-12524916-images-thumbs&n=13')

@dp.message_handler(text='Заказать')
async def order(message: types.Message):
    await message.reply("Пожалуйста, введите артикул товара, который хотите заказать:")
    await OrderForm.waiting_for_articul.set()

@dp.message_handler(state=OrderForm.waiting_for_articul)
async def process_articul(message: types.Message, state: FSMContext):
    await state.update_data(articul=message.text)
    await message.reply("Пожалуйста, поделитесь вашим контактом", reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton("Поделиться контактом", request_contact=True)))
    await OrderForm.waiting_for_contact.set()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=OrderForm.waiting_for_contact)
async def process_contact(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    articul = user_data['articul']
    contact = message.contact.phone_number
    user_name = message.contact.full_name

    order_message = f"Новый заказ!\nАртикул: {articul}\nКонтакт: {contact}\nИмя: {user_name}"
    await bot.send_message(chat_id=-4269502098, text=order_message)

    await message.reply("Спасибо за заказ! Мы свяжемся с вами в ближайшее время.", reply_markup=start_keyboard)
    await state.finish()

@dp.message_handler(text='Контакты')
async def send_contact(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, вот наши контакты:')
    await message.answer_contact(phone_number="+996552847773", first_name="Tehno-shop")

@dp.message_handler(text = 'Назад')
async def back(message:types.Message):
    await start(message)

# executor.start_polling(dp)



