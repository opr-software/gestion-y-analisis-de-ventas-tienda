# 🏪 Sistema de Gestión y Análisis de Ventas de una Tienda

Simulador y analizador de ventas diarias desarrollado en Python utilizando la librería **NumPy**, enfocado en la manipulación de arreglos, operaciones matemáticas vectorizadas y matrices.

---

## 📋 Descripción del Proyecto

Este proyecto demuestra el uso de funciones fundamentales de **NumPy** aplicadas al control comercial de una tienda durante un periodo de 10 días:

1. **Identificadores de días:** Generación de un rango de días con `np.arange(1, 11)`.
2. **Inicialización de registros:** Arreglo base en ceros mediante `np.zeros(10)`.
3. **Factores de descuento:** Creación de arrays de unos escalados con `np.ones(10) * 0.8` (aplicación del 20% de descuento).
4. **Secuencia de ventas:** Simulación de una tendencia descendente con paso negativo mediante `np.arange()`.
5. **Operaciones matemáticas vectoriales:** Cálculo de ventas netas multiplicando arreglos directamente sin bucles.
6. **Matriz de productos:** Modelado de ventas multidimensionales por producto (matriz 2D).
7. **Métricas de rendimiento:** Identificación del mejor resultado de ventas con el método `.max()`.

---

## 🛠️ Tecnologías

- **Python 3.8+**
- **NumPy**

---

## 📁 Estructura del Proyecto

```text
Sistema de gestión y análisis de ventas de una tienda/
│
├── main.py              # Script con la lógica de análisis y gestión de ventas
├── requirements.txt     # Dependencias del proyecto (numpy)
└── README.md            # Documentación del proyecto
```

---

## 🚀 Instalación y Configuración

### 1. Acceder a la carpeta del proyecto
Abre una terminal en la carpeta principal:
```bash
cd "Sistema de gestión y análisis de ventas de una tienda"
```

### 2. Crear y activar un entorno virtual (recomendado)

- **En Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar dependencias
Con el entorno virtual activado:
```bash
pip install -r requirements.txt
```

---

## ▶️ Uso y Ejecución

Ejecuta el script principal desde la terminal:

- **En Windows:**
  ```powershell
  py main.py
  # o también:
  python main.py
  ```

- **En macOS / Linux:**
  ```bash
  python3 main.py
  ```

### Salida esperada en consola

```text
Días:  [ 1  2  3  4  5  6  7  8  9 10]
Registros:  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Descuentos:  [0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8]
Ventas:  [800. 720. 640. 560. 480. 400. 320. 240. 160.  80.]
Productos:  [[ 10 203]
 [ 20  30]
 [ 30  40]
 [ 40  50]
 [ 50  60]
 [ 60  70]
 [ 70  80]
 [ 80  90]
 [ 90 100]
 [100 110]]
Mejor día: 800.0
```

---

## 📚 Conceptos de NumPy Aplicados

| Función / Método | Uso en el Proyecto |
| :--- | :--- |
| `np.arange()` | Creación de rangos numéricos y secuencias descendentes. |
| `np.zeros()` | Inicialización de buffers o registros en ceros. |
| `np.ones()` | Creación de vectores unitarios escalados para multiplicadores/descuentos. |
| `array_a * array_b` | Multiplicación vectorial elemento por elemento (broadcasting). |
| `np.array([...])` | Creación de matrices multidimensionales (2D). |
| `array.max()` | Extracción del valor máximo en un arreglo. |

---

## 📄 Licencia

Proyecto de código abierto desarrollado con fines didácticos y de práctica en análisis de datos con Python.
