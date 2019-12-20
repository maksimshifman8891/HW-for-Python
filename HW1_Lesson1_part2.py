seconds = int(input('give me an integer '))
minutes = (seconds // 60) % 60
hours = (seconds // 3600) % 24
sec1 = seconds % 60
print(f'you have {hours} hours {minutes} minutes and {sec1} seconds to...')

