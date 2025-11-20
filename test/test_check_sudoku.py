import pytest
from src.check_sudoku import check_sudoku
from casos_test import casos_test_sudoku

@pytest.mark.es_sudoku_valido
@pytest.mark.parametrize(
    "sudoku, valor_esperado",
    [
        (casos_test_sudoku.correcto, True),
        (casos_test_sudoku.columna_invalida, False),
        (casos_test_sudoku.fila_invalida, False),
        (casos_test_sudoku.no_cuadrado, False),
        (casos_test_sudoku.no_entero, False),
        (casos_test_sudoku.lista_vacia, False),
        (casos_test_sudoku.rango_sobrepasado, False),
    ],
)
def test_check_sudoku (sudoku, valor_esperado):

    assert check_sudoku (sudoku) == valor_esperado

# Incendio