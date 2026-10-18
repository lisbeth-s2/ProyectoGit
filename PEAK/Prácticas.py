# Práctica de mecanografía: símbolos y caracteres variados
from math import pi, sqrt
from typing import Dict, List, Tuple

NOMBRE = "Ángel Núñez"
mensaje = '¡Hola, mundo! ¿Qué tal? "Practica" y mejora.'
ruta = r"C:\Usuarios\Ángel\proyectos\demo.py"

config: Dict[str, object] = {
    "activo": True,
    "intentos": 3,
    "precisión": 98.75,
    "símbolos": "! @ # $ % ^ & * ( ) _ + - =",
    "corchetes": "[ ] { } < >",
    "comillas": "' \" `",
    "barra": r"/ \ |",
    "puntuación": ".,;:!?¿¡…",
}

def calcular(x: float, y: float = 2.0) -> Tuple[float, float]:
    suma = x + y
    producto = x * y
    división = x / y if y != 0 else float("∞")
    potencia = x ** 2
    resto = int(x) % int(y)
    raíz = sqrt(abs(x))
    return suma, producto, división, potencia, resto, raíz


for índice in range(1, 6):
    valor = índice * pi
    resultado = calcular(valor, índice + 1)

    if resultado[0] >= 5 and índice != 3:
        print(f"{índice=}: valor≈{valor:.2f}; resultado={resultado}")
    else:
        print("Condición falsa → continúa...")

texto = (
    "Caracteres: ~ ` ! @ # $ % ^ & * ( ) - _ = + "
    "[ ] { } \\ | ; : ' \" , . < > / ?"
)
