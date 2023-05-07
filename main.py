from claseViajero import Viajero
from controladorViajeros import Controlador
from claseMenu import Menu

def test():
    viajeros = Controlador()
    viajeros.cargarDatos()
    numViajero = int(input("Ingrese un numero de viajero: "))
    viajero = viajeros.buscar_viajero(numViajero)
    menu = Menu()
    menu.opciones(viajero)
    #mayCantMill = viajeros.buscarMayor()
    #viajeros.mostrarViajerosMayMillasAcum(mayCantMill)
    instancia1 = Viajero(210, 32875738, "Juan", "Perez", 12500)
    instancia2 = Viajero(212, 45867426, "Pedro", "Lopez", 48000)
    if (instancia1 > instancia2):
        print ("Nombre {} , Millas {}" .format(instancia1.getNombre(), instancia1.getMillasAcum()))
    else:
        print ("Nombre {} , Millas {}" .format(instancia2.getNombre(), instancia2.getMillasAcum()))
    millasAacumular = int(input("Ingrese la cantidad de millas a acumular: "))
    print("Millas antes de acumular: {}" .format(instancia1.getMillasAcum()))
    acumulado = instancia1 + millasAacumular
    print("Millas luego de acumular: {}" .format(acumulado))
    millasAcanjear = int(input("Ingrese la cantidad de millas a canjear: "))
    print("Millas antes de canjear: {}" .format(instancia2.getMillasAcum()))
    canjeado = instancia2 - millasAcanjear
    print("Millas luego de canjear: {}" .format(canjeado))


if __name__ == "__main__":
    test ()