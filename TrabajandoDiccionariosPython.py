# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Verificar si la clave "profesion" existe, si no, agregarla
if "profesion" not in informacion_personal:
    informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
