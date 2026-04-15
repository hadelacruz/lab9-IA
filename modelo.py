# Define los parámetros del modelo de Red Bayesiana: Terremotos, Robos y Alarmas
# Basado en el problema clásico de Judea Pearl.

# Probabilidad base de un evento raro (epsilon)
EPSILON = 0.01

def p_robo(b):
    if b == 1:
        return EPSILON
    else:
        return 1 - EPSILON

def p_terremoto(e):
    if e == 1:
        return EPSILON
    else:
        return 1 - EPSILON

def p_alarma_dado(a, b, e):
    # La alarma debería sonar si b=1 OR e=1
    alarma_esperada = int(b == 1 or e == 1)
    # Retorna 1 si el valor de 'a' coincide con lo esperado, 0 si no
    return 1 if a == alarma_esperada else 0

def prob_conjunta(b, e, a):
    return p_robo(b) * p_terremoto(e) * p_alarma_dado(a, b, e)
