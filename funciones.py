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

    global vehiculos_atendidos
    global recaudacion_total
    global total_horas

    patente = input("Ingrese la patente: ")

    if patente not in vehiculos:
        print("Error: vehículo no encontrado.")
        return

    hora_salida = int(input("Ingrese la hora de salida (0-23): "))

    hora_ingreso = vehiculos[patente]

    horas = hora_salida - hora_ingreso

    importe = horas * 1000

    print("Horas de permanencia:", horas)
    print("Importe a pagar: $", importe)

    vehiculos_atendidos += 1
    recaudacion_total += importe
    total_horas += horas

    del vehiculos[patente]

    print("Egreso registrado correctamente.")


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
