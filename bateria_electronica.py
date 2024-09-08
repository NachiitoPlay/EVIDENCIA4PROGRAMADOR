# bateria_electronica.py
class BateriaElectronica:
    def __init__(self, max_volumen, volumen_inicial):
        # Encapsulamiento: Protección de los datos internos
        if max_volumen <= 0:
            raise ValueError("El volumen máximo debe ser mayor que 0")
        self.__max_volumen = max_volumen  # Atributo privado
        
        if volumen_inicial < 0 or volumen_inicial > max_volumen:
            raise ValueError(f"El volumen inicial debe estar entre 0 y {max_volumen}")
        self.__volumen = volumen_inicial  # Atributo privado
        self.__estado = False  # Atributo privado

    # Método para encender la batería (abstracción)
    def encender(self):
        self.__estado = True

    # Método para apagar la batería (abstracción)
    def apagar(self):
        self.__estado = False

    # Método para ajustar el volumen con protección de datos (encapsulamiento)
    def ajustar_volumen(self, volumen):
        if volumen > self.__max_volumen:
            self.__volumen = self.__max_volumen
        elif volumen < 0:
            self.__volumen = 0
        else:
            self.__volumen = volumen

    # Método para mostrar el estado de la batería
    def __str__(self):
        estado_str = "Encendida" if self.__estado else "Apagada"  # Corrección
        return f"Batería Electrónica - Estado: {estado_str}, Volumen: {self.__volumen}"

    # Método para obtener el volumen máximo
    def obtener_max_volumen(self):
        return self.__max_volumen

    # Método para obtener el estado actual
    def obtener_estado(self):
        return self.__estado

    # Getters para acceder a los atributos privados
    def obtener_max_volumen(self):
        return self.__max_volumen

    def obtener_estado(self):
        return self.__estado

    def obtener_volumen(self):
        return self.__volumen