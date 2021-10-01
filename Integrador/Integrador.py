fact = "/Users/cosettediaz/Documents/GitHub/integrador-a01754693/covidmx_reducido.csv.py"

def casoesp():
    print("Mostrar los casos en un día específicado")

def DatosEstatales():
    print("Mostrar los datos de un estado y el total del estado")

def DatosNacionales():
    print("Mostrar los datos nacionales y el total nacional")


def archivocovid(nombre):

    f = open(nombre, "r")
    a = []
    for i in f:
        x = i.split(",")
        a.append(x)
    return a

def menu(nom):

    while True:
        print("1 : Leer archivo de información Covid en México")
        print("2 : Mostrar los datos nacionales y el total nacional")
        print("3 : Mostrar los datos de un estado y el total del estado")
        print("4 : Mostrar los casos en un día especificado")
        print("5 : Salir")

        R = int(input("Seleccionar una opción: "))

        if R == 5:
            break
        else:
            if R == 1:
                fin = archivocovid(nom)
                print(fin)
            else:
                if R == 2:
                    DatosNacionales()
                else:
                    if R == 3:
                        DatosEstatales()
                    else:
                        if R == 4:
                            casoesp()
