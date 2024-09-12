from automovil import Automovil

class TestAutomovil:

    @staticmethod
    def test():
        auto_1 = Automovil("Ford", "Focus", 2005, 210, 0)
        print(f"El auto es: {auto_1.obtenerMarca()}")

        if auto_1.acelerar(100):
            print(f'El auto aceleró. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print(f'El auto no aceleró mas ya que llegó a su velocidad maxima. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        if auto_1.acelerar(100):
            print(f'El auto aceleró. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print(f'El auto no aceleró mas ya que llegó a su velocidad maxima. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        if auto_1.acelerar(100):
            print(f'El auto aceleró. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print(f'El auto no aceleró mas ya que llegó a su velocidad maxima. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        if auto_1.acelerar(100):
            print(f'El auto aceleró. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print(f'El auto no aceleró mas ya que llegó a su velocidad maxima. Velocidad actual: {auto_1.obtenerVelocidadActual()}')

        if auto_1.desacelerar(100):
            print(f'El auto desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print (f'El auto no desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        if auto_1.desacelerar(100):
            print(f'El auto desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print (f'El auto no desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        if auto_1.desacelerar(100):
            print(f'El auto desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print (f'El auto no desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        if auto_1.desacelerar(100):
            print(f'El auto desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        else:
            print (f'El auto no desacelero. Velocidad actual: {auto_1.obtenerVelocidadActual()}')
        
        auto_1.frenarPorCompleto()
        auto_1.acelerar(120)
        auto_1.frenarPorCompleto()
        print (auto_1.obtenerVelocidadActual())

if __name__ == '__main__':
    TestAutomovil.test()