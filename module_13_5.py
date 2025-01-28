from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

bot = Bot(token = api)

dp = Dispatcher(bot, storage = MemoryStorage())

keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
keyboard.row(button1, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = 'Привет!')
async def hello(message):
    await message.answer('Введите команду /start, чтобы начать расчёт килокалорий.')

@dp.message_handler(commands = 'start')
async def start(message):
    await message.answer('Нажмите на кнопку "Рассчитать"', reply_markup = keyboard)

@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Необходимое количество килокалорий (ккал) в сутки для Вас - {calories}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)