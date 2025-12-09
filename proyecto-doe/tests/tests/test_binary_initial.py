"""
test_binary_initial.py
Conjunto inicial de pruebas para medir cobertura básica del algoritmo
binary_search.py antes de mejorarla.
"""

from src.binary_search import binary_search


def test_found_beginning():
    """
    Caso básico:
    - El target está en la primera posición.
    - Se cubre una ruta simple del algoritmo.
    """
    assert binary_search([1, 2, 3], 1) == 0


def test_found_end():
    """
    Caso básico:
    - El target está en la última posición.
    """
    assert binary_search([1, 2, 3], 3) == 2


def test_not_found():
    """
    Caso donde el elemento NO está en la lista.
    - Permite cubrir el retorno final (-1).
    """
    assert binary_search([1, 2, 3], 4) == -1
