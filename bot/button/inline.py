from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_color_en_menu():
    design = [
        [InlineKeyboardButton("⬜️White",callback_data="white"),InlineKeyboardButton("🟨Yellow",callback_data="yellow")],
        [InlineKeyboardButton("⬛️Black",callback_data="black"),InlineKeyboardButton("🟥Red",callback_data="red")],
        [InlineKeyboardButton("🟪Pink",callback_data="pink"),InlineKeyboardButton("🟧Orange",callback_data="orange")],
        [InlineKeyboardButton("🟩Green",callback_data="green"),InlineKeyboardButton("🟦Blue",callback_data="blue")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design,row_width=2)
def inline_color_uz_menu():
    design = [
        [InlineKeyboardButton("⬜️Oq",callback_data="white"),InlineKeyboardButton("🟨Sariq",callback_data="yellow")],
        [InlineKeyboardButton("⬛️Qora",callback_data="black"),InlineKeyboardButton("🟥Qizil",callback_data="red")],
        [InlineKeyboardButton("🟪Pushti",callback_data="pink"),InlineKeyboardButton("🟧To'q sariq",callback_data="orange")],
        [InlineKeyboardButton("🟩Yashil",callback_data="green"),InlineKeyboardButton("🟦Ko`k",callback_data="blue")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design,row_width=2)
def inline_color_ru_menu():
    design = [
        [InlineKeyboardButton("⬜️Белый",callback_data="white"),InlineKeyboardButton("🟨Желтый",callback_data="yellow")],
        [InlineKeyboardButton("⬛️Черный",callback_data="black"),InlineKeyboardButton("🟥Красный",callback_data="red")],
        [InlineKeyboardButton("🟪Розовый",callback_data="pink"),InlineKeyboardButton("🟧Оранжевый ",callback_data="orange")],
        [InlineKeyboardButton("🟩Зеленый",callback_data="green"),InlineKeyboardButton("🟦Синий",callback_data="blue")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design,row_width=2)


