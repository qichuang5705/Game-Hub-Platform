history = [
    {'users': 1, 'score': 200},
    {'users': 2, 'score': 150},
    {'users': 1, 'score': 250},
]

user = {
    1: 'CustomUser: Alice',
    2: '<CustomUser: Bob',
    3: 'CustomUser: Charlie'
}

print(history)
print(user)


for entry in history:
    entry['user'] = user[entry['users']]


print(history)