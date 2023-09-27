import psycopg2
from psycopg2 import Error


def get_unique_id_of_item(item_unique_id):
    try:
        connection = psycopg2.connect(user = '', password = '', host ='', port = '', database = 'postgres_db')
        cursor = connection.cursor()
        postgres_sql_query = 'select item_unique_id from id'
        cursor.execute(postgres_sql_query)
        item_unique_id = cursor.fetchone()
        return item_unique_id
    except (Exception, Error):
        print('В работе с базой данных косяк, скоро пофиксим <3, но все же проверь, вдруг, ты неправильно ввел ID')
        '''В этом файле осталось писать отдельные функции для конкретных действий с бд, скелет одинаковый, просто разные
        запросы, а также необходимо реализовать функцию отправки ошибок на сервак, чтобы уведомляло при смэрти базы'''
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Соединение закрыто')


