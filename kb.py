from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

import utils


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


menu_main = [
    [InlineKeyboardButton(text="Знаю номер товара", callback_data="item_search_ID"), InlineKeyboardButton(text="Поиск подходящего товара", callback_data="item_search_choice")]
]
logic_fork = [
    [InlineKeyboardButton(text="Поиск по бренду", callback_data="filter_brand"), InlineKeyboardButton(text="Поиск по типу одежды", callback_data="filter_type")]
]
genders = ["М", "Ж"]
sizes = ["XS", "S", "M", "L", "XL", "XXL"]
brand_validation=["Да", "Нет"]
type_list = utils.get_type_list()
brand_list = utils.get_brand_list()
logic_fork = InlineKeyboardMarkup(inline_keyboard=logic_fork)
menu_main = InlineKeyboardMarkup(inline_keyboard=menu_main)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="menu_main")]])

