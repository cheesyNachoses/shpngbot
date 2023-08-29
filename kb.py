from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


menu_main = [
    [InlineKeyboardButton(text="Уже выбрал товар", callback_data="item_search_ID"), InlineKeyboardButton(text="Поиск товара", callback_data="item_search_choice")]
]
logic_fork = [
    [InlineKeyboardButton(text="Выбор по бренду", callback_data="filter_brand"), InlineKeyboardButton(text="Выбор по типу одежды", callback_data="filter_type")]
]
genders = ["М", "Ж"]
sizes = ["XS", "S", "M", "L", "XL", "XXL"]
logic_fork = InlineKeyboardMarkup(inline_keyboard=logic_fork)
menu_main = InlineKeyboardMarkup(inline_keyboard=menu_main)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="menu_main")]])

