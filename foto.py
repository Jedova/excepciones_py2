from error import DimensionError

class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.ancho = ancho
        self.alto = alto
        self.__ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError("Ancho fuera de rango", dimension=ancho, maximo=self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        if alto < 1 or alto > self.MAX:
            raise DimensionError("Alto fuera de rango", dimension=alto, maximo=self.MAX)
        self.__alto = alto

    @property
    def ruta(self) -> str:
        return self.__ruta
