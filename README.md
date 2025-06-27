# Curso de Python - Proyecto de Aprendizaje

Este repositorio contiene un proyecto estructurado para aprender programación en Python, diseñado para principiantes y desarrolladores que quieren establecer buenas prácticas desde el inicio.

## 🎯 Objetivos

- Aprender los fundamentos de Python
- Establecer un flujo de trabajo profesional
- Implementar buenas prácticas de desarrollo
- Crear código mantenible y bien documentado

## 📁 Estructura del Proyecto

```
curso-python/
├── src/                    # Código fuente principal
│   ├── __init__.py        # Inicialización del paquete
│   ├── main.py            # Punto de entrada de la aplicación
│   └── utils.py           # Funciones de utilidad
├── tests/                 # Pruebas unitarias
│   ├── __init__.py
│   └── test_utils.py      # Pruebas para utils.py
├── notebooks/             # Jupyter Notebooks
│   └── 01_introduccion_python.ipynb
├── docs/                  # Documentación
├── requirements.txt       # Dependencias del proyecto
├── pyproject.toml        # Configuración del proyecto
├── .gitignore            # Archivos a ignorar en Git
└── README.md             # Este archivo
```

## 🚀 Inicio Rápido

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd curso-python
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el programa principal

```bash
python src/main.py
```

### 5. Ejecutar las pruebas

```bash
pytest tests/
```

## 📚 Contenido del Curso

### Módulos Incluidos

1. **`src/main.py`**: Programa principal con ejemplos básicos
   - Variables y tipos de datos
   - Funciones básicas
   - Estructuras de control

2. **`src/utils.py`**: Funciones de utilidad
   - Cálculos matemáticos
   - Conversiones
   - Estadísticas básicas

3. **`tests/test_utils.py`**: Pruebas unitarias
   - Verificación de funciones
   - Casos de prueba variados
   - Manejo de excepciones

4. **`notebooks/01_introduccion_python.ipynb`**: Tutorial interactivo
   - Configuración del entorno
   - Conceptos fundamentales
   - Ejemplos prácticos

## 🛠️ Herramientas y Dependencias

### Dependencias Principales
- `numpy`: Computación numérica
- `pandas`: Análisis de datos
- `matplotlib`: Visualización
- `requests`: Peticiones HTTP

### Herramientas de Desarrollo
- `pytest`: Framework de pruebas
- `black`: Formateador de código
- `flake8`: Linting
- `pylint`: Análisis estático

### Entorno Jupyter
- `jupyter`: Notebooks interactivos
- `ipykernel`: Kernel de Python

## 📖 Uso de los Notebooks

Para trabajar con los Jupyter Notebooks:

1. Asegúrate de tener el entorno virtual activado
2. Instala las dependencias: `pip install -r requirements.txt`
3. Inicia Jupyter: `jupyter notebook` o `jupyter lab`
4. Navega a la carpeta `notebooks/`
5. Abre `01_introduccion_python.ipynb`

## 🧪 Ejecutar Pruebas

### Todas las pruebas
```bash
pytest
```

### Pruebas con cobertura
```bash
pytest --cov=src
```

### Pruebas específicas
```bash
pytest tests/test_utils.py::TestCalcularAreaCirculo
```

## 🎨 Formateo y Linting

### Formatear código con Black
```bash
black src/ tests/
```

### Verificar estilo con Flake8
```bash
flake8 src/ tests/
```

### Análisis estático con Pylint
```bash
pylint src/
```

## 📝 Convenciones

### Estilo de Código
- Seguimos [PEP 8](https://pep8.org/) para el estilo de Python
- Usamos [Black](https://black.readthedocs.io/) para formateo automático
- Nombres de variables y funciones en `snake_case`
- Nombres de clases en `PascalCase`

### Documentación
- Todas las funciones deben tener docstrings
- Incluir descripción, parámetros y valor de retorno
- Ejemplos de uso cuando sea apropiado

### Pruebas
- Una prueba por funcionalidad específica
- Nombres descriptivos para las pruebas
- Incluir casos de borde y manejo de errores

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en:
- Abrir un issue en GitHub
- Enviar un email a [tu.email@ejemplo.com]
- Unirte a las discusiones del proyecto

## 🎓 Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/)
- [Real Python](https://realpython.com/) - Tutoriales avanzados
- [Python Package Index (PyPI)](https://pypi.org/)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

¡Feliz codificación! 🐍✨