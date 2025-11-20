import pytest
from src.comprobar_cuadrado import comprobar_cuadrado
from casos_test import casos_test_sudoku

@pytest.mark.es_cuadrado
@pytest.mark.parametrize(
    "sudoku, valor_esperado",
    [
        (casos_test_sudoku.correcto, True),
        (casos_test_sudoku.no_numeros, True),
        (casos_test_sudoku.no_cuadrado, False),
    ],
)
def test_comprobar_cuadrado (sudoku, valor_esperado):

    assert comprobar_cuadrado(sudoku) == valor_esperado

