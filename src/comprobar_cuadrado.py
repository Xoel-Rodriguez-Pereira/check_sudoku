def comprobar_cuadrado(sudoku):

    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        if len(sudoku[fila]) != numero_filas:

            return False
        
        else:

            fila += 1

    return True
