import qrcode
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.button.inline import *
from bot.button.reply import *
from bot.button.text import *
from bot.dispatcher import dp

from bot.button.inline import inline_color_uz_menu, inline_color_en_menu, inline_color_ru_menu
from bot.button.reply import color_uz_menu, color_en_menu, color_ru_menu
from bot.button.text import asli, kod_rangi, background, original, code_color, fon, originalniy, kodiviy_svet


@dp.message_handler(state="start_function")
async def create_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file["data"] = msg.text
    await state.set_state("select")
    await msg.answer("Tanlang", reply_markup=color_uz_menu())


# =================================================================================
@dp.message_handler(Text(oqra_fon), state="select")
async def select_color_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Tanlang:", reply_markup=inline_color_uz_menu())
    await state.set_state("uz_color")


@dp.callback_query_handler(state="uz_color")
async def update_color(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as file:
        file["back_color"] = call.data
    await call.message.answer("Muvaffaqiyatli o`zgartirildi")
    file = dict(file)
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    color_back = f"{file.get('back_color')}"
    color_back = str(color_back)
    qr_image = qr.make_image(fill_color="black", back_color=color_back)
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await call.message.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await call.message.answer("Xizmatimizdan foydalanganizngizdan mamnunmiz", reply_markup=new_qr_create_uz())
    file["data"] == None
    await call.message.delete()
    await state.finish()


# ==================================================================================

@dp.message_handler(Text(asli), state="select")
async def select_color_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file['yellow'] = "yellow"
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await msg.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await msg.answer("Xizmatimizdan foydalanganizngizdan mamnunmiz", reply_markup=new_qr_create_uz())
    await msg.delete()
    await state.finish()


# =================================================================
@dp.message_handler(Text(kod_rangi), state="select")
async def select_color_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Tanlang:", reply_markup=inline_color_uz_menu())
    await state.set_state("qr_uz_color")


@dp.callback_query_handler(state="qr_uz_color")
async def update_color(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as file:
        file["fill_color"] = call.data
    file = dict(file)
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    color_back = f"{file.get('fill_color')}"
    color_back = str(color_back)
    qr_image = qr.make_image(fill_color=color_back, back_color="white")
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await call.message.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await call.message.answer("Xizmatimizdan foydalanganizngizdan mamnunmiz", reply_markup=new_qr_create_uz())
    file["data"] == None
    await call.message.delete()
    await state.finish()


# =====================================================================================================
# =====================================================================================================


@dp.message_handler(state="start_en_function")
async def create_en_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file["data"] = msg.text
    await state.set_state("select")
    await msg.answer("Select", reply_markup=color_en_menu())


# =================================================================================
@dp.message_handler(Text(background), state="select")
async def select_color_en_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Select:", reply_markup=inline_color_en_menu())
    await state.set_state("en_color")


@dp.callback_query_handler(state="en_color")
async def update_en_color(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as file:
        file["back_color"] = call.data
    await call.message.answer("Changed successfully")
    file = dict(file)
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    color_back = f"{file.get('back_color')}"
    color_back = str(color_back)
    qr_image = qr.make_image(fill_color="black", back_color=color_back)
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await call.message.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await call.message.answer("We are glad that you are using our service", reply_markup=new_qr_create_en())
    file["data"] == None
    await call.message.delete()
    await state.finish()


# ==================================================================================

@dp.message_handler(Text(original), state="select")
async def select_color_en_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file['yellow'] = "yellow"
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await msg.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await msg.answer("We are glad that you are using our service", reply_markup=new_qr_create_en())
    await msg.delete()
    await state.finish()


# =================================================================
@dp.message_handler(Text(code_color), state="select")
async def select_color_en_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Select:", reply_markup=inline_color_en_menu())
    await state.set_state("en_cod_color")


@dp.callback_query_handler(state="en_cod_color")
async def update_color(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as file:
        file["fill_color"] = call.data
        print(call.data)
    await call.message.answer("Changed successfully")
    file = dict(file)
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    color_back = f"{file.get('fill_color')}"
    color_back = str(color_back)
    qr_image = qr.make_image(fill_color=color_back, back_color="white")
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await call.message.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await call.message.answer("We are glad that you are using our service", reply_markup=new_qr_create_en())
    file["data"] == None
    await call.message.delete()
    await state.finish()


# =========================================================================
# =========================================================================


@dp.message_handler(state="start_ru_function")
async def create_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file["data"] = msg.text
    await state.set_state("select")
    await msg.answer("Выбирать", reply_markup=color_ru_menu())


# =================================================================================
@dp.message_handler(Text(fon), state="select")
async def select_color_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Выбирать:", reply_markup=inline_color_ru_menu())
    await state.set_state("color")


@dp.callback_query_handler(state="color")
async def update_color(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as file:
        file["back_color"] = call.data
    await call.message.answer("Изменено успешно")
    file = dict(file)
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    color_back = f"{file.get('back_color')}"
    color_back = str(color_back)
    qr_image = qr.make_image(fill_color="black", back_color=color_back)
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await call.message.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await call.message.answer("Мы рады, что вы пользуетесь нашим сервисом", reply_markup=new_qr_create_ru())
    file["data"] == None
    await call.message.delete()
    await state.finish()


# ==================================================================================

@dp.message_handler(Text(originalniy), state="select")
async def select_color_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file['yellow'] = "yellow"
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await msg.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await msg.answer("Мы рады, что вы пользуетесь нашим сервисом", reply_markup=new_qr_create_ru())
    await msg.delete()
    await state.finish()


# =================================================================
@dp.message_handler(Text(kodiviy_svet), state="select")
async def select_color_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Выбирать:", reply_markup=inline_color_ru_menu())
    await state.set_state("qr_color")


@dp.callback_query_handler(state="qr_color")
async def update_color(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as file:
        file["fill_color"] = call.data
    await call.message.answer("Изменено успешно")
    file = dict(file)
    data = f"{file.get('data')}"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    color_back = f"{file.get('fill_color')}"
    color_back = str(color_back)
    qr_image = qr.make_image(fill_color=color_back, back_color="white")
    qr_filename = 'qrcode.png'
    qr_image.save(qr_filename)
    await call.message.answer_photo(photo=open(f"{qr_filename}", "rb"))
    await call.message.answer("Мы рады, что вы пользуетесь нашим сервисом", reply_markup=new_qr_create_ru())
    await call.message.delete()
    await state.finish()


@dp.message_handler(Text(new_qr_code_ru))
async def new_qr_handler(msg: types.Message, state: FSMContext):
    await msg.answer(
        "Введите информацию, необходимую для создания QR-кода: ")
    await state.set_state("start_ru_function")


@dp.message_handler(Text(new_qr_code_en))
async def new_qr_handler(msg: types.Message, state: FSMContext):
    await msg.answer(
        "Enter the information you need to create a QR code: ")
    await state.set_state("start_en_function")


@dp.message_handler(Text(new_qr_code_uz))
async def new_qr_handler(msg: types.Message, state: FSMContext):
    await msg.answer(
        "QR kod yasash kerak bo`lgan ma`lumotni kiriting: ")
    await state.set_state("start_function")


@dp.message_handler(Text(change_lang))
async def new_qr_handler(msg: types.Message, state: FSMContext):
    await state.set_state("start")
    await msg.answer("Tanlang: ", reply_markup=select_language())
