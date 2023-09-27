from fuzzywuzzy import process, fuzz
#Тут должна быть реализация динамического получения данных с БД
def get_type_list():
    list = ["Верхняя одежда", "Футболки и рубашки", "Худи и свитшоты", "Штаны", "Аксессуары"]
    return list


def get_brand_list():
    list = ["Nike", "Stone Island", "Adidas", "C.P Company", "Louis Vuitton", "Tommy Hilfiger"]
    return list


#Функция для сравнения
def brand_check(brand_list, message_text):
    get_brand_list()
    desired_brand = process.extractOne(message_text, list)
    if desired_brand[1] >= 80:
        return desired_brand
    else:
        return None
