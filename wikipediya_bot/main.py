import logging
import wikipedia

wikipedia.set_lang('uz')

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5822770543:AAG-LTdt9KPlvx6EIAW4MDk-qkQ_d7BXiTY'


wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom wikipediyabotga xush kelibsiz !")


@dp.message_handler(commands=['help','yordam'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bu bot wikipediyadan foydali ma'lumotlarni beradi")



@dp.message_handler()
async def echo(message: types.Message):
    matn = message.text

    try:
        javob = wikipedia.summary(matn)
        await message.answer(javob)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)