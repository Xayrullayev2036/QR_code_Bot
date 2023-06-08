from aiogram.types import ReplyKeyboardMarkup

from bot.button.text import asli, kod_rangi, oqra_fon, original, code_color, background, kodiviy_svet, originalniy, fon, \
    uz, ru, en, new_qr, new_qr_code_uz, change_lang, new_qr_code_en, new_qr_code_ru


def new_cod_qr():
    design = [
        [new_qr]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def color_uz_menu():
    design = [
        [asli],
        [oqra_fon, kod_rangi]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def color_en_menu():
    design = [
        [original],
        [background, code_color]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def color_ru_menu():
    design = [
        [originalniy],
        [fon, kodiviy_svet]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def select_language():
    design = [
        [en, ru],
        [uz]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def new_qr_create_uz():
    design = [
        [new_qr_code_uz],
        [change_lang]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def new_qr_create_en():
    design = [
        [new_qr_code_en],
        [change_lang]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def new_qr_create_ru():
    design = [
        [new_qr_code_ru],
        [change_lang]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
