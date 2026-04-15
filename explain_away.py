# Demuestra numéricamente el efecto "Explain Away" usando la Red Bayesiana.
# Este efecto ocurre cuando conocer una causa reduce la probabilidad de otra causa,
# a pesar de que ambas causas son independientes entre sí.

from inferencia import inferencia_marginal

def demostrar_explain_away():

    print("=" * 55)
    print("  DEMOSTRACIÓN DEL EFECTO EXPLAIN AWAY")
    print("  Red Bayesiana: Terremotos, Robos y Alarmas")
    print("=" * 55)

    # --- Diagnóstico Simple ---
    # P(B=1 | A=1): dado que la alarma sonó, ¿qué tan probable es un robo?
    # Aplicamos P(X|Y) = P(X,Y)/P(Y) marginalizando sobre E (variable oculta).
    p_robo_dado_alarma = inferencia_marginal(
        query={'B': 1},
        evidencia={'A': 1}
    )
    print(f"\n1. Diagnóstico Simple")
    print(f"   P(B=1 | A=1) = {p_robo_dado_alarma:.4f}")
    print(f"   La alarma sonó. Probabilidad de robo: {p_robo_dado_alarma:.4f}")

    # --- Efecto Explain Away ---
    # P(B=1 | A=1, E=1): la alarma sonó Y sabemos que hubo terremoto.
    # El terremoto "explica" la alarma, reduciendo la sospecha de robo.
    p_robo_dado_alarma_y_terremoto = inferencia_marginal(
        query={'B': 1},
        evidencia={'A': 1, 'E': 1}
    )
    print(f"\n2. Efecto Explain Away")
    print(f"   P(B=1 | A=1, E=1) = {p_robo_dado_alarma_y_terremoto:.4f}")
    print(f"   La alarma sonó Y hubo terremoto. Probabilidad de robo: {p_robo_dado_alarma_y_terremoto:.4f}")

    # --- Comparación ---
    print(f"\n3. Comparación")
    print(f"   P(B=1 | A=1)       = {p_robo_dado_alarma:.4f}")
    print(f"   P(B=1 | A=1, E=1)  = {p_robo_dado_alarma_y_terremoto:.4f}")
    reduccion = p_robo_dado_alarma - p_robo_dado_alarma_y_terremoto
    print(f"   Reducción          = {reduccion:.4f}")
    print("=" * 55)

    return p_robo_dado_alarma, p_robo_dado_alarma_y_terremoto
