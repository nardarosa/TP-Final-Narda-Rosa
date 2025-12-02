from flask import Flask, render_template, request
# Importamos SOLO lo necesario
from grafo_dijkstra import generar_itinerario_completo, NOMBRES_ATRACCIONES

app = Flask(__name__)

HOTEL_OPTIONS = {
    "H_Alvear": "Hotel Alvear (Recoleta)", 
    "H_Hilton": "Hotel Hilton (Puerto Madero)",
    "H_FourSeasons": "Hotel Four Seasons (Retiro)", 
    "H_Sheraton": "Hotel Sheraton (Retiro)",
    "H_Faena": "Hotel Faena (Puerto Madero)"
}

# Filtramos solo las atracciones (A_) para mostrarlas en los checkboxes
LISTA_ATRACCIONES = {k: v for k, v in NOMBRES_ATRACCIONES.items() if k.startswith('A_')}

@app.route('/', methods=['GET', 'POST'])
def itinerario_web():
    resultados = None
    hotel_seleccionado_nombre = None
    
    if request.method == 'POST':
        hotel_id = request.form.get('hotel_select')
        atracciones_seleccionadas = request.form.getlist('atracciones')
        
        if hotel_id:
            try:
                if not atracciones_seleccionadas:
                    atracciones_seleccionadas = []
                
                # Ejecutamos el algoritmo principal
                resultados = generar_itinerario_completo(hotel_id, atracciones_seleccionadas)
                hotel_seleccionado_nombre = HOTEL_OPTIONS.get(hotel_id, hotel_id)
                
            except Exception as e:
                print(f"Error calculando itinerario: {e}")
                
    return render_template('itinerario_ba.html', 
                           hoteles=HOTEL_OPTIONS.items(), 
                           atracciones_disponibles=LISTA_ATRACCIONES.items(),
                           resultados=resultados,
                           hotel_seleccionado_nombre=hotel_seleccionado_nombre)

if __name__ == "__main__":
    app.run(debug=True)