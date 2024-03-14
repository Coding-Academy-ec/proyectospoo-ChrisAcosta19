# Archivo: gestion_proyectos/__main__.py
from gestion_proyectos.equipos.equipo import Equipo
from gestion_proyectos.proyectos.proyecto import Proyecto
from gestion_proyectos.tareas.tarea import Tarea

def main():
    # Crear clientes
    proyecto1 = Proyecto("Agendamientos de Citas Médicas", "Crear una app para reservar citas médicas",
                          "2023-08-01", "2024-06-01")
    proyecto2 = Proyecto("Catálogo de Videojuegos", "Crear una app para ver información sobre videojuegos",
                          "2023-10-05", "2024-07-02")

    # Crear empleados
    equipo1 = Equipo("Deathmachine of Coding", "Jefferson", "2023-08-01")
    equipo2 = Equipo("Los Programadores", "Christopher", "2023-10-01")
    
    # Realizar transacciones
    tarea1 = Tarea("Levantamiento de requerimientos", "Entrevistar al cliente para conocer " +
                   "los requerimientos funcionales y no funcionales", "2024-05-01")
    tarea2 = Tarea("Prototipado de baja resolución", "Crear los wireframes en Figma", "2024-06-12")

    # Mostrar detalles de las transacciones
    print("Proyectos del Equipo 1:")
    print(equipo1)
    print(proyecto1)
    print("Tarea:", tarea1)

    print("\nProyectos del Equipo 2:")
    print(equipo2)
    print(proyecto2)
    print("Tarea:", tarea2)

if __name__ == "__main__":
    main()
