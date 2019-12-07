class Number:
    def __init__(self, value):
        print('Metoda init wywołana')
        self.value = value
    def wyzeruj(self):
        self.value = 0
    def ustaw(self, value):
        self.value = ustaw


numer = Number(2)
numer.wyzeruj()
numer.ustaw(9)
print(numer.value)





