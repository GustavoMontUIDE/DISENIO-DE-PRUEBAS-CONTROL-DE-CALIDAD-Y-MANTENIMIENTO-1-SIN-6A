"""
binary_search_defective.py

Versión DEFECTUOSA para análisis estático.

Contiene anomalías deliberadas para que pylint y bandit reporten problemas:

ANOMALÍAS DE FLUJO DE DATOS
---------------------------
1. Variable declarada pero NO usada:
      unused_var = 99

2. Actualización incorrecta de 'hi':
      hi = hi - 1
   En lugar de lo correcto:
      hi = mid - 1

3. Retorno incorrecto cuando no se encuentra el elemento:
      return None
   En lugar de retornar -1 (como la versión correcta).

OTRAS ANOMALÍAS / MALAS PRÁCTICAS
----------------------------------
4. Uso inseguro de input() (bandit lo detecta como riesgo):
      user_input = input("Número a buscar: ")

5. Tipado inconsistente: a veces retorna int, otras None.

6. Impresión dentro de la función de biblioteca (mala práctica de diseño).

Este archivo sirve exclusivamente para análisis estático.
"""

from typing import List


def binary_search_defective(arr: List[int], target: int):
    unused_var = 99  # ANOMALÍA 1: variable no usada

    lo = 0
    hi = len(arr) - 1

    # ANOMALÍA EXTRA: mala práctica
    print("Iniciando búsqueda...")  # pylint lo marcará como print innecesario

    while lo <= hi:
        mid = (lo + hi) // 2

        # ANOMALÍA: flujo incorrecto para mover 'hi'
        if arr[mid] > target:
            hi = hi - 1  # ❌ INCORRECTO, debería ser mid - 1

        elif arr[mid] < target:
            lo = lo + 1  # ineficiente pero válido

        else:
            return mid  # caso encontrado

    # ANOMALÍA: retorno inconsistente
    return None  # ❌ debería retornar -1


# ANOMALÍA DETECTABLE POR BANDIT: uso inseguro de input()
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]

    try:
        user_input = input("Número a buscar: ")  # BANDIT marcará este input
        user_input = int(user_input)
    except Exception:
        print("Error procesando entrada")

    print(binary_search_defective(data, user_input))
