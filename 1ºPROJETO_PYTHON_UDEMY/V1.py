from math import pi
import sys

def help():
     print("""\
            É necessário informar o raio do círculo.
            Sintaxe: {} <raio>""".format(sys.argv[0]))

def circulo(r):
    return pi*float(r)**2

if __name__ == '__main__': 
    if len(sys.argv) < 2:
        help()
    elif not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor númerico')
    else:
        r = sys.argv[1]
        area = circulo(r)
        print('Área do círculo', area)
