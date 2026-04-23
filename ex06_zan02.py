# %%
arr = [10, 20, 30, 40, 50]

print(f'arr:{arr}, type of arr:{type(arr)}')
# %%

print(f'first element:{arr[0]}')

arr[1] = 15

print(f'arr={arr}')
# %%
print(f'id of arr:{id(arr)}')

arr[2] = 25
arr.append(100)

print(f'id of arr:{id(arr)}')

# %%
values = 11, 22, 33, 44

arr_t = list(values)

print(f'array form tuple:{arr_t}')

# %%
vals = tuple(arr_t)
print(f'vals = {vals}')
# %%
arr_s = list('Hello Python')

print(f'arr from str:{arr_s}')
# %%
