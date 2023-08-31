#Тут должна быть реализация динамического получения данных с БД
def get_type_list():
    list = ["Кофты", "Футболки", "Еще что-то"]
    return list


def get_brand_list():
    list = ["Nike", "Stone Island", "Еще что-то"]
    return list

#Функция для сравнения
def brand_check(brand_list, message_text):
    result_brand = None
