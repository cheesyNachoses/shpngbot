from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu_main = [
    [InlineKeyboardButton(text="Уже выбрал товар", callback_data="item_search_ID"), InlineKeyboardButton(text="Поиск товара", callback_data="item_search_choice")]
]
menu_main = InlineKeyboardMarkup(inline_keyboard=menu_main)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="menu_main")]])

