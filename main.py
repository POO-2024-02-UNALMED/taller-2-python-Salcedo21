class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos():
        return len(self.asientos)

    def verificarIntegridad():
        
        if (self.registro == motor.registro):
            for asiento in asientos :
                if (asiento.registro != motor.asiento):
                    return "Las piezas no son originales"                      
            return "Auto original"
        else:
            return "Las piezas no son originales"       

class Motor:

    def __init__(self,numerosCilindros,tipo,registro):
        self.numerosCilindros = numerosCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(ente):
        self.registro = ente

    def asignarTipo(tiMotor):
        if tiMotor == "electrico" or tiMotor == "gasolina":
            self.tipo = tiMotor


class Asiento:

    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(stri):
        list_color = ["rojo","verde","amarillo","negro","blanco"]

        if stri in list_color:
            self.color = stri