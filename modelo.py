import json

class Mecanica:

    # CAMBIA 'description' por 'descripcion' aquí:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"[{self.nombre.upper()}]\n{self.descripcion}"
    
class Arma:

    def __init__(self, nombre: str,tipo: str, costo: int, dano: dict, consejo: dict):
        self.nombre = nombre
        self.tipo = tipo
        self.costo = costo
        self.dano = dano
        self.consejo = consejo
    
    def __str__(self):
        return f"{self.nombre.upper()} - {self.tipo} | {self.costo} creditos"

#Clase para gestionar la carga del JSON

class BaseDatos:
    def __init__(self, ruta_archivo: str = "datos.json"):
        self.ruta_archivo = ruta_archivo
        self.mecanicas: dict[str, Mecanica] = {}
        self.armas: dict[str, Arma] = {}

#Funcion para cargar el JSON

    def cargar(self) -> bool:
        try:
            with open(self.ruta_archivo,"r", encoding="utf-8") as archivo:
                datos_crudos = json.load(archivo)
        
        except FileNotFoundError:
            return False
        except json.JSONDecodeError:
            return False
    
        #Construir mecánicas
        for nombre, descripcion in datos_crudos.get("mecanicas", {}).items():
            self.mecanicas[nombre] = Mecanica(nombre, descripcion)

        #Construir armas
        for nombre, info in datos_crudos.get("armas", {}).items():
            self.armas[nombre] = Arma( 
                nombre=nombre,
                tipo=info.get("tipo", "Desconocido"),
                costo=info.get("costo", 0),
                dano=info.get("dano", {}),
                consejo=info.get("consejo", {}),
            )
        
        return True
    

    def obtener_mecanica(self, nombre: str):
        return self.mecanicas.get(nombre.lower())
    
    def obtener_arma(self, nombre: str):
        return self.armas.get(nombre.lower())
    
    def listar_mecanicas(self):
        return list(self.mecanicas.keys())
    
    def listar_armas(self):
        return list(self.armas.keys())