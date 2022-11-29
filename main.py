from Moduls.functions import *

if __name__ == '__main__':
    users = read_from_json('users.json')
    books = read_from_csv('books.csv')

    users_object_list = generate_object_users_list(users)
    books_object_list = generate_object_books_list(books)

    users_with_books = distribute_books(books_object_list, users_object_list)

    dict_list = generate_dict_users_list(users_with_books)

    write_to_json(file='result.json', data=dict_list)
