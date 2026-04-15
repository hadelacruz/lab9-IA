from modelo import prob_conjunta, EPSILON
from inferencia import inferencia_marginal
from explain_away import demostrar_explain_away

def task_2_1():
    print("\n" + "=" * 55)
    print("  DISTRIBUCIÓN CONJUNTA")
    print(f"  Parámetro epsilon = {EPSILON}")
    print("=" * 55)
    print(f"  {'B':>3} {'E':>3} {'A':>3}   P(B,E,A)")
    print("-" * 55)

    total = 0.0
    for b in [0, 1]:
        for e in [0, 1]:
            for a in [0, 1]:
                p = prob_conjunta(b, e, a)
                total += p
                print(f"  {b:>3} {e:>3} {a:>3}   {p:.8f}")

    print("-" * 55)
    print(f"  Suma total: {total:.8f}  ← debe ser 1.0")

def task_2_2():
    print("\n" + "=" * 55)
    print("  INFERENCIA MARGINAL")
    print("=" * 55)

    # P(A=1) sin ninguna evidencia: marginalizar sobre B y E
    p_alarma = inferencia_marginal(
        query={'A': 1},
        evidencia={}  # Sin evidencia = distribución marginal pura
    )
    print(f"\n  P(A=1) = {p_alarma:.6f}")
    print(f"  → Probabilidad de que la alarma suene sin saber nada más.")
    print(f"  (Valor teórico: 2ε - ε² = {2*EPSILON - EPSILON**2:.6f})")

def task_2_3():
    print("\n" + "=" * 55)
    print("  EFECTO EXPLAIN AWAY")
    print("=" * 55)
    demostrar_explain_away()

if __name__ == "__main__":
    print("\nCC3045 - Inteligencia Artificial | Laboratorio 9")
    print("Motor de Inferencia: Red Bayesiana de Judea Pearl")

    task_2_1()
    task_2_2()
    task_2_3()