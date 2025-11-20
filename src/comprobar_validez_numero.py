def comprobar_validez_numero(sudoku):

    MAX_RANGE = len(sudoku) + 1
    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        columna = 0
        while columna < numero_filas:

            if sudoku[fila][columna] not in range (1, MAX_RANGE):

                return False
            
            columna += 1

        fila += 1
            
    return True


