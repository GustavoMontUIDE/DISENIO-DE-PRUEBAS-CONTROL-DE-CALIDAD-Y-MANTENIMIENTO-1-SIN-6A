# describe PyDOE3 / ACTS (con fuentes)
# Herramienta utilizada para DOE

Se implementó un generador full-factorial propio en Python usando únicamente:
- itertools.product
- csv
- pathlib

Para combinaciones Pairwise se implementó un algoritmo greedy interno sin dependencias externas.

Esto garantiza:
- Reproducibilidad
- No necesidad de instalar PyDOE2 o allpairs
