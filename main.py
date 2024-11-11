class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        return len(self.asientos)

    def verificarIntegridad(self):
        
        if (self.registro == Motor.registro):
            for asiento in self.asientos :
                if (asiento.registro != Motor.asiento):
                    return "Las piezas no son originales"                      
            return "Auto original"
        else:
            return "Las piezas no son originales"       

class Motor:

    def __init__(self,numerosCilindros,tipo,registro):
        self.numerosCilindros = numerosCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,ente):
        self.registro = ente

    def asignarTipo(self,tiMotor):
        if tiMotor == "electrico" or tiMotor == "gasolina":
            self.tipo = tiMotor


class Asiento:

    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,stri):
        list_color = ["rojo","verde","amarillo","negro","blanco"]

        if stri in list_color:
            self.color = stri