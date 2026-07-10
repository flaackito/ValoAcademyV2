
from modelo import BaseDatos
from vista import ValoAcademyVista


class ValoAcademyControlador:

    def __init__(self, ruta_json: str = "datos.json"):
        self.modelo = BaseDatos(ruta_json)
        self.vista = ValoAcademyVista()

    def iniciar(self):
        if not self.modelo.cargar():
            self.vista.mostrar_error_carga()
            return
        
        self.vista.mostrar_bienvenida()
        self.bucle_principal()

    def bucle_principal(self):
        while True:
            self.vista.motrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                self.manejar_mecanicas()
            elif opcion == "2":
                self.manejar_armas()
            elif opcion == "3":
                self.vista.mostrar_despedida()
                break
            
            else:
                self.vista.mostrar_opcion_invalida()

    def manejar_mecanicas(self):
        self.vista.mostrar_lista_mecanicas(self.modelo.listar_mecanicas())
        seleccion = self.vista.pedir_mecanica()

        mecanica = self.modelo.obtener_mecanica(seleccion)
        if mecanica:
            self.vista.mostrar_mecanica(mecanica)
        else:
            self.vista.mostrar_mecanica_invalida()

    def manejar_armas(self):
        self.vista.mostrar_lista_armas(self.modelo.listar_armas())
        seleccion = self.vista.pedir_arma()

        arma = self.modelo.obtener_arma(seleccion)
        if not arma:
            self.vista.mostrar_arma_invalida()
            return
        
        self.vista.mostrar_arma(arma)

        distancia = self.vista.pedir_distancia()
        consejo = arma.obtener_consejo(distancia)


        if consejo:
            self.vista.mostrar_consejo(distancia, consejo)
        else:
            self.vista.mostrar_distancia_invalida()