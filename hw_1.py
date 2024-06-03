# from aiogram import Bot,Dispatcher, types, executor
# import random
# from config import token

# bot = Bot(token=token)
# dp = Dispatcher(bot)

# number = random.randint(1, 3)

# @dp.message_handler(commands='start')
# async def a (message:types.Message):
#     await message.answer("Я загадал число от 1 до 3 угадай")

# @dp.message_handler(text = '1')
# async def a (message:types.Message):
#     if number == 1:
#         await message.reply("Правильно отгадали")
#         await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     elif number != 1:
#         await message.reply("Вы неправильно отгадали")
#         await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')
    
# @dp.message_handler(text = '2')
# async def a (message:types.Message):
#     if number == 2:
#         await message.reply("ПРавильно отгадали")
#         await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     elif number != 2:
#         await message.reply("Вы неправильно отгадали")
#         await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

# @dp.message_handler(text = '3')
# async def a (message:types.Message):
#     if number ==3:
#         await message.reply("ПРавильно отгадали")
#         await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
#     elif number != 3:
#         await message.reply("Вы неправильно отгадали")
#         await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

# executor.start_polling(dp)