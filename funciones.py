import config, random, csv

def generar_id():
    id = random.randint(100000,999999)
    return id 

def menu():
    op = 1
    while True:
        for opcion in config.lista_opciones:
            print(f"{op}. {opcion}")
            op += 1 
        seleccion = int(input("Ingresa una opcion: "))      
        if seleccion != None:
            break
        else:
            print("Ingrese una opcion valida")
    return seleccion

def registrar_pedido(lista_datos):
    id = generar_id()
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    sector = input("Ingresa tu sector: ")
    direccion = input("Ingresa tu direccion: ")
    disponible_6 = input("Cantidad de cilindros 6 lts.: ")
    disponible_10 = input("Cantidad de cilindros 10 lts.: ")
    disponible_20 = input("Cantidad cilindros 20 lts.: ")

    cliente = [id, nombre, apellido, sector, direccion, disponible_6, disponible_10, disponible_20]
    lista_datos.append(cliente)
    return cliente

def listar_pedidos(lista_datos):
    print("Id. Cliente\tNombre cliente\tSector\tDireccion\tDisp. 6lts\tDisp. 10lts\tDisp. 20lts")    
    for cliente in lista_datos: 
        lista_datos = (f"{id[0]}\t{nombre[1]}\t{apellido[2]}\t{sector[3]}\t{direccion[4]}\t{disponible_6[5]}\t{disponible_10[6]}\t{disponible_20[7]}")

def imprimir_hoja(lista_datos):
    with open ("planilla.csv", "w") as archivo:
        archivo = csv.writer(archivo)
        archivo.writerow("Id. Cliente\tNombre Cliente\tSector\tDireccion\tDisp.6lts\tDisp.10lts\tDisp.20lts")
        for cliente in lista_datos:
            lista_datos = (f"{id[0]}\t{nombre[1]}\t{apellido[2]}\t{sector[3]}\t{direccion[4]}\t{disponible_6[5]}\t{disponible_10[6]}\t{disponible_20[7]}")
        
        return archivo

           

