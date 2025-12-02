import heapq

class Graph: # define un grafo
    def __init__(self):
        self.graph = {}

    # Agrega una arista al grafo, doble sesntido porque es no dirigido
    def add_edge(self, nodo1, nodo2, peso): 
        if nodo1 not in self.graph: self.graph[nodo1] = {}
        if nodo2 not in self.graph: self.graph[nodo2] = {}
        self.graph[nodo1][nodo2] = peso
        self.graph[nodo2][nodo1] = peso 

    # crea diccionario con distancia inf a los nodos y 0 al origen
    def distancia_minima(self, origen: str): 
        distancia = {node: float("inf") for node in self.graph}
        distancia[origen] = 0
        # cola de prioridad
        pq = [(0, origen)] 
        # se guarda el camino
        caminos = {node: None for node in self.graph}
        
        # saca el nodo mas cercano no visitado
        while pq:
            distancia_actual, nodo_actual = heapq.heappop(pq) # nodo con menor distancia
            if distancia_actual > distancia[nodo_actual]: # si ya se visitó,
                continue
            # recorre todos los vecinos
            for vecino, peso in self.graph.get(nodo_actual, {}).items(): # vecinos del nodo actual
                distancia_tentativa = distancia_actual + peso # distancia hasta el vecino
                # si es menor, actualiza distancia y camino
                if distancia_tentativa < distancia[vecino]:
                    distancia[vecino] = distancia_tentativa
                    caminos[vecino] = nodo_actual 
                    heapq.heappush(pq, (distancia_tentativa, vecino))     
        return distancia, caminos

GRAFO_TIEMPOS = {
    "H_Alvear": {"A_Cementerio": 5, "A_BellasArtes": 10, "A_Colon": 15},
    "H_Hilton": {"A_PteMujer": 5, "A_Rosada": 15, "A_CCK": 10},
    "H_FourSeasons": {"A_Cementerio": 10, "A_Obelisco": 15, "A_Colon": 10},
    "H_Sheraton": {"A_Obelisco": 20, "A_CCK": 15, "A_Cementerio": 20},
    "H_Faena": {"A_PteMujer": 10, "A_SanTelmo": 15, "A_Reserva": 5},
    
    "A_Obelisco": {"A_Colon": 5, "A_Rosada": 15, "A_Tortoni": 10, "A_Congreso": 15, "A_Cementerio": 20},
    "A_Colon": {"A_Obelisco": 5, "A_Tortoni": 10, "A_Ateneo": 15, "A_Cementerio": 15},
    "A_Rosada": {"A_Obelisco": 15, "A_Catedral": 5, "A_Cabildo": 5, "A_SanTelmo": 15, "A_PteMujer": 10, "A_CCK": 10},
    "A_Catedral": {"A_Rosada": 5, "A_Cabildo": 2, "A_Obelisco": 10},
    "A_Cabildo": {"A_Rosada": 5, "A_Catedral": 2, "A_Tortoni": 5},
    "A_Tortoni": {"A_Cabildo": 5, "A_Obelisco": 10, "A_Barolo": 5},
    "A_Barolo": {"A_Tortoni": 5, "A_Congreso": 5},
    "A_Congreso": {"A_Barolo": 5, "A_Ateneo": 15, "A_Obelisco": 15},
    "A_Caminito": {"A_Bombonera": 10, "A_SanTelmo": 20, "A_Reserva": 25},
    "A_Bombonera": {"A_Caminito": 10, "A_SanTelmo": 15},
    "A_SanTelmo": {"A_Caminito": 20, "A_Bombonera": 15, "A_MAMBA": 5, "A_Rosada": 15},
    "A_MAMBA": {"A_SanTelmo": 5, "A_PteMujer": 20},
    "A_PteMujer": {"A_Reserva": 10, "A_CCK": 10, "A_Rosada": 10, "H_Hilton": 5},
    "A_Reserva": {"A_PteMujer": 10, "A_Caminito": 25, "H_Faena": 5},
    "A_CCK": {"A_PteMujer": 10, "A_Rosada": 10, "A_Colon": 15},
    "A_Cementerio": {"A_Floralis": 10, "A_BellasArtes": 5, "A_Ateneo": 10, "A_Colon": 15, "A_Obelisco": 20},
    "A_Floralis": {"A_Cementerio": 10, "A_BellasArtes": 5, "A_Japones": 15, "A_MALBA": 10},
    "A_BellasArtes": {"A_Cementerio": 5, "A_Floralis": 5, "A_Japones": 15},
    "A_Ateneo": {"A_Cementerio": 10, "A_Colon": 15, "A_Congreso": 15},
    "A_Japones": {"A_Floralis": 15, "A_BellasArtes": 15, "A_MALBA": 5, "A_Rosedal": 10, "A_Planetario": 10},
    "A_Rosedal": {"A_Japones": 10, "A_Planetario": 5, "A_River": 20},
    "A_MALBA": {"A_Japones": 5, "A_Floralis": 10},
    "A_Planetario": {"A_Japones": 10, "A_Rosedal": 5, "A_River": 15},
    "A_River": {"A_Planetario": 15, "A_Rosedal": 20}
}

TIEMPOS_VISITA = {
    "A_Obelisco": 15, "A_Colon": 60, "A_Rosada": 60, "A_Catedral": 30,
    "A_Cabildo": 45, "A_Tortoni": 45, "A_Barolo": 90, "A_Congreso": 30,
    "A_Caminito": 60, "A_Bombonera": 60, "A_SanTelmo": 45,
    "A_MAMBA": 60, "A_PteMujer": 20, "A_Reserva": 90, "A_CCK": 60,
    "A_Cementerio": 90, "A_Floralis": 20, "A_BellasArtes": 90, "A_Ateneo": 30,
    "A_Japones": 60, "A_Rosedal": 45, "A_MALBA": 90, "A_Planetario": 45,
    "A_River": 90
}

NOMBRES_ATRACCIONES = {
    "H_Alvear": "Hotel Alvear (Recoleta)", "H_Hilton": "Hotel Hilton (Puerto Madero)",
    "H_FourSeasons": "Hotel Four Seasons (Retiro)", "H_Sheraton": "Hotel Sheraton (Retiro)",
    "H_Faena": "Hotel Faena (Puerto Madero)", 
    "A_Obelisco": "Obelisco", "A_Colon": "Teatro Colón", "A_Rosada": "Casa Rosada",
    "A_Catedral": "Catedral Metropolitana", "A_Cabildo": "Cabildo", "A_Tortoni": "Café Tortoni",
    "A_Barolo": "Palacio Barolo", "A_Congreso": "Congreso Nacional", "A_Caminito": "Caminito",
    "A_Bombonera": "Estadio La Bombonera", "A_SanTelmo": "Feria de San Telmo",
    "A_MAMBA": "Museo de Arte Moderno", "A_PteMujer": "Puente de la Mujer", 
    "A_Reserva": "Reserva Ecológica", "A_CCK": "Centro Cultural Kirchner", 
    "A_Cementerio": "Cementerio de la Recoleta", "A_Floralis": "Floralis Genérica", 
    "A_BellasArtes": "Museo Bellas Artes", "A_Ateneo": "El Ateneo Grand Splendid", 
    "A_Japones": "Jardín Japonés", "A_Rosedal": "El Rosedal de Palermo", 
    "A_MALBA": "MALBA", "A_Planetario": "Planetario", "A_River": "Estadio Monumental"
}

DESCRIPCIONES = {
    "A_Obelisco": "El máximo ícono de la ciudad, construido en 1936.",
    "A_Colon": "Uno de los teatros de ópera con mejor acústica del mundo.",
    "A_Rosada": "Sede del Gobierno Nacional y su famoso balcón.",
    "A_Catedral": "El principal templo católico de Argentina.",
    "A_Cabildo": "Edificio histórico testigo de la Revolución de Mayo.",
    "A_Tortoni": "El café más antiguo de la ciudad.",
    "A_Barolo": "Rascacielos inspirado en la Divina Comedia.",
    "A_Congreso": "Imponente palacio legislativo.",
    "A_Caminito": "Museo a cielo abierto lleno de color y tango.",
    "A_Bombonera": "El mítico estadio de Boca Juniors.",
    "A_SanTelmo": "El barrio más antiguo y bohemio.",
    "A_MAMBA": "Museo de Arte Moderno.",
    "A_PteMujer": "Icono de Puerto Madero por Calatrava.",
    "A_Reserva": "Espacio verde para conectar con la naturaleza.",
    "A_CCK": "Antiguo Palacio de Correos, hoy centro cultural.",
    "A_Cementerio": "Arte funerario y mausoleos históricos.",
    "A_Floralis": "Escultura metálica gigante con movimiento.",
    "A_BellasArtes": "Colección de arte público más importante.",
    "A_Ateneo": "Librería ubicada en un antiguo teatro.",
    "A_Japones": "Cultura nipona, lagos y puentes.",
    "A_Rosedal": "Paseo romántico con miles de rosales.",
    "A_MALBA": "Museo de Arte Latinoamericano.",
    "A_Planetario": "Centro de divulgación astronómica.",
    "A_River": "Estadio de River Plate y la selección."
}

DIRECCIONES = {
    "H_Alvear": "Av. Alvear 1891", "H_Hilton": "Macacha Güemes 351",
    "H_FourSeasons": "Posadas 1086", "H_Sheraton": "San Martín 1225",
    "H_Faena": "Martha Salotti 445", 
    "A_Obelisco": "Av. 9 de Julio y Corrientes", "A_Colon": "Cerrito 628",
    "A_Rosada": "Balcarce 50", "A_Catedral": "San Martín 27",
    "A_Cabildo": "Bolívar 65", "A_Tortoni": "Av. de Mayo 825",
    "A_Barolo": "Av. de Mayo 1370", "A_Congreso": "Av. Entre Ríos s/n",
    "A_Caminito": "Valle Iberlucea 1200", "A_Bombonera": "Brandsen 805",
    "A_SanTelmo": "Defensa y Humberto I", "A_MAMBA": "Av. San Juan 350",
    "A_PteMujer": "Dique 3, Puerto Madero", "A_Reserva": "Av. Tristán Achával Rodríguez 1550",
    "A_CCK": "Sarmiento 151", "A_Cementerio": "Junín 1760",
    "A_Floralis": "Av. Figueroa Alcorta 2301", "A_BellasArtes": "Av. del Libertador 1473",
    "A_Ateneo": "Av. Santa Fe 1860", "A_Japones": "Av. Casares 3450",
    "A_Rosedal": "Av. Infanta Isabel 900", "A_MALBA": "Av. Figueroa Alcorta 3415",
    "A_Planetario": "Av. Sarmiento s/n", "A_River": "Av. Figueroa Alcorta 7597"
}

COORDENADAS = {
    "H_Alvear": (-34.5875, -58.3885), "H_Hilton": (-34.6103, -58.3640),
    "H_FourSeasons": (-34.5913, -58.3805), "H_Sheraton": (-34.5929, -58.3744),
    "H_Faena": (-34.6155, -58.3630),
    "A_Obelisco": (-34.6037, -58.3816), "A_Colon": (-34.6011, -58.3831),
    "A_Rosada": (-34.6080, -58.3705), "A_Catedral": (-34.6076, -58.3733),
    "A_Cabildo": (-34.6086, -58.3737), "A_Tortoni": (-34.6091, -58.3800),
    "A_Barolo": (-34.6096, -58.3857), "A_Congreso": (-34.6098, -58.3926),
    "A_Caminito": (-34.6394, -58.3627), "A_Bombonera": (-34.6356, -58.3648),
    "A_SanTelmo": (-34.6212, -58.3733), "A_MAMBA": (-34.6239, -58.3712),
    "A_PteMujer": (-34.6084, -58.3650), "A_Reserva": (-34.6150, -58.3550),
    "A_CCK": (-34.6035, -58.3695), "A_Cementerio": (-34.5878, -58.3929),
    "A_Floralis": (-34.5819, -58.3944), "A_BellasArtes": (-34.5841, -58.3929),
    "A_Ateneo": (-34.5956, -58.3932), "A_Japones": (-34.5755, -58.4034),
    "A_Rosedal": (-34.5716, -58.4176), "A_MALBA": (-34.5773, -58.4018),
    "A_Planetario": (-34.5697, -58.4116), "A_River": (-34.5453, -58.4498)
}

MAPA_IMAGENES = {
    'hilton': '/static/img/hilton.jpg', 'sheraton': '/static/img/sheraton.jpg', 
    'faena': '/static/img/faena.jpg', 'alvear': '/static/img/alvear.jpg', 
    'four': '/static/img/fs.jpg', 'season': '/static/img/fs.jpg',
    'obelisco': '/static/img/obelisco.jpg', 'colon': '/static/img/colon.jpg', 
    'teatro': '/static/img/colon.jpg', 'rosada': '/static/img/casa_rosada.jpg', 
    'gobierno': '/static/img/casa_rosada.jpg', 'mujer': '/static/img/puente_mujer.jpg', 
    'madero': '/static/img/puerto_madero.jpg', 'flor': '/static/img/floralis.jpg', 
    'caminito': '/static/img/caminito.jpg', 'boca': '/static/img/caminito.jpg', 
    'recoleta': '/static/img/cementerio_recoleta.jpg', 'cementerio': '/static/img/cementerio_recoleta.jpg', 
    'ateneo': '/static/img/ateneo.jpg', 'japonés': '/static/img/jardin_japones.jpg', 
    'japones': '/static/img/jardin_japones.jpg', 'san telmo': '/static/img/san_telmo.jpg', 
    'barolo': '/static/img/barolo.jpg', 'congreso': '/static/img/congreso.jpg', 
    'mayo': '/static/img/plaza_mayo.jpg', 'cabildo': '/static/img/cabildo.jpg', 
    'catedral': '/static/img/catedral.jpg', 'tortoni': '/static/img/tortoni.jpg', 
    'malba': '/static/img/malba.jpg', 'bellas': '/static/img/bellas_artes.jpg', 
    'planetario': '/static/img/planetario.jpg', 'reserva': '/static/img/reserva.jpg', 
    'cck': '/static/img/cck.jpg', 'kirchner': '/static/img/cck.jpg', 
    'usina': '/static/img/usina.jpg', 'rosedal': '/static/img/rosedal.jpg', 
    'arte': '/static/img/arte_moderno.jpg', 'river': '/static/img/river.jpg', 
    'monumental': '/static/img/river.jpg', 'bombonera': '/static/img/boca.jpg'
}

def obtener_imagen(nombre):
    nombre_lower = nombre.lower()
    for key, url in MAPA_IMAGENES.items():
        if key in nombre_lower:
            return url
    return f"/static/img/default.jpg"

def generar_link_maps(ruta_del_dia):
    base_url = "https://www.google.com/maps/dir"
    coords_str = []
    for punto in ruta_del_dia:
        if punto['id'] in COORDENADAS:
            lat, lng = COORDENADAS[punto['id']]
            coords_str.append(f"{lat},{lng}")
    
    if not coords_str:
        return "#"
    
    return f"{base_url}/{'/'.join(coords_str)}"

# arma el itinerario
def generar_itinerario_completo(hotel_inicio: str, atracciones_deseadas: list = None):
    g_baires = Graph()  # Crear el grafo con todos los lugares y tiempos de viaje
    for origen, vecinos in GRAFO_TIEMPOS.items():
        for destino, tiempo in vecinos.items():
            g_baires.add_edge(origen, destino, tiempo)

    # Si no se especifican atracciones, se visitan todas las disponibles
    if not atracciones_deseadas:
        atracciones_deseadas = [k for k in g_baires.graph.keys() if k.startswith('A_')]

    TIEMPO_MAX_DIA = 480  # Tiempo máximo de visita por día (8 horas)
    pendientes = set(atracciones_deseadas)  # Atracciones por visitar
    visitados_en_total = set()  # Atracciones ya visitadas
    itinerarios_por_dia = []  # Guardará el itinerario diario
    tiempo_total_global = 0
    dia_actual = 1

    while pendientes:
        pendientes_al_inicio_dia = len(pendientes)
        log_decisiones = []  # Registro de elecciones hechas en el día
        
        # Inicio del día desde el hotel
        nodo_actual = hotel_inicio
        tiempo_acumulado_hoy = 0
        
        # Info del hotel para iniciar el itinerario
        coord_inicio = COORDENADAS.get(hotel_inicio, (-34.6037, -58.3816))
        dir_inicio = DIRECCIONES.get(hotel_inicio, "Buenos Aires, Argentina")
        img_inicio = obtener_imagen(NOMBRES_ATRACCIONES.get(hotel_inicio, ""))
        
        itinerario_hoy = [{"paso": 0, "id": hotel_inicio, "nombre": NOMBRES_ATRACCIONES.get(hotel_inicio, hotel_inicio),
                           "tiempo_viaje": 0, "tiempo_visita": 0, "costo_total_tramo": 0,
                           "descripcion": "Punto de partida.", "direccion": dir_inicio,
                           "lat": coord_inicio[0], "lng": coord_inicio[1], "imagen": img_inicio}]
        paso_contador = 1
        
        while True:
            # Calcula distancia mínima desde el nodo actual a todos los lugares
            distancias, _ = g_baires.distancia_minima(nodo_actual)
            proximo_destino = None
            menor_tiempo_viaje = float('inf')
            candidatos_paso = []

            # Selecciona la atracción más cercana pendiente
            for destino, tiempo_viaje in distancias.items():
                if destino in pendientes:
                    candidatos_paso.append({"nombre": NOMBRES_ATRACCIONES.get(destino, destino), "peso": tiempo_viaje})
                    if tiempo_viaje < menor_tiempo_viaje:
                        menor_tiempo_viaje = tiempo_viaje
                        proximo_destino = destino
            
            candidatos_paso.sort(key=lambda x: x['peso'])
            
            if proximo_destino is None:  # No quedan destinos alcanzables
                break

            # Verifica si cabe en el tiempo disponible del día
            tiempo_actividad = TIEMPOS_VISITA.get(proximo_destino, 60)
            costo_total_tramo = menor_tiempo_viaje + tiempo_actividad
            
            if tiempo_acumulado_hoy + costo_total_tramo <= TIEMPO_MAX_DIA:
                # Se agrega al itinerario
                tiempo_acumulado_hoy += costo_total_tramo
                tiempo_total_global += costo_total_tramo
                log_decisiones.append({"paso": paso_contador,
                                       "origen": NOMBRES_ATRACCIONES.get(nodo_actual, nodo_actual),
                                       "elegido": NOMBRES_ATRACCIONES.get(proximo_destino, proximo_destino),
                                       "peso_elegido": menor_tiempo_viaje,
                                       "candidatos": candidatos_paso[:4]})
                
                pendientes.remove(proximo_destino)
                visitados_en_total.add(proximo_destino)
                
                # Info de la atracción
                desc = DESCRIPCIONES.get(proximo_destino, "Descubre este lugar.")
                dire = DIRECCIONES.get(proximo_destino, "Buenos Aires")
                coord = COORDENADAS.get(proximo_destino, (-34.6037, -58.3816))
                nombre_real = NOMBRES_ATRACCIONES.get(proximo_destino, proximo_destino)
                img_lugar = obtener_imagen(nombre_real)
                
                itinerario_hoy.append({"paso": paso_contador, "id": proximo_destino, "nombre": nombre_real,
                                       "tiempo_viaje": menor_tiempo_viaje, "tiempo_visita": tiempo_actividad,
                                       "costo_total_tramo": costo_total_tramo, "descripcion": desc,
                                       "direccion": dire, "lat": coord[0], "lng": coord[1], "imagen": img_lugar})
                
                nodo_actual = proximo_destino
                paso_contador += 1
            else:
                break
        
        if len(pendientes) == pendientes_al_inicio_dia:
            break  # No se pudo avanzar, fin del itinerario

        # Regreso al hotel al final del día
        distancias_regreso, _ = g_baires.distancia_minima(nodo_actual)
        tiempo_regreso = distancias_regreso.get(hotel_inicio, 0)
        coord_fin = COORDENADAS.get(hotel_inicio, (-34.6037, -58.3816))
        dir_fin = DIRECCIONES.get(hotel_inicio, "Buenos Aires")
        img_fin = obtener_imagen(NOMBRES_ATRACCIONES.get(hotel_inicio, ""))

        itinerario_hoy.append({"paso": paso_contador, "id": hotel_inicio,
                               "nombre": NOMBRES_ATRACCIONES.get(hotel_inicio, hotel_inicio) + " (Regreso)",
                               "tiempo_viaje": tiempo_regreso, "tiempo_visita": 0,
                               "costo_total_tramo": tiempo_regreso, "descripcion": "Fin del recorrido diario.",
                               "direccion": dir_fin, "lat": coord_fin[0], "lng": coord_fin[1], "imagen": img_fin})
        
        tiempo_acumulado_hoy += tiempo_regreso
        tiempo_total_global += tiempo_regreso
        
        # Genera link de Google Maps para ese día
        mapa_url = generar_link_maps(itinerario_hoy)
        
        itinerarios_por_dia.append(
            {"dia": dia_actual, 
             "ruta": itinerario_hoy,
            "tiempo_dia_min": tiempo_acumulado_hoy,
            "mapa_url": mapa_url, "log_decisiones": log_decisiones})
        
        dia_actual += 1

    # Retorna el itinerario completo con tiempos y cantidad de atracciones visitadas
    return {"itinerario": itinerarios_por_dia, 
            "tiempo_total_min": tiempo_total_global,
            "atracciones_visitadas": len(visitados_en_total)}


if __name__ == "__main__":
    # Bloque de prueba
    hotel_seleccionado = "H_Hilton" 
    print(f"Calculando ruta de prueba...")
    resultado = generar_itinerario_completo(hotel_seleccionado)
    print("Cálculo finalizado correctamente.")