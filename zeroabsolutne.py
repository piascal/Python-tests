from liczba import Number

class AbsolutZero(Number):
    def __init__(self):
        self_value = 0
    def __str__(self):
        return 'Jestem zerem!'
    
    def reklama(self):
        print('Zacheta do nauki')

zero = AbsolutZero
print(zero)
