from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

secret_token = '2144078778:AAERvt6KRV5q-MeslE3cwLZrqC5M3Yue0C4'

bot = Bot(token=secret_token)
dp = Dispatcher(bot)
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    await message.reply_photo(photo=get_url())

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
