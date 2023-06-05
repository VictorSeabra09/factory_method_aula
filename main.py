

class Controlador:
    def __init__(self):
        self.atributo = None


class ControladorCreator:
    def __init__(self):
        self.__controlador_instance = None

    def factory_method(self):
        if self.__controlador_instance is None:
            self.__controlador_instance = Controlador()
        return self.__controlador_instance

# TESTANDO


creator = ControladorCreator()

controlador = creator.factory_method()
controlador2 = creator.factory_method()

print(controlador)
print(controlador2)
