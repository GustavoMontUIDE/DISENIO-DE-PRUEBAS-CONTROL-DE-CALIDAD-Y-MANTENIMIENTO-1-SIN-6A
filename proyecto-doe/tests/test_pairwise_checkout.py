
"""
test_pairwise_checkout.py
Ejecuta pruebas usando reports/pairwise_cases.csv
y valida reglas de negocio del checkout.
"""

import csv
from pathlib import Path
import pytest

from src.checkout_simulator import simulate_checkout

# ---- Configuración de tipos esperados por columna (ajusta según tu CSV) ----
CASTS = {
    # Ejemplos comunes del proyecto; añade/ajusta los que existan en tu CSV:
    "items_count": int,
    "item_price": float,
    "tax_rate": float,
    # Campos de reglas que mencionaste:
    "estado_red": str,        # 'SinConexion' | 'OK' | etc.
    "tipo_cliente": str,      # 'Invitado' | 'Registrado' | etc.
    "metodo_pago": str,       # 'Tarjeta' | 'Transferencia' | 'Cripto' | ...
    # Otros campos del pairwise:
    "discount_code": str,     # 'NONE' | 'SAVE10' | 'VIP20' (si aplica)
    "shipping_method": str,   # 'standard' | 'express' | 'pickup'
    "payment_method": str,    # 'card' | 'cash' | 'wallet'
    "currency": str,          # 'USD'
}


def _cast_row(row: dict) -> dict:
    """Aplica CASTS por columna si la columna existe en el CSV."""
    casted = {}
    for k, v in row.items():
        v = v.strip() if isinstance(v, str) else v
        caster = CASTS.get(k)
        if caster:
            # Manejo de vacío para numéricos
            if v == "" and caster in (int, float):
                raise ValueError(f"Valor vacío en columna numérica '{k}'")
            casted[k] = caster(v)
        else:
            casted[k] = v
    return casted


def load_cases():
    path = Path("reports/pairwise_cases.csv")
    assert path.exists(), "No existe reports/pairwise_cases.csv — ejecuta doe/generate_pairwise.py"
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for raw in reader:
            yield _cast_row(raw)


@pytest.mark.parametrize("case", list(load_cases()))
def test_pairwise_checkout(case):
    """
    Ejecuta simulate_checkout(case) y valida reglas:
      - Si estado_red == 'SinConexion' => fallo esperado.
      - Si tipo_cliente == 'Invitado' y metodo_pago in ('Transferencia','Cripto') => fallo esperado.
      - Si no aplica ninguna regla prohibitiva => éxito esperado.
    """
    ok, msg = simulate_checkout(case)

    # ---- Reglas de negocio (las que pediste) ----
    if case.get("estado_red") == "SinConexion":
        assert not ok, f"Esperado fallo por SinConexion en {case}. msg={msg}"
        return

    if case.get("tipo_cliente") == "Invitado" and case.get("metodo_pago") in ("Transferencia", "Cripto"):
        assert not ok, f"Invitado no debería poder pagar con {case.get('metodo_pago')}. case={case}, msg={msg}"
        return

    # ---- Si ninguna regla impide la operación, esperamos que pase ----
    assert ok, f"Se esperaba ok para {case}. msg={msg}"
