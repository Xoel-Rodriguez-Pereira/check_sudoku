
if __name__ != '__main__':
    import sys
    sys.path.append('src')

from comprobar_columna import comprobar_columna
from comprobar_fila import comprobar_fila
from comprobar_cuadrado import comprobar_cuadrado
from comprobar_validez_numero import comprobar_validez_numero


def check_sudoku(sudoku):

    return comprobar_cuadrado(sudoku) and comprobar_validez_numero(sudoku) and comprobar_fila(sudoku) and comprobar_columna(sudoku)


