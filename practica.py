#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola

#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Producto:
    def __init__(self, nombre, unidades, precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio

    def infoProducto(self):

        print(f' El producto con el nombre {self.nombre} tiene {self.unidades} unidades, cuesta {self.precio} €, y tiene {self.unidades*self.precio} de inventario')

producto1=Producto('Camisa verde', 10, 9.95)

producto1.infoProducto()



class Servicio:
    @staticmethod
    def consultarDetalle():
        print('El servicio es básico')


class Estandar(Servicio):
    @staticmethod
    def consultarDetalle():
        print('Este es un método estándar')

class Premium(Servicio):
    @staticmethod
    def consultarDetalle():
        print('Este es un método premium')
servicio1=Premium

opcion=input('Elige un servicio: ')
if opcion=='premium':
    servicio1.consultarDetalle()


