# genera casos por pares con allpairspy
"""
"""

import csv
from itertools import product
from pathlib import Path

OUT = Path("reports")
OUT.mkdir(exist_ok=True)

FACTORS = {
    "tipo_cliente": ["Nuevo", "Recurrente", "Invitado, Empresa", "VIP"],
    "metodo_pago": ["Tarjeta", "PayPal", "Transferencia", "Contraentrega", "Cripto"],
    "dispositivo": ["Movil", "Desktop", "Tableta", "SmartTV", "Consola"],
    "estado_red": ["Buena", "Media", "Lenta", "Intermitente", "SinConexion"],
    "region_fiscal": ["LATAM", "EU", "US", "APAC"],
    "envio": ["Economico", "Estandar", "Express", "Pickup"]
}

keys = list(FACTORS.keys())
levels = [FACTORS[k] for k in keys]

# Generar todos los pares a cubrir
pairs = set()
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        for a in levels[i]:
            for b in levels[j]:
                pairs.add(((i, a), (j, b)))

def covered_pairs(case):
    c = set()
    for i in range(len(case)):
        for j in range(i+1, len(case)):
            c.add(((i, case[i]), (j, case[j])))
    return c

testcases = []
remaining = set(pairs)

# Greedy
for candidate in product(*levels):
    new_cov = covered_pairs(candidate) & remaining
    if new_cov:
        testcases.append(candidate)
        remaining -= new_cov
    if not remaining:
        break

output_file = OUT / "pairwise_cases.csv"

with output_file.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for t in testcases:
        writer.writerow(t)

print(f"Pairwise generado en: {output_file}")
#actualizacion