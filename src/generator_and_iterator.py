from files import JSON_FILE_PATH, CSV_FILE_PATH
import csv
import json


books = []
with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        del row["Publisher"]
        books.append(row)


with open(JSON_FILE_PATH, mode='r', encoding='utf-8') as jsonfile:
    users_raw = json.load(jsonfile)


users = []
for user in users_raw:
    filtered_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    users.append(filtered_user)


user_count = len(users)
book_count = len(books)


books_per_user = book_count // user_count
extra_books = book_count % user_count

book_index = 0

for user in users:
    user['books'] = []
    for _ in range(books_per_user):
        if book_index < book_count:
            user['books'].append(books[book_index])
            book_index += 1


for i in range(extra_books):
    if book_index < book_count:
        users[i]['books'].append(books[book_index])
        book_index += 1


with open('result.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(users, jsonfile, indent=4)