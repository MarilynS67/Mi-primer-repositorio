# Escritura de Archivo de Texto
# Creamos y abrimos el archivo en modo escritura ('w')
with open("my_notes.txt", "w") as file:
    file.write("1. Estudiar Python todos los días.\n")
    file.write("2. Practicar ejercicios de programación.\n")
    file.write("3. Aprender sobre redes y ciberseguridad.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leemos y mostramos cada línea del archivo
    for line in file:
        print(line.strip())  # strip() elimina espacios en blanco o saltos de línea adicionales

# No es necesario cerrar el archivo manualmente ya que 'with open' maneja el cierre automáticamente
