import json
from csv import DictReader

with open("data/users.json", "r", encoding='utf-8') as file_json:
    users = json.loads(file_json.read())

with open('data/books.csv', newline='', encoding='utf-8') as file_csv:
    reader = DictReader(file_csv)
    iter_user = iter(users)
    for book in reader:
        try:
            current_user = next(iter_user)
        except StopIteration:
            iter_user = iter(users)
            current_user = next(iter_user)

        if "books" not in current_user:
            current_user["books"] = []

        current_user["books"].append({"title": book["Title"],
                                      "author": book["Author"],
                                      "pages": int(book["Height"]),
                                      "genre": book["Genre"]
                                      })

data = []
for user in users:
    data.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": book
    })

with open("data/result.json", "w", encoding='utf-8') as file:
    result = json.dumps(data, indent=4)
    file.write(result)
