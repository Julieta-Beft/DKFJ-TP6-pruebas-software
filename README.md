# DKFJ-TP6-pruebas-software

# Gestión de la Calidad del Software

## 👥 Integrantes del grupo
- Kevin Damian
- Julieta Fretes

## 🧾 Descripción
Este proyecto corresponde al Trabajo Práctico N°6 de la materia Ingeniería de Software III (2025) y tiene como objetivo aplicar técnicas de aseguramiento de la calidad del software, a través de pruebas unitarias, pruebas de integración y pruebas basadas en comportamiento (BDD).

Las funciones utilizadas en este trabajo son:
- suma(a, b): retorna la suma de dos enteros
- cuadrado(a): retorna el cuadrado de un número
- cuadrado_binomio(a, b): calcula el cuadrado de un binomio usando suma y cuadrado


## 📂 Estructura del proyecto
DKFJ-TP6-PRUEBAS-SOFTWARE/
├── funciones.py               # Funciones matemáticas
├── test_funciones.py         # Pruebas unitarias e integración con pytest
├── requirements.txt          # Dependencias del proyecto
├── README.md                # Este archivo
├── features/
│   ├── suma.feature          # Escenarios Gherkin para la función suma
│   ├── cuadrado.feature      # Escenarios Gherkin para la función cuadrado
│   └── steps/
│       └── math_steps.py     # Implementación de los pasos (Behave)


## 🧪 Pruebas con Pytest
El archivo test_funciones.py contiene:
- 3 pruebas unitarias por Kevin Damian
- 2 pruebas unitarias por Julieta Fretes
- 1 prueba de integración por cada integrante

▶ Cómo ejecutar las pruebas unitarias:
pytest test_funciones.py -v


🧬 Pruebas con Behave (BDD)
Los escenarios .feature están escritos en lenguaje Gherkin y permiten validar el comportamiento de las funciones suma y cuadrado.

▶ Cómo ejecutar las pruebas de comportamiento:

behave


## 📦 Instalación de dependencias
Para instalar las dependencias necesarias, ejecutar:
pip install -r requirements.txt

Esto instalará pytest y behave.