def calcular_descuento(monto_total, porcentaje_descuento=12):
    """
    Calcula el monto del descuento basado en el porcentaje y retorna el descuento aplicado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 200  # Monto total de la compra
monto2 = 500  # Otro monto total de la compra
porcentaje_personalizado = 15  # Porcentaje de descuento personalizado

descuento1 = calcular_descuento(monto1)  # Uso del valor por defecto (12%)
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)  # Uso de un porcentaje personalizado

# Cálculo del monto final después del descuento
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"Compra 1: Monto total: ${monto1}, Descuento: ${descuento1}, Monto final a pagar: ${monto_final1}")
print(f"Compra 2: Monto total: ${monto2}, Descuento: ${descuento2}, Monto final a pagar: ${monto_final2}")
