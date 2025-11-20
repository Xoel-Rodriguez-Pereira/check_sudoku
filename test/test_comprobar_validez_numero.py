import pytest
from src.comprobar_validez_numero import comprobar_validez_numero
from casos_test import casos_test_sudoku

@pytest.mark.es_numero_valido
@pytest.mark.parametrize(
    "sudoku, valor_esperado",
    [
        (casos_test_sudoku.correcto, True),
        (casos_test_sudoku.columna_invalida, True),
        (casos_test_sudoku.no_cuadrado, False),
        (casos_test_sudoku.no_entero, False),
        (casos_test_sudoku.rango_sobrepasado, False),
    ],
)
def test_validez_numero (sudoku, valor_esperado):

    assert comprobar_validez_numero (sudoku) == valor_esperado
