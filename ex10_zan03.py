value = float(input('Enter a random number:'))
output_txt = ''

if value >= 0:
    output_txt = 'positive'
else:
    output_txt = 'negative'

print(f'value {value} is {output_txt} number, type is {type(value)}')
print('--- end of script ---')