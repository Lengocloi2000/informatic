from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import re

secret_token = '2120664649:AAFLtktUy1Y66dVowXypGEuxSDZ8p7HAFtM'

bot = Bot(token=secret_token)
dp = Dispatcher(bot)
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
   # url = get_url()
   # chat_id = message.migrate_from_chat_id(url)
   # await message.reply_photo(message.chat.id )
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)