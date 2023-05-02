
import wikipedia
import logging

from aiogram import Bot, Dispatcher, executor, types



API_TOKEN = '6046333123:AAG4_Gq1Uj0lXCN65NUVt_5Os19Z1GQ1YO4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /help buyrugi uchun handler yozing
@dp.message_handler(commands="help")
async def yordamchi_help(message:types.Message):
    await message.answer("hello qanaqa yordam bera olaman")

#/start komandasi uchun handler
@dp.message_handler(commands="start")
async def select_start(message:types.Message):
    await message.answer(f"hallo @{message.from_user.username} welcom bot me")

#totiqush handlers
wikipedia.set_lang("uz")
@dp.message_handler()
async def echo_handler(message:types.Message):
    try:
        javob=wikipedia.summary(message)
        await message.answer(javob)
    except:
        await message.answer("Bunday ma'lumot topolmadi boshqa xabar yozing")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)