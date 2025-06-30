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
├── .vscode/               # Configuración de VS Code
│   └── settings.json     # Configuración optimizada para Python
├── src/                   # Código fuente principal
│   ├── __init__.py       # Inicialización del paquete
│   ├── main.py           # Punto de entrada de la aplicación
│   └── utils.py          # Funciones de utilidad
├── tests/                # Pruebas unitarias
│   ├── __init__.py
│   └── test_utils.py     # Pruebas para utils.py (importación simplificada)
├── notebooks/            # Jupyter Notebooks
│   └── 01_introduccion_python.ipynb  # Tutorial completo
├── docs/                 # Documentación
├── venv/                 # Entorno virtual (creado automáticamente)
├── .gitignore           # Archivos a ignorar en Git (configurado)
├── activar.bat          # Script de activación rápida (Windows CMD)
├── activar.ps1          # Script de activación rápida (PowerShell)
├── limpiar.py           # Script de limpieza de archivos temporales
├── limpiar.bat          # Script de limpieza para Windows
├── pyproject.toml       # Configuración del proyecto
├── requirements.txt     # Dependencias del proyecto
├── setup.py             # Script de configuración automática (mejorado)
└── README.md            # Este archivo
```

## ✨ Mejoras Recientes

### 🔧 **Script de configuración mejorado (`setup.py`)**
- ✅ Verificación completa del entorno virtual
- ✅ Instalación automática de dependencias
- ✅ Creación de scripts de activación
- ✅ Diagnósticos detallados
- ✅ Instrucciones paso a paso

### 🧪 **Pruebas simplificadas**
- ✅ Importación directa y robusta en `test_utils.py`
- ✅ Eliminación de archivos de configuración innecesarios
- ✅ Limpieza de archivos temporales (`__pycache__`, `.pytest_cache`)

### 🧹 **Manejo de archivos temporales**
- ✅ Configuración de `.gitignore` para ignorar archivos de cache
- ✅ Configuración de VS Code para ocultar carpetas temporales
- ✅ Scripts de limpieza automática (`limpiar.py`, `limpiar.bat`)
- ✅ Limpieza integrada en el script de setup

> **Nota**: Las carpetas `__pycache__` y `.pytest_cache` se crean automáticamente cuando ejecutas Python o pytest. Esto es normal y necesario para el funcionamiento óptimo, pero no deben incluirse en el repositorio Git. Nuestro proyecto está configurado para manejar esto automáticamente.

### 📝 **Scripts de activación automáticos**
- ✅ `activar.bat` para Windows Command Prompt
- ✅ `activar.ps1` para Windows PowerShell
- ✅ Activación simplificada del entorno virtual

## 🚀 Inicio Rápido

### 1. Configuración automática (Recomendado)

```bash
# Ejecutar el script de configuración mejorado
python setup.py
```

Este script automáticamente:
- ✅ Crea el entorno virtual si no existe
- ✅ Verifica la instalación de Python
- ✅ Instala todas las dependencias
- ✅ Crea scripts de activación rápida
- ✅ Proporciona instrucciones detalladas

### 2. Activación rápida del entorno

**Opción A: Scripts automáticos**
```bash
# Windows Command Prompt
activar.bat

# Windows PowerShell
.\activar.ps1
```

**Opción B: Activación manual**
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.\venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

### 3. Verificar que el entorno está activo

Deberías ver `(venv)` al inicio del prompt:
```bash
(venv) PS C:\tu\proyecto>
```

### 4. Ejecutar código

```bash
# Programa principal
python src/main.py

# Pruebas unitarias
python -m pytest tests/ -v

# Jupyter Notebook
jupyter notebook notebooks/01_introduccion_python.ipynb
```

### 5. Desactivar entorno

```bash
deactivate
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

## 🛠️ Solución de Problemas

### ❓ **El entorno virtual no se activa**
```bash
# 1. Verificar que existe
dir venv\Scripts\         # Windows
ls venv/bin/              # Linux/Mac

# 2. Ejecutar configuración automática
python setup.py

# 3. Usar scripts de activación
activar.bat               # Windows CMD
.\activar.ps1            # PowerShell
```

### ❓ **Error de importación en las pruebas**
```bash
# Las pruebas usan importación simplificada
# Solo ejecuta:
python -m pytest tests/ -v
```

### ❓ **Falta algún paquete**
```bash
# Instalar dependencias automáticamente
python setup.py

# O manualmente
pip install -r requirements.txt
```

### ❓ **VS Code no reconoce el entorno virtual**
1. Abre VS Code en la carpeta del proyecto
2. Presiona `Ctrl+Shift+P`
3. Escribe "Python: Select Interpreter"
4. Selecciona: `.\venv\Scripts\python.exe`

### ❓ **Aparecen carpetas __pycache__ o .pytest_cache**
Esto es normal en Python, pero hay varias formas de limpiarlas:

```bash
# Opción 1: Script Python
python limpiar.py

# Opción 2: Script de lote (Windows)
limpiar.bat

# Opción 3: Configuración automática (incluye limpieza)
python setup.py

# Opción 4: Manual en PowerShell
Remove-Item -Path "__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".pytest_cache" -Recurse -Force -ErrorAction SilentlyContinue
```

> **💡 Tip**: Estas carpetas están configuradas para ocultarse automáticamente en VS Code y no se incluyen en Git.

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