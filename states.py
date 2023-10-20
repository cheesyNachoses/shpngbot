from aiogram.filters.state import StatesGroup, State


class User(StatesGroup):
    choosing_gender = State()
    choosing_size = State()
    first_step_done = State()
    choosing_type = State()
    choosing_brand = State()
    choosing_brand_validation = State()
    retry_choosing_brand = State()
    step_of_choosing_items = State()
    chose_watching_all_items = State()
    chose_types_after_brand = State()