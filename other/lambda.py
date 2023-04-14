#Anonym function

double = lambda a: a * 2

print(double(2))
print((lambda x: x + 1)(2))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

print(full_name("Maki", "Majom"))

capitalize = lambda string: string.upper()

#Nested lambda
print(capitalize(full_name("Maki", "Majom")))
#Invoke direclty
print((lambda string: string.upper())(full_name("Maki", "Majom")))

string_reverse = lambda s: s[::-1]
print(string_reverse("Maki Majom"))

print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))
print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
print(sorted_ids)

#Sorting the list based on the integers
ids = ["pek-23", "muki-45", "profi-11","hkjjkhjsafadsf-2"]
#The lambda function extracts the integer from the string and pass it to the sorted method
sorted_ids = sorted(ids, key=lambda string: int(string.split("-")[1]))
print(sorted_ids)

users = {
    "computer": 2,
    "user": 100
}

print(sorted(users.items(), key=lambda x: x[1], reverse=True))