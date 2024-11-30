def cargarActividad(archivoActividad):
    try:
        actividad_dict = {}
        with open(archivoActividad, 'r') as f:
            for linea in f:
                usuario, estado = linea.strip().split(';')
                actividad_dict[usuario] = estado
    except FileNotFoundError:
        print(f"El archivo '{archivoActividad}' no existe.")
    return actividad_dict

