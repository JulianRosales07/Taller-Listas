import os
"""
Taller presentado por Julian David Rosales y Juan Diego Botina Realpe
"""
def crear_archivo_estudiantes():
    """
    Creamos el archivo 'estudiantes.txt' con datos ingresados por el usuario si no existe.
    """
    if not os.path.exists("estudiantes.txt"):
        print("El archivo 'estudiantes.txt' no existe.")
        print("Vamos a crearlo con datos iniciales.")
        estudiantes = []
        while True:
            nombre = input("Ingrese el nombre del estudiante (o 'fin' para finalizar):")
            if nombre.lower() == 'fin':
                break
            comida = input("Elija la opcion de comida (Pizza o Hamburguesa):")
            while comida not in ['Pizza', 'Hamburguesa']:
                comida = input("Opcion invalida, Elija Pizza o Hamburguesa:").upper()
            bebida = input("Eija la opcion de bebida (Jugo natural o Gaseosa):")
            while bebida not in ['Jugo natural', 'Gaseosa']:
                bebida = input("Opcion invalida, Elija Jugo natural o Gaseosa:").upper()
            estudiantes.append(f"{nombre};{comida};{bebida}")
            print(f"Estudiante {nombre} agregado.")
        with open("estudiantes.txt", 'w') as archivo:
            for estudiante in estudiantes:
                archivo.write(f"{estudiante}\n")
        print("Archivo 'estudiantes.txt' creado con los datos ingresados." )
    else:
        print("El archivo 'estudiantes.txt' ya existe." )

def leer_archivo(nombre_archivo):
    """
    lee el archivo de estudiantes y retorna una lisa con los datos.
    """

    estudiantes = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                if len(datos) == 3:
                    nombre, comida, bebida = datos
                    estudiantes.append((nombre, comida, bebida))
                    print(f"Estudiante {nombre} leido.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no e encontro.")
    return estudiantes

def guardar_estudiantes(estudiantes, nombre_archivo):
    """
    Guarda la lista de estudiantes en el archivo.
    """

    with open(nombre_archivo, 'w') as archivo:
        for estudiante in estudiantes:
            archivo.write(f"{estudiante[0]};{estudiante[1]};{estudiante[2]}\n")
            print(f"Estudiante {estudiante[0]} guardado.")

def registrar_estudiantes(estudiantes):
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar):")
        if nombre.lower() == 'fin' :
            break
        comida = input("Elija la opcion de comida ('Pizza' o 'Hamburguesa') (o 'fin' para terminar):")
        if comida.lower() == 'fin' :
            break
        bebida = input("Elija la opcion de bebida ('Jugo natural' o 'Gaseosa') (o 'fin' para terminar):")
        if bebida.lower() == 'fin' :
            break
        estudiantes.append((nombre, comida, bebida))
        print(f"Estudiante {nombre} agregado.")
    return estudiantes

def ver_lista_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\nLista de estudiantes inscritos:")
        for i, (nombre, comidas, bebidas) in enumerate(estudiantes, 1):
            print(f"{i}. {nombre}. comida: {comidas}, bebida: {bebidas}")

def calcular_comidas_y_bebidas(estudiantes):
    comida_Pizza = comida_Hamburguesa = bebida_Jugo = bebida_Gaseosa = 0
    for _, comidas, bebidas in estudiantes:
        if comidas == 'Pizza':
            comida_Pizza += 1
        else:
            comida_Hamburguesa += 1
        if bebidas == 'Jugo natural':
            bebida_Jugo += 1
        else:
            bebida_Gaseosa += 1
    return comida_Pizza, comida_Hamburguesa, bebida_Jugo, bebida_Gaseosa

def generar_reporte(estudiantes, nombre_reporte):
    if not estudiantes:
        print(f"No hay estudiantes registrados para generar el informe.")
        return
    total_estudiantes = len(estudiantes)
    comida_Pizza, comida_Hamburguesa, bebida_Jugo, bebida_Gaseosa = calcular_comidas_y_bebidas(estudiantes)

    with open(nombre_reporte, 'w') as archivo:
        archivo.write("--- Informe Final ___\n")
        archivo.write(f"Total de estudiantes inscritos: {total_estudiantes}\n")
        archivo.write(f"Cantidad de comida opcion Pizza: {comida_Pizza}\n")
        archivo.write(f"Cantidad de comida opcion Hamburguesa: {comida_Hamburguesa}\n")
        archivo.write(f"Cantidad de bebida opcion Jugo natural: {bebida_Jugo}\n")
        archivo.write(f"Cantidad de bebida opcion Gaseosa: {bebida_Gaseosa}\n")

        archivo.write("\nEstudiantes por opcion de comida:\n")
        archivo.write("Opcion Pizza:\n")
        for nombre, comida, _ in estudiantes:
            if comida == 'Pizza':
                archivo.write(f"- {nombre}\n")
        archivo.write("\nOpcion Hamburguesa:\n")
        for nombre, comida, _ in estudiantes:
            if comida == 'Hamburguesa':
                archivo.write(f"- {nombre}\n")
        
        archivo.write("\nEstudiantes por opcion de bebida:\n")
        archivo.write("Opcion Jugo natural:\n")
        for nombre, _, bebida in estudiantes:
            if bebida == 'Jugo natural':
                archivo.write(f"- {nombre}\n")
        archivo.write("\nOpcion Gaseosa:\n")
        for nombre, _, bebida in estudiantes:
            if bebida == 'Gaseosa':
                archivo.write(f"- {nombre}\n")
                
    print(f"Informe generado exitosamente en '{nombre_reporte}'.")

def mostrar_menu():
    print("\n--- Menu Principal ---")
    print("1. Registrar estudiantes.")
    print("2. Ver lista de estudiantes.")
    print("3. Generar informe del evento.")
    print("4. Salir.")
    return input("Seleccione una opcion: ")

def main():
    print("Bienvenido al organizador de eventos escolares de la Universidad Mariana.")

    archivo_estudiantes = "estudiantes.txt"
    archivo_informe = "informe_evento.txt"

    crear_archivo_estudiantes()
    estudiantes = leer_archivo(archivo_estudiantes)

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            estudiantes = registrar_estudiantes(estudiantes)
            guardar_estudiantes(estudiantes, archivo_estudiantes)
        elif opcion == '2':
            ver_lista_estudiantes(estudiantes)
        elif opcion == '3':
            generar_reporte(estudiantes, archivo_informe)
        elif opcion == '4':
            print("Gracias por usar el organizador de eventos. ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del menu.")

if __name__ == "__main__":
    main()
