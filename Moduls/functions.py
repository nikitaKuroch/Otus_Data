import json
import csv
import os
import random

from Forms.book import Book
from Forms.user import User


def read_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "data/{0}".format(file)), 'r') as f:
        lst = list(json.load(f))
    return lst


def read_from_csv(file):
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "data/{0}".format(file)), 'r') as f:
        file_reader = csv.reader(f, delimiter=",")
        header = next(file_reader)

        res = [dict(zip(header, row)) for row in file_reader]
    return res


def write_to_json(file, data):
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "data/{0}".format(file)), 'w') as out:
        json.dump(data, out, indent=4)


def generate_object_users_list(dict_users_list):
    if not isinstance(dict_users_list, list):
        raise ValueError(f'Аргуметр "{dict_users_list}" должен быть в формате списка.')

    return [
        User(name=user['name'], age=user['age'], gender=user['gender'], address=user['address'])
        for user in dict_users_list
    ]


def generate_object_books_list(dict_books_list):
    if not isinstance(dict_books_list, list):
        raise ValueError(f'Аргуметр "{dict_books_list}" должен быть в формате списка.')

    return [
        Book(title=book['Title'], author=book['Author'], genre=book['Genre'], pages=book['Pages'])
        for book in dict_books_list
    ]


def generate_dict_users_list(object_users_list):
    if not isinstance(object_users_list, list):
        raise ValueError(f'Аргуметр "{object_users_list}" должен быть в формате списка.')
    return [user.__dict__ for user in object_users_list]


def distribute_books(books_list, users_list):
    if not isinstance(books_list, list) or not isinstance(users_list, list):
        raise ValueError('Аргуметры должны быть в формате списка.')

    for _ in books_list:
        for user in users_list:
            if len(books_list) == 0:
                break
            book = random.choice(books_list)
            user.books += [book.__dict__]
            books_list.remove(book)
    return users_list
