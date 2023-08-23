from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu_main)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def menu_main(msg: Message):
    await msg.answer(text.menu_main, reply_markup=kb.menu_main)


@router.callback_query(F.data.startswith == "item_search")
async def callback_main_menu(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    if action == "ID":
        #Ветка с поиском товара по ID
    elif action == "choice":
        #Ветка с выбором товара
    await callback.answer()


