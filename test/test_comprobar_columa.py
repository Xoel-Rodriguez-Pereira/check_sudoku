import pytest
from src.comprobar_columna import comprobar_columna
from casos_test import casos_test_sudoku

@pytest.mark.columnas_validas
@pytest.mark.parametrize(
    "sudoku, valor_esperado",
    [
        (casos_test_sudoku.correcto, True),
        (casos_test_sudoku.columna_invalida, False),
    ],
)
def test_comprobar_columna (sudoku, valor_esperado):

    assert comprobar_columna(sudoku) == valor_esperado

