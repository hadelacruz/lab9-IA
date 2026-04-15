# Red Bayesiana: Terremotos, Robos y Alarmas

---

## Descripción

Implementación del motor de inferencia del problema clásico de Judea Pearl usando una **Red Bayesiana**. El modelo incluye tres variables booleanas: Robo (B), Terremoto (E) y Alarma (A), y demuestra numéricamente el efecto *Explain Away*.

---

## Estructura del proyecto

```
├── main.py          # Punto de entrada: ejecuta los tres tasks
├── modelo.py        # Task 2.1 – Parámetros y distribución conjunta P(B,E,A)
├── inferencia.py    # Task 2.2 – Inferencia marginal por marginalización
├── explain_away.py  # Task 2.3 – Demostración del efecto Explain Away
└── README.md
```

---

## Cómo ejecutar

```bash
python main.py
```

No se requieren dependencias externas. Solo Python 3.x estándar.

---

## El Modelo Bayesiano

La red sigue la estructura causal del problema de Pearl:

```
  B       E
   \     /
    \   /
      A
```

Con los siguientes parámetros (ε = 0.01):

| Variable | Distribución |
|----------|-------------|
| P(B=1)   | ε = 0.01    |
| P(E=1)   | ε = 0.01    |
| P(A=1 \| B,E) | 1 si B=1 ó E=1, 0 en caso contrario |

La distribución conjunta se calcula con la **regla de la cadena para Redes Bayesianas**:

```
P(B, E, A) = P(B) · P(E) · P(A | B, E)
```

---

## Resultados esperados

### Task 2.1 – Distribución Conjunta

La tabla completa de `P(B=b, E=e, A=a)` para las 8 combinaciones posibles. La suma de todas las filas debe ser exactamente 1.0.

### Task 2.2 – Inferencia Marginal

```
P(A=1) ≈ 0.019900
```

Esto se obtiene marginalizando sobre B y E: sumando `P(B=b, E=e, A=1)` para todos los valores de b y e. El valor teórico es `2ε - ε²`.

### Task 2.3 – Efecto Explain Away

```
P(B=1 | A=1)       ≈ 0.5025
P(B=1 | A=1, E=1)  ≈ 0.0100
```

---

## Conclusión: El Efecto *Explain Away*

El efecto *Explain Away* (o "explicar al descartar") es uno de los fenómenos más importantes que emergen de las Redes Bayesianas con estructura de **causa común**. Se produce cuando dos causas independientes comparten un mismo efecto: al condicionar sobre el efecto, las causas dejan de ser independientes entre sí.

### ¿Qué demuestran los números?

En nuestro modelo, **Robo (B)** y **Terremoto (E)** son causas **independientes** entre sí (no hay ninguna arista que las conecte directamente). Sin embargo, al observar que la alarma sonó (A=1), ocurre algo contraintuitivo:

- **Sin evidencia de terremoto:** `P(B=1 | A=1) ≈ 0.5025`
  Cuando la alarma suena y no sabemos nada más, la probabilidad de robo sube dramáticamente desde el prior de 0.01 hasta aproximadamente 0.50. Tiene sentido: la alarma necesita una causa, y el robo es una candidata igualmente probable al terremoto.

- **Con evidencia de terremoto:** `P(B=1 | A=1, E=1) ≈ 0.0100`
  Al enterarnos de que hubo un terremoto (E=1), la probabilidad de robo **cae de vuelta al prior (ε = 0.01)**. El terremoto "explica" completamente por qué sonó la alarma, eliminando la necesidad de invocar al robo como causa.

### ¿Por qué ocurre esto?

Formalmente, sabemos que B y E son **marginalmente independientes**: `P(B, E) = P(B) · P(E)`. Sin embargo, **condicionadas sobre A**, se vuelven dependientes: `P(B, E | A) ≠ P(B | A) · P(E | A)`.

Esto ocurre porque A es un **nodo colisionador** (collider) en la estructura del grafo. Al condicionar sobre un colisionador, se abre un camino de influencia entre sus padres que antes estaba bloqueado. Este es un resultado fundamental de la teoría de d-separación de Pearl.

