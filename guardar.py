def guardar_string_en_archivo(mi_string, nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(mi_string)
        print(f"El string se ha guardado en '{nombre_archivo}' con éxito, Mi Señor.")
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")

# Esto te permitirá usar la función desde otro archivo.

def guardar_respuesta_en_archivo_apend(mi_string, nombre_archivo):
    try:
        # Leer el contenido actual del archivo si existe
        contenido_anterior = ""
        try:
            with open(nombre_archivo, "r") as archivo_lectura:
                contenido_anterior = archivo_lectura.read()
        except FileNotFoundError:
            pass
        
        # Concatenar el nuevo string con el contenido anterior
        nuevo_contenido = f"Respuesta N {len(contenido_anterior.split('Respuesta N '))}\n{mi_string}\n\n{contenido_anterior}"
        
        with open(nombre_archivo, "w") as archivo_escritura:
            archivo_escritura.write(nuevo_contenido)
        
        print(f"La respuesta se ha guardado en '{nombre_archivo}' con éxito, Mi Señor.")
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")
