# Archivo: gestion_proyectos/equipos/equipo.py

class Equipo:
    def __init__(self, nombre, lider, fecha_creacion):
        self.nombre = nombre
        self.lider = lider
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return f"Equipo: {self.nombre}\nLíder: {self.lider}\nFecha creación: {self.fecha_creacion}"
