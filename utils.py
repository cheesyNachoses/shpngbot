from fuzzywuzzy import process, fuzz
#Тут должна быть реализация динамического получения данных с БД
def get_type_list():
    list = ["Верхняя одежда", "Футболки и рубашки", "Худи и свитшоты", "Штаны", "Аксессуары"]
    return list


def get_brand_list():
    list = ["Nike", "Stone Island", "Adidas", "C.P Company", "Louis Vuitton", "Tommy Hilfiger"]
    return list


#Функция для сравнения
def brand_check(message_text):
    brand_list = get_brand_list()
    if message_text in brand_list:
        return [True]
    desired_brand = process.extractOne(message_text, brand_list)
    if desired_brand[1] >= 80:
        return [False, desired_brand[0]]
    else:
        return [False, None]
