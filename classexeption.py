class MiError(Exception):
    def __init__(self, valor):
         self.valor = valor
    def __str__(self):
         return repr(self.valor)

try:
    raise MiError(2*2)
except MyError as e:
    print('Ocurrió mi excepción, valor:', e.encode('utf-8'))
