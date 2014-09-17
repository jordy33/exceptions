def mistake(name):
    raise Exception(name+" caused exception")


try:
    x=1/0
except ZeroDivisionError:
    print ("Tryed div by zero")
print ("salir")
mistake("error de conexion")
