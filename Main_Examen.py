import random
import csv

alumnos = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"] 

while True:
    try:
        print("1. Inicializar lista de alumnos y creditos")   
        print("2. Otorgar creditos aleatorios")
        print("3. Clasificar creditos")
        print("4. Cálculo de Estadísticas de Créditos: ")
        print("5. Generación de Reporte de Créditos:")
        print("6. Salir")


        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            if not alumnos:
                print("No hay alumnos registrados")
            else:
                print("Creando lista de alumnos y creditos")
                Lista = []
                for alumno in alumnos:
                    Lista.append ({
                        "Nombre": alumno,
                        "Creditos": int
                    })
                print("Lista Creada!")
                print("---------------------------------")

                

        elif opcion == 2:
            if not Lista:
                print("No hay alumnos en la lista")
            else:
                print("Otorgando creditos aleatorios")
                for alumno in Lista:
                    alumno["Creditos"] = random.randint(50, 200)
                print("---------------------------------")



        elif opcion == 3:
            if not Lista:
                print("No hay alumnos en la lista")
            else:
                print("Clasificando creditos")
                for alumno in Lista:
                    if alumno["Creditos"] < 100:
                        alumno["Clasificacion"] = "Bajo Credito"

                    elif alumno["Creditos"] >= 100 and alumno["Creditos"] < 150:
                        alumno["Clasificacion"] = "Medio Credito"
                    
                    else:
                        alumno["Clasificacion"] = "Alto Credito"

            print("---Bajo Credito---")
            for alumno in Lista:
                if alumno["Creditos"] < 100:
                    print(f"{alumno['Nombre']} , {alumno['Creditos']} creditos")

            print("---Medio Credito---")
            for alumno in Lista:
                if alumno["Creditos"] >= 100 and alumno["Creditos"] < 150:
                    print(f"{alumno['Nombre']} , {alumno['Creditos']} creditos")

            print("---Alto Credito---")
            for alumno in Lista:
                if alumno["Creditos"] >= 150:
                    print(f"{alumno['Nombre']} , {alumno['Creditos']} creditos")
            print("---------------------------------")

        elif opcion == 4:

            if not Lista:
                print("No hay alumnos en la lista")
            else:
                print("Calculando estadísticas de créditos")
                print("El menor credito fue de: ", min([alumno["Creditos"] for alumno in Lista]))
                print("El mayor credito fue de: ", max([alumno["Creditos"] for alumno in Lista]))
                print("El promedio de creditos fue de: ", sum([alumno["Creditos"] for alumno in Lista]) / len(Lista))
        
        elif opcion == 5:
            if not Lista:
                print("No hay alumnos en la lista")
            else:
                print("Generando reporte de creditos")
                csv = open("Reporte.csv", "w")
                csv.write("Nombre, Creditos, Clasificacion\n")

                for alumno in Lista:
                    csv.write(f"{alumno['Nombre']}, {alumno['Creditos']}, {alumno['Clasificacion']}\n")
                csv.close()

    except ValueError:
        print("Ingrese una opción válida")
        continue
        