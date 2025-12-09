"""
binary_search.py
Implementación clásica de búsqueda binaria.

Devuelve:
- índice del elemento si se encuentra
- -1 si no existe en la lista

Esta versión es completamente correcta y será usada para:
1) Medir cobertura inicial (con test_binary_initial.py)
2) Aumentar cobertura (con test_binary_improved.py)
3) Comparar contra la versión defectuosa en análisis estático
"""

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        value = arr[mid]

        if value == target:
            return mid
        elif value < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


if __name__ == "__main__":
    # Prueba manual rápida
    data = [1, 3, 5, 7, 9]

    print("Buscar 7 →", binary_search(data, 7))  # 3
    print("Buscar 2 →", binary_search(data, 2))  # -1
