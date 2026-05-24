import heapq

SISTEMA_MIO = {
    'Terminal Menga': [
        ('Estación Alamos', 6, 'E21'), 
        ('Estación San Pedro', 18, 'T31')
    ],
    'Estación Alamos': [
        ('Terminal Menga', 6, 'E21'), 
        ('Estación San Pedro', 12, 'E21')
    ],
    'Estación San Pedro': [
        ('Terminal Menga', 18, 'T31'),
        ('Estación Alamos', 12, 'E21'),
        ('Estación Unidad Deportiva', 10, 'T31'),
        ('Estación Unidad Deportiva', 11, 'E21')  # Opción alternativa por la misma troncal
    ],
    'Estación Unidad Deportiva': [
        ('Estación San Pedro', 10, 'T31'),
        ('Estación Pampalinda', 7, 'T31'),
        ('Terminal Andrés Sanín', 22, 'T47B')
    ],
    'Estación Pampalinda': [
        ('Estación Unidad Deportiva', 7, 'T31'),
        ('Terminal Universidades', 12, 'T31'),
        ('Terminal Universidades', 10, 'E21')
    ],
    'Terminal Universidades': [
        ('Estación Pampalinda', 10, 'E21'),
        ('Estación Pampalinda', 12, 'T31')
    ],
    'Terminal Andrés Sanín': [
        ('Estación Unidad Deportiva', 22, 'T47B')
    ]
}

# 2. HEURÍSTICA 

HEURISTICA_HACIA_UNIVERSIDADES = {
    'Terminal Menga': 35,
    'Estación Alamos': 30,
    'Estación San Pedro': 20,
    'Terminal Andrés Sanín': 25,
    'Estación Unidad Deportiva': 12,
    'Estación Pampalinda': 8,
    'Terminal Universidades': 0
}

# 3. MOTOR DE INFERENCIA 
def buscar_ruta_mio(sistema, inicio, destino, heuristica):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica.get(inicio, 0), 0, inicio, [(inicio, 'Inicio')]))
    
    costos_visitados = {inicio: 0}
    
    while cola_prioridad:
        f, g_actual, nodo_actual, camino = heapq.heappop(cola_prioridad)
        
        if nodo_actual == destino:
            return camino, g_actual
            
        for vecino, tiempo, ruta_bus in sistema.get(nodo_actual, []):
            nuevo_g = g_actual + tiempo
            
            if vecino not in costos_visitados or nuevo_g < costos_visitados[vecino]:
                costos_visitados[vecino] = nuevo_g
                h = heuristica.get(vecino, 0)
                nuevo_f = nuevo_g + h
                
                nuevo_camino = list(camino)
                nuevo_camino.append((vecino, ruta_bus))
                
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, nuevo_camino))
                
    return None, float('inf')

# 4. EJECUCIÓN Y PRUEBA DEL SISTEMA INTELEGENTE
origen = 'Terminal Menga'
destino = 'Terminal Universidades'

ruta_optima, tiempo_total = buscar_ruta_mio(SISTEMA_MIO, origen, destino, HEURISTICA_HACIA_UNIVERSIDADES)

# Presentación de resultados
if ruta_optima:
    print(f"Calculando la mejor ruta desde: {origen}")
    print(f"Destino solicitado: {destino}\n")
    
    for i, (estacion, bus) in enumerate(ruta_optima):
        if i == 0:
            print(f"[Inicio] Abordar en: {estacion}")
        else:
            print(f"Tomar ruta [{bus}] hasta {estacion}")
            
    print(f"Tiempo total estimado de viaje: {tiempo_total} minutos.")

else:
    print("Lo sentimos, no se pudo consolidar una ruta con las reglas vigentes.")
