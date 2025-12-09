

from src.binary_search import binary_search


# --- Casos límite básicos ---

def test_empty_list():
    assert binary_search([], 5) == -1


def test_single_element_found():
    assert binary_search([10], 10) == 0


def test_single_element_not_found():
    assert binary_search([10], 5) == -1


# --- Listas pequeñas: cubrir ramas del while ---

def test_even_list_found():
    arr = [2, 4, 6, 8]  # tamaño par
    assert binary_search(arr, 6) == 2


def test_even_list_not_found():
    arr = [2, 4, 6, 8]
    assert binary_search(arr, 5) == -1


def test_odd_list_found_middle():
    arr = [1, 3, 5]
    assert binary_search(arr, 3) == 1


def test_odd_list_not_found():
    arr = [1, 3, 5]
    assert binary_search(arr, 4) == -1


# --- Extremos de listas ---

def test_first_position():
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 10) == 0


def test_last_position():
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 50) == 4


# --- Pruebas de rango amplio (mejoran cobertura de bucles y ramas) ---

def test_large_list_middle():
    arr = list(range(0, 101))  # 0–100
    assert binary_search(arr, 50) == 50


def test_large_list_low_end():
    arr = list(range(0, 101))
    assert binary_search(arr, 0) == 0


def test_large_list_high_end():
    arr = list(range(0, 101))
    assert binary_search(arr, 100) == 100
