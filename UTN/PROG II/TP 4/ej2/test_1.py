from vinoteca import Vinoteca

class testVinoteca:
    def test():
        vinoteca_1 = Vinoteca()
        vinoteca_2 = Vinoteca()

        if vinoteca_1.venderJugos(4500):
            print (f"Se vendieron jugos correctamente. Quedan {vinoteca_1.obtenerCantidadJugos()} jugos en el deposito")
        else:
            print (f"Se vendieron los jugos que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_1.obtenerCantidadJugos()} jugos en el deposito.")
        
        if vinoteca_2.venderJugos(5500):
            print (f"Se vendieron jugos correctamente, quedan {vinoteca_2.obtenerCantidadJugos()} jugos en el deposito")
        else:
            print (f"Se vendieron los jugos que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_2.obtenerCantidadJugos()} jugos en el deposito.")
        
        vinoteca_1.reponerJugos()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_1.obtenerCantidadJugos()} jugos.")
        vinoteca_2.reponerJugos()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_2.obtenerCantidadJugos()} jugos.")

        if vinoteca_1.venderVinosBLancos(4500):
            print (f"Se vendieron vinos blancos correctamente. Quedan {vinoteca_1.obtenerCantidadVinosBlancos()} vinos blanco en el deposito")
        else:
            print (f"Se vendieron los vinos blancos que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_1.obtenerCantidadVinosBlancos()} vinos blanco en el deposito.")
        
        if vinoteca_2.venderVinosBLancos(5500):
            print (f"Se vendieron vinos blancos correctamente, quedan {vinoteca_2.obtenerCantidadVinosBlancos()} vinos blanco en el deposito")
        else:
            print (f"Se vendieron los vinos blancos que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_2.obtenerCantidadVinosBlancos()} vinos blanco en el deposito.")
        
        vinoteca_1.reponerVinosBlancos()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_1.obtenerCantidadVinosBlancos()} vinos blancos")
        vinoteca_2.reponerVinosBlancos()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_2.obtenerCantidadVinosBlancos()} vinos blancos")


        if vinoteca_1.venderVinosTintosJovenes(4500):
            print (f"Se vendieron vinos tintos jovenes correctamente. Quedan {vinoteca_1.obtenerCantidadVinosTintosJovenes()} vinos tintos jovenes en el deposito")
        else:
            print (f"Se vendieron los vinos tintos jovenes que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_1.obtenerCantidadVinosTintosJovenes()} vinos tintos jovenes en el deposito.")
        
        if vinoteca_2.venderVinosTintosJovenes(5500):
            print (f"Se vendieron vinos tintos jovenes correctamente, quedan {vinoteca_2.obtenerCantidadVinosTintosJovenes()} vinos tintos jovenes en el deposito")
        else:
            print (f"Se vendieron los vinos tintos jovenes que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_2.obtenerCantidadVinosTintosJovenes()} vinos tintos jovenes en el deposito.")
        
        vinoteca_1.reponerVinosTintoJoven()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_1.obtenerCantidadVinosBlancos()} vinos tintos jovenes")
        vinoteca_2.reponerVinosTintoJoven()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_2.obtenerCantidadVinosBlancos()} vinos tintos jovenes")

        if vinoteca_1.venderVinosTintosAnejados(4500):
            print (f"Se vendieron vinos tintos anejados correctamente. Quedan {vinoteca_1.obtenerCantidadVinosTintosAnejados()} vinos tintos anejados en el deposito")
        else:
            print (f"Se vendieron los vinos tintos anejados que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_1.obtenerCantidadVinosTintosAnejados()} vinos tintos anejados en el deposito.")
        
        if vinoteca_2.venderVinosTintosAnejados(5500):
            print (f"Se vendieron vinos tintos anejados correctamente, quedan {vinoteca_2.obtenerCantidadVinosTintosAnejados()} vinos tintos anejados en el deposito")
        else:
            print (f"Se vendieron los vinos tintos anejados que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_2.obtenerCantidadVinosTintosAnejados()} vinos tintos anejados en el deposito.")
        
        vinoteca_1.reponerVinosTintoAnejado()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_1.obtenerCantidadVinosTintosAnejados()} vinos tintos anejados")
        vinoteca_2.reponerVinosTintoAnejado()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_2.obtenerCantidadVinosTintosAnejados()} vinos tintos anejados")


if __name__ == '__main__':
    testVinoteca.test()