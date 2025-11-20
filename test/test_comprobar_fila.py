import pytest
from src.comprobar_fila import comprobar_fila
from casos_test import casos_test_sudoku

@pytest.mark.filas_validas
@pytest.mark.parametrize(
    "sudoku, valor_esperado",
    [
        (casos_test_sudoku.correcto, True),
        (casos_test_sudoku.fila_invalida, False),
    ],
)
def test_comprobar_fila (sudoku, valor_esperado):

    assert comprobar_fila (sudoku) == valor_esperado

