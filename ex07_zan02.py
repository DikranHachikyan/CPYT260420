# %%
conn = dict(
    host='localhost',
    db='sales',
    port=1521,
    keepalive=True
)

print(f'hostname is {conn["host"]}')
# %%
# JSON - JavaScript Object Notation
user = {
    'firstname': 'Anna',
    'lastname': 'Smith',
    'phone': '111-22-33',
    'age': 35,
    'friends': ['Markus', 'Jane']
}

print(f'Hello, {user["firstname"]} {user["lastname"]}!')
# %%

print(user.keys())
# %%
print(user.values())

# %%

print('age' in user)
# %%
print('Smith' in user.values())

# %%
# KeyError: 'address'
# print(user['address'])
# %%
print(user.get('address'))
# %%
print(user.get('address', 'Bulgaria, Sofia'))

# %%
