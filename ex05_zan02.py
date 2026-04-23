# %%

values = ( 10, 23, 34, 56, 78)

print(f'numbers:{values}')
# %%
print(f'second element: {values[1]}')
# %%
# TypeError: 'tuple' object does not support item assignment
# values[1] = 100
# %%
a, b, c, d, e = values

print(f'a={a},b={b},c={c},d={d},e={e}')

# %%

a, b, *_ = values

print(f'a={a}, b={b}')
# %%

*_, a, b = values

print(f'a={a}, b={b}')

# %%
vals = 1, 2, 3, 4, 5

print(f'values = {vals}')
# %%

vals1 = (100,)

print( type(vals1) )
# %%

print( 2 in vals )
# %%

print( 2 not in vals )

# %%

print( type(vals) is tuple )
# %%
