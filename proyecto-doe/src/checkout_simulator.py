def simulate_checkout(case: dict):
    cliente = case.get("tipo_cliente")
    pago = case.get("metodo_pago")
    dispositivo = case.get("dispositivo")
    red = case.get("estado_red")
    region = case.get("region_fiscal")
    envio = case.get("envio")  # opcional

    
    if red == "SinConexion":
        return False, "Falló por falta de conexión"

    if cliente == "Invitado" and pago in ("Transferencia", "Cripto"):
        return False, "Invitado no puede usar ese método de pago"

    if region == "US" and pago == "Contraentrega":
        return False, "Contraentrega no disponible en US"

    
    return True, "Checkout exitoso"
