from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.button.reply import select_language
from bot.button.text import uz, en, ru
from bot.dispatcher import dp


@dp.message_handler(commands="start")
async def start_handler(msg: types.Message, state: FSMContext):
    await state.set_state("start")
    await msg.answer("Tanlang: ", reply_markup=select_language())


@dp.message_handler(Text(uz), state="start")
async def start_handler_len(msg: types.Message, state: FSMContext):
    await msg.answer(
        f"Assalomu aleykum {msg.from_user.full_name} QR kod yasab beradigan botga xush kelibsiz !!!.\nQR kod yasash kerak bo`lgan ma`lumotni kiriting: ")
    await state.set_state("start_function")


@dp.message_handler(Text(en), state="start")
async def start_handler_len(msg: types.Message, state: FSMContext):
    await msg.answer(
        f"Assalomu aleykum {msg.from_user.full_name} welcome to the QR code generator bot !!!.\nEnter the information you need to create a QR code: ")
    await state.set_state("start_en_function")


@dp.message_handler(Text(ru), state="start")
async def start_handler_len(msg: types.Message, state: FSMContext):
    await msg.answer(
        f"Ассалому алейкум {msg.from_user.full_name} добро пожаловать в бота-генератор QR-кода !!!.\nВведите информацию, необходимую для создания QR-кода: ")
    await state.set_state("start_ru_function")
