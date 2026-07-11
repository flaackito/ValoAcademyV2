from flask import Flask, jsonify, render_template, request
from modelo import BaseDatos

class ValoAcademyControlador:
    def __init__(self, ruta_json: str = "datos.json"):
        self.modelo = BaseDatos(ruta_json)
        self.app = Flask(__name__, template_folder=".") # Servirá el HTML desde la misma carpeta

        # Registrar las rutas del servidor web
        self.configurar_rutas()

    def iniciar(self):
        if not self.modelo.cargar():
            print("Error crucial: No se pudo cargar el archivo datos.json")
            return
        
        print("Servidor de ValoAcademy iniciado correctamente en http://127.0.0.1:5000")
        # Inicia el servidor web local
        self.app.run(debug=True, port=5000)

    def configurar_rutas(self):
        # 1. Ruta para cargar la página web inicial
        @self.app.route("/")
        def index():
            return render_template("index.html")

        # 2. Endpoint para obtener datos de una mecánica específica
        @self.app.route("/api/mecanica/<nombre>")
        def api_mecanica(nombre):
            mecanica = self.modelo.obtener_mecanica(nombre)
            if mecanica:
                return jsonify({
                    "status": "success",
                    "nombre": mecanica.nombre.upper(),
                    "descripcion": mecanica.descripcion
                })
            return jsonify({"status": "error", "message": "Mecánica no encontrada"}), 404

        # 3. Endpoint para obtener datos de un arma específica
        @self.app.route("/api/arma/<nombre>")
        def api_arma(nombre):
            arma = self.modelo.obtener_arma(nombre)
            if arma:
                return jsonify({
                    "status": "success",
                    "nombre": arma.nombre.upper(),
                    "tipo": arma.tipo,
                    "costo": arma.costo,
                    "dano": arma.dano,
                    "consejo": arma.consejo
                })
            return jsonify({"status": "error", "message": "Arma no encontrada"}), 404