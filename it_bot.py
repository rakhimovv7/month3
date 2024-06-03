from aiogram import Bot, Dispatcher, types, executor
from logging import basicConfig, INFO
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Контакты')
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply(f"Здравствуйте, {message.from_user.full_name} !",
    reply_markup=start_keyboard)

@dp.message_handler(text = 'О нас')
async def text(message:types.Message):
    await message.reply("Geeks - это айти курсы в Оше, Кара-Балте, Бишкеке основанная в 2019 году")

@dp.message_handler(text ='Адрес')
async def adres(message:types.Message):
    await message.reply("Наш адрес: город ОШ, Мырзалы Аматова 1Б (БЦ 'Томирис')")
    await message.reply_location(40.51931846586533, 72.80297788183063)

@dp.message_handler(text ='Контакты')
async def contact(message:types.Message):
    await message.answer(f'{message.from_user.full_name}, вот наши контакты: ')
    await message.answer_contact("+996505180600", "Islam", "Toksonbaev")
    await message.answer_contact("+996222226070", "Syimyk", "Abdykadyrov")

courses = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("Ux/Ui"),
    types.KeyboardButton("Детское программирование"),
    types.KeyboardButton("Основы программирования"),
    types.KeyboardButton("Оставить заявку", request_contact=True),
    types.KeyboardButton("Назад")
]

courses_keyboar = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses)



@dp.message_handler(text = 'Backend')
async def backend(message:types.Message):
    await message.reply("Бэкенд-разработчик (backend developer) — это специалист, который занимается серверной частью сайтов, мобильных и десктопных приложений и игр. Он реализует внутреннюю логику работы приложения, обеспечивает его взаимодействие с базами данных и внешними сервисами")

@dp.message_handler(text = 'Frontend')
async def frontend(message:types.Message):
    await message.reply("Фронтенд-разработчики занимаются разработкой графического интерфейса — той части приложений, которую видит пользователь. Они превращают макет, созданный веб-дизайнером, в функциональный и удобный пользовательский интерфейс. Корректное отображение полей и блоков, работающие кнопки и формы для ввода данных — всё, с чем сталкивается пользователь в браузере, находится в зоне ответственности фронтендеров")

@dp.message_handler(text = 'Android')
async def Android(message:types.Message):
    await message.reply("Android-программирование – это разработка программного обеспечения для мобильных устройств, работающих на операционной системе Android. Это включает в себя разработку приложений для смартфонов, планшетов и других устройств на базе Android. Android-платформа основана на программном обеспечении от компании Google, которое включает в себя операционную систему, среду разработки, фреймворк и инструменты")

@dp.message_handler(text = 'Ux/Ui')
async def ux_ui(message:types.Message):
    await message.reply("UX/UI-дизайн — это проектирование удобных, понятных и эстетичных пользовательских интерфейсов.UX (user experience) — это «пользовательский опыт», который включает в себя навигацию по сайту или приложению, состав функций внутри цифрового продукта, понятный текст.UI (user interface) — это пользовательский интерфейс, который включает в себя наполнение сайта, систематизацию элементов, выбор цветов, построение визуальной композиции, оформление кнопок, колонок и других графических элементов.")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def b(message:types.Message):
    await message.answer(message)
    await bot.send_message(-4269502098, f"Заявка на курсы:\nИмя: {message.contact.last_name}\nФамилия: {message.contact.first_name}\nТелефон: {message.contact.phone_number}\n ")

@dp.message_handler(text = 'Назад')
async def back(message:types.Message):
    await start(message)

executor.start_polling(dp)