from vinoteca import Vinoteca

class testVinoteca:
    def test():
        vinoteca_1 = Vinoteca()
        vinoteca_2 = Vinoteca()

        if vinoteca_1.venderVinosBLancos(5500):
            print (f"Se vendieron vinos correctamente, quedan {vinoteca_1.obtenerCantidadVinosBlancos()} vinos en el deposito")
        else:
            print (f"Se vendieron los vinos que quedaban en el deposito, pero no el total pedido . Quedan un total de {vinoteca_1.obtenerCantidadVinosBlancos()} vinos en el deposito.")
        
        vinoteca_1.reponerVinosBlancos()
        print(f"Luego de reponer, ahora vuelve a haber: {vinoteca_1.obtenerCantidadVinosBlancos()} vinos")

if __name__ == '__main__':
    testVinoteca.test()