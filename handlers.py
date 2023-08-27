from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State


import kb
import text

router = Router()


class User(StatesGroup):
    choosing_gender = State()
    choosing_size = State()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu_main)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def menu_main(msg: Message):
    await msg.answer(text.menu_main, reply_markup=kb.menu_main)


@router.callback_query(F.data.startswith("item_search"))
async def callback_main_menu(callback: types.CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[2]
    if action == "choice":
        await callback.message.answer(text.gender, reply_markup=kb.make_row_keyboard(kb.genders))
        await state.set_state(User.choosing_gender)
    elif action == "ID":
        # Ветка с поиском товара по ID
        await callback.message.answer("Пока здесь ничего нет")
    await callback.answer()


@router.message(User.choosing_gender, F.text.in_(kb.genders))
async def gender_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_gender=message.text)
    await message.answer(text="Хорошо, теперь выберите размер", reply_markup=kb.make_row_keyboard(kb.sizes))
    await state.set_state(User.choosing_size)


@router.message(User.choosing_gender)
async def gender_chosen_incorrectly(message: Message):
    await message.answer(text="Такого нет!\n\nВыберите из нижеперечисленного:", reply_markup=kb.make_row_keyboard(kb.genders))


@router.message(User.choosing_size, F.text.in_(kb.sizes))
async def size_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_size=message.text)
    user_data = await state.get_data()
    await message.answer(text=(user_data['chosen_gender']+" "+user_data['chosen_size']), reply_markup=kb.ReplyKeyboardRemove())


@router.message(User.choosing_size)
async def size_chosen_incorrectly(message: Message):
    await message.answer(text="Размер выбран неправильно", reply_markup=kb.make_row_keyboard(kb.sizes))
