#main.py: su unica funcion es instanciar el "controlador" y arrancar el programa.

from controlador import ValoAcademyControlador

if __name__ == "__main__":
    app = ValoAcademyControlador(ruta_json="datos.json")
    app.iniciar()