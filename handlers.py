from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State


import kb
import text
import utils
from db import get_unique_id_of_item


router = Router()


class User(StatesGroup):
    choosing_gender = State()
    choosing_size = State()
    first_step_done = State()
    choosing_type = State()
    choosing_brand = State()
    choosing_brand_validation = State()
    retry_choosing_brand = State()
    brand_choosed= State()  #Этот стэйт надо нормально назвать в соответствии с тем, что дальше по логике



@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text.greet.format(name=message.from_user.full_name), reply_markup=kb.menu_main)


@router.message(F.text.lower() == "меню" or F.text.lower() == "menu")
@router.message(F.text == "Выйти в меню")
async def menu_main(message: Message):
    await message.answer(text.menu_main, reply_markup=kb.menu_main)


@router.message(Command("cancel"))
@router.message(F.text.lower() == "cancel" or F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Действия отменены", reply_markup=kb.ReplyKeyboardRemove())


@router.callback_query(F.data.startswith("item_search"))
async def callback_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup()
    action = callback.data.split("_")[2]
    if action == "choice":
        await callback.message.answer(text.gender, reply_markup=kb.make_row_keyboard(kb.genders))
        await state.set_state(User.choosing_gender)
    elif action == "ID":
        # Поиск товара по ID
        #Тут нужно все пересмотреть есть косяки
        await callback.message.answer('Хороший выбор, вводите артикул желаемого товара')
        await state.set_state(User.choosed_id_search)
        item_unique_id = callback.message.text
        result = get_unique_id_of_item()
        if item_unique_id != result:
            await callback.message.answer('Артикул товара введен неправильно')
        else:
            callback.message.answer('Товар успешно добавлен в корзину.\n Продолжаем шоппинг?)')
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
    await message.answer(text=text.user_data, reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(User.first_step_done)
    await message.answer(text=text.logic_fork, reply_markup=kb.logic_fork)


@router.message(User.choosing_size)
async def size_chosen_incorrectly(message: Message):
    await message.answer(text="Размер выбран неправильно", reply_markup=kb.make_row_keyboard(kb.sizes))


@router.callback_query(User.first_step_done, F.data.startswith("filter"))
async def callback_logic_fork(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup()
    action = callback.data.split("_")[1]
    if action == "brand":
        await callback.message.answer(text.brand)
        await state.set_state(User.choosing_brand)
    elif action == "type":
        # Ветка с поиском товара по типу
        await callback.message.answer(text.type, reply_markup=kb.make_row_keyboard(kb.type_list))
        await state.set_state(User.choosing_type)
    await callback.answer()


@router.message(User.choosing_type, F.text.in_(kb.type_list))
async def type_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_type=message.text)
    await message.answer(text=text.type_search, reply_markup=types.ReplyKeyboardRemove())


@router.message(User.choosing_type)
async def type_chosen_incorrectly(message: Message):
    await message.answer(text="Тип выбран неправильно", reply_markup=kb.make_row_keyboard(kb.type_list))


@router.message(User.choosing_brand)
async def brand_chosen(message: Message, state: FSMContext):
    # Проверка введенного текста в сообщении на схожесть с элементами из списка брендов
    suggested_brand = utils.brand_check(message.text)
    await message.answer(text="Происходит поиск бренда",reply_markup=types.ReplyKeyboardRemove())
    if suggested_brand[0]:
        await state.update_data(chosen_brand=suggested_brand)
        await state.set_state(User.brand_choosed)
        await message.answer(text=f"Ваш бренд: {suggested_brand[1]}")
        await message.answer(text="Бренд записан")
    elif len(suggested_brand)>1 and suggested_brand[1] is not None:
        await state.update_data(chosen_brand=suggested_brand)
        await message.answer(text=text.brand_validation, reply_markup=kb.make_row_keyboard(kb.brand_validation))
        await message.answer(text=f"Ваш бренд: {suggested_brand[1]}")
        await state.set_state(User.choosing_brand_validation)
    elif not (suggested_brand[0] and (len(suggested_brand > 1 ) and suggested_brand[1] is not None)):
        await message.answer(text=text.wrong_brand)
        await message.answer(text=text.another_try_ask)
        return

        #Тут надо предложить еще раз попробовать ввести бренд так как мы его не смогли найти

@router.message(User.choosing_brand_validation, F.text.in_(kb.brand_validation))
async def brand_validation(message: Message, state: FSMContext):
    if message.text=="Да":
        await state.set_state(User.brand_choosed)
        await message.answer(text="Отлично, бренд выбран. Перейдем к вещам?", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(text=text.brand_defined_wrong,reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(User.choosing_brand_validation)
        await state.finish()
        await state.set_state(User.choosing_brand)
        #Дописать логику как и в хэндлере выше про предложение о еще одной попытке


@router.message(User.choosing_brand_validation)
async def brand_chosen_incorrectly(message: Message):
    await message.answer(text="Ответ дан неверно", reply_markup=kb.make_row_keyboard(kb.brand_validation))


#Дальше пишется хэндлер для нового стэйта

