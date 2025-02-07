# customers = ["Anna", "Johan", "Erik", "Lisa", "Oskar"]

# for i in customers:
#     print(f"Välkommen {i}!")

# animals = ["Hund", "Katt", "Fågel", "Kanin"]

# for animal in animals:
#     print(f"Jag gillar {animal}!")

# cities = [
#     {"name": "Stockholm", "population": 975551},
#     {"name": "Göteborg", "population": 583056},
#     {"name": "Malmö", "population": 347949},
#     {"name": "Berlin", "population": 3769000},
#     {"name": "London", "population": 8982000},
# ]


# # Din kod här
# for city in cities:
#     if city["population"] > 1000000:
#         print(f"{city['name']} har fler över 1 miljon invånare")


# people = [
#     {"name": "Erik", "age": 25},
#     {"name": "Lisa", "age": 16},
#     {"name": "Johan", "age": 17},
#     {"name": "Oskar", "age": 22},
# ]
# for person in people:
#     if person['age'] < 18:
#         print(f"{person['name']} är under 18 år.")
#     else:
#         print(f"{person['name']} är över 18 år.")

# books = [
#     {"title": "Bok A", "pages": 150},
#     {"title": "Bok B", "pages": 200},
#     {"title": "Bok C", "pages": 300},
#     {"title": "Bok D", "pages": 120}
# ]
# max_pages = -1
# book_max_pages = ""
# for book in books:
#     if book['pages'] > max_pages:
#         max_pages = book["pages"]
#         book_max_pages = book['title']
# print(f"Boken med flest sidor är {book_max_pages}")

# numbers = [5, 12, 3, 20, 8, 15, 10]
# for num in numbers:
#     if num > 10:
#         print(num)

# temperatures = [0, 10, 20, 30, 40]


# for temp in temperatures:
#     fahr = (9 / 5) * temp + 32

#     print(f"{temp} grader Celsius är {fahr} i fahrenheit.")

# names = ["Anna", "Johan", "Erik", "Lisa"]

# # Skriv en loop som hälsar på alla i listan
# for name in names:
#     print(f"Hej, {name}")

# people = [
#     {"name": "Anna", "age": 25},
#     {"name": "Johan", "age": 17},
#     {"name": "Erik", "age": 30},
#     {"name": "Lisa", "age": 16}
# ]
# for person in people:
#     if person['age'] < 18:
#         print(f"{person['name']} är inte vuxen.")
#     else:
#         print(f"{person['name']} är vuxen.")    

books = [
    {"title": "Bok 1", "pages": 150},
    {"title": "Bok 2", "pages": 320},
    {"title": "Bok 3", "pages": 280},
    {"title": "Bok 4", "pages": 350},
    {"title": "Bok 5", "pages": 90},
    {"title": "Bok 6", "pages": 300}
]
for book in books:
    if book["pages"] > 300:
        print(f"{book["title"]} har fler än 300 sidor.",)
    elif book["pages"] == 300:
        print(f"{book["title"]} har exakt 300 sidor.")
    elif book["pages"] < 100 :
        print(f"{book["title"]} är kort.")    
        
    