# %%

st = set([6, 6, 4, 12, 8, 12])

print(f'set={st}')

# %%

st2 = {1, 2, 2, 4, 5, 3}

print(f'set2={st2}')

# %%

st2.add(10)
st2.add(3)

print(f'set2={st2}')
# %%

print(f'st1={st},st2={st2}')

print(f'union:{st | st2}')

print(f'intersect:{st & st2}')

print(f'minus:{st - st2}')
# %%

print(f'st={st}, id={id(st)}')

st.add(2)

print(f'st={st}, id={id(st)}')
# %%
