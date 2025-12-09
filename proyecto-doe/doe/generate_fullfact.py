# genera matriz DOE con PyDOE3
"""
generate_fullfact.py
Genera matriz full-factorial con los factores definidos.
Salida: reports/doe_fullfact.csv
"""

import csv
from itertools import product
from pathlib import Path

OUT = Path("reports")
OUT.mkdir(exist_ok=True)

FACTORS = {
    "tipo_cliente": ["Nuevo", "Recurrente", "Invitado", "Empresa", "VIP"],
    "metodo_pago": ["Tarjeta", "PayPal", "Transferencia", "Contraentrega", "Cripto"],
    "dispositivo": ["Movil", "Desktop", "Tableta", "SmartTV", "Consola"],
    "estado_red": ["Buena", "Media", "Lenta", "Intermitente", "SinConexion"],
    "region_fiscal": ["LATAM", "EU", "US", "APAC"],
    "envio": ["Economico", "Estandar", "Express", "Pickup"]
}

keys = list(FACTORS.keys())
levels = [FACTORS[k] for k in keys]

output_file = OUT / "doe_fullfact.csv"

with output_file.open("w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for combination in product(*levels):
        writer.writerow(combination)

print(f"Full factorial generado en: {output_file}")
