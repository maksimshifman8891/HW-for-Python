a = int(input('your income: '))
b = int(input('your costs: '))
if (a > b):
    c = int(a-b)
    print('your profit is:', c)
    # looks that i don't need this step:
    e = a / c
    print('your profitability is:', e)
else:
    d = int(a - b)
    print('your lesion is:', d)

f = int(input('how much employees do you have? '))
if (a >b):
    g = int(c // f)
    print('firm profit per employee: ', g)
else:
    print('it is batter to you to close your company')
