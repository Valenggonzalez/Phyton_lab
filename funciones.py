CAPACIDAD = 50

vehiculos = {}

vehiculos_atendidos = 0
recaudacion_total = 0
total_horas = 0

def ingresar_vehiculo():

    patente = input("Ingrese la patente: ")

    if patente in vehiculos:
        print("Error: el vehículo ya se encuentra estacionado.")
        return

    hora_ingreso = int(input("Ingrese la hora de ingreso (0-23): "))

    vehiculos[patente] = hora_ingreso

    print("Vehículo registrado correctamente.")    


def registrar_egreso():
    print("Función registrar egreso")


def mostrar_estacionados():

    if len(vehiculos) == 0:
        print("No hay vehículos estacionados.")
        return

    print("\nVehículos estacionados:")

    for patente in vehiculos:
        print(patente)

def mostrar_disponibles():

    ocupados = len(vehiculos)

    disponibles = CAPACIDAD - ocupados

    print("\nCapacidad total:", CAPACIDAD)
    print("Lugares ocupados:", ocupados)
    print("Lugares disponibles:", disponibles)


def mostrar_estadisticas():
    print("Función mostrar estadísticas")
