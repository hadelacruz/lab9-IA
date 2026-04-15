# Implementa inferencia marginal sobre la Red Bayesiana de Terremotos, Robos y Alarmas.
# La marginalización consiste en sumar sobre las variables "ocultas" (no observadas).

from modelo import prob_conjunta

# Dominio de cada variable booleana
DOMINIO = [0, 1]

def inferencia_marginal(query: dict, evidencia: dict) -> float:
    numerador = 0.0    # P(query, evidencia) - suma sobre variables ocultas
    denominador = 0.0  # P(evidencia)        - suma sobre query y variables ocultas

    # Iterar sobre todas las combinaciones posibles de las 3 variables booleanas
    for b in DOMINIO:
        for e in DOMINIO:
            for a in DOMINIO:
                asignacion = {'B': b, 'E': e, 'A': a}

                # Verificar si esta asignación es consistente con la evidencia
                consistente_evidencia = all(
                    asignacion[var] == val for var, val in evidencia.items()
                )

                if not consistente_evidencia:
                    continue  # Saltar combinaciones inconsistentes con la evidencia

                # P(B=b, E=e, A=a) - usamos la distribución conjunta del modelo
                p = prob_conjunta(b, e, a)

                # Acumulamos el denominador: P(evidencia) sumando sobre todo lo demás
                denominador += p

                # Verificar si también es consistente con la query
                consistente_query = all(
                    asignacion[var] == val for var, val in query.items()
                )

                if consistente_query:
                    # Acumulamos el numerador: P(query, evidencia)
                    numerador += p

    if denominador == 0:
        raise ValueError("La probabilidad de la evidencia es 0. Evidencia imposible.")

    # P(query | evidencia) = P(query, evidencia) / P(evidencia)
    return numerador / denominador
