# Curso Python - Repositorio Colaborativo

Este repositorio contiene material educativo y ejercicios prácticos para el curso de Python, diseñado para trabajo colaborativo y aprendizaje efectivo.

## 📋 Estructura del Proyecto

```
Repositorio Curso Python/
├── src/                    # Código fuente principal
│   ├── __init__.py        # Configuración del paquete
│   ├── main.py            # Archivo principal con ejemplos
│   ├── utils.py           # Funciones de utilidad
│   ├── ejemplo_problematico.py  # Ejemplos para herramientas de análisis
│   └── ejemplo_tipos.py   # Ejemplos de anotaciones de tipo
├── tests/                  # Pruebas unitarias
│   ├── __init__.py
│   └── test_utils.py      # Pruebas para utils.py
├── notebooks/             # Jupyter Notebooks educativos
│   └── 01_introduccion_python.ipynb
├── .vscode/               # Configuraciones de VS Code
│   ├── settings.example.json  # Plantilla de configuración
│   ├── extensions.json   # Extensiones recomendadas
│   └── CONFIGURACION.md  # Guía detallada de configuración
├── docs/                  # Documentación
├── venv/                  # Entorno virtual (no incluido en Git)
├── .gitignore            # Archivos excluidos del control de versiones
├── activar.bat            # Script de activación (Windows CMD)
├── activar.ps1            # Script de activación (PowerShell)
├── limpiar.bat            # Script de limpieza (Windows)
├── limpiar.py             # Script de limpieza de archivos temporales
├── pyproject.toml         # Configuración del proyecto
├── requirements.txt       # Dependencias del proyecto
├── setup.py               # Script de configuración automática
└── README.md              # Este archivo
```

## 🚀 Inicio Rápido

### Paso 1: Obtener el Proyecto

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd "Repositorio Curso Python"
```

### Paso 2: Configuración del Entorno

#### Opción A: Configuración Automática (Recomendado)

```bash
# Ejecutar el script de configuración completa
python setup.py
```

**Este script automáticamente:**
- ✅ Crea el entorno virtual si no existe
- ✅ Verifica la instalación de Python
- ✅ Instala todas las dependencias
- ✅ Crea scripts de activación rápida
- ✅ Proporciona instrucciones detalladas

#### Opción B: Configuración Manual

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# Windows (Command Prompt)
.\venv\Scripts\activate.bat
# macOS/Linux
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Scripts de Activación Rápida

**Disponibles después de la configuración:**
```bash
# Windows Command Prompt
activar.bat

# Windows PowerShell
.\activar.ps1
```

**Verificar entorno activo:**
Deberías ver `(venv)` al inicio del prompt:
```bash
(venv) PS C:\tu\proyecto>
```

### Configurar VS Code

1. Abre el proyecto en VS Code
2. Instala las extensiones recomendadas (aparecerá notificación automática)
3. Copia `.vscode/settings.example.json` a `.vscode/settings.json`
4. Ajusta la ruta del intérprete según tu sistema operativo
5. **Lee `.vscode/CONFIGURACION.md`** para comprender cada configuración en detalle

### Ejecutar el Proyecto

```bash
# Programa principal
python src/main.py

# Ejecutar todas las pruebas
pytest tests/

# Iniciar Jupyter Notebook
jupyter notebook notebooks/01_introduccion_python.ipynb
```

## 🔧 Configuración Colaborativa

### ⚠️ Reglas para Colaboradores

**❌ NO incluir en Git:**
- `.vscode/settings.json` (configuraciones personales del IDE)
- `.vscode/launch.json` (configuraciones de debug personales)
- `venv/` (entorno virtual local)
- `__pycache__/`, `.pytest_cache/` y `.mypy_cache/` (archivos de cache)

**✅ SÍ incluir en Git:**
- `.vscode/settings.example.json` (plantilla compartida)
- `.vscode/extensions.json` (extensiones recomendadas)
- `.vscode/CONFIGURACION.md` (documentación de configuración)

### ¿Por qué esta estructura colaborativa?

1. **🔄 Flexibilidad**: Cada desarrollador personaliza su IDE sin conflictos
2. **🎯 Consistencia**: Configuraciones esenciales sincronizadas entre todos
3. **🌍 Compatibilidad**: Funciona en Windows, macOS y Linux
4. **👥 Colaboración**: Evita conflictos en diferentes entornos de desarrollo

### Extensiones VS Code Recomendadas

- **Python** (`ms-python.python`): Soporte completo para Python
- **Black Formatter** (`ms-python.black-formatter`): Formateo automático
- **Flake8** (`ms-python.flake8`): Análisis y linting de código
- **Jupyter** (`ms-toolsai.jupyter`): Soporte para notebooks
- **Pylint** (`ms-python.pylint`): Análisis estático avanzado
- **MyPy Type Checker** (`ms-python.mypy-type-checker`): Verificación de tipos

### Configuraciones Clave del IDE

- **🐍 Intérprete**: Configurado para usar el entorno virtual local
- **🧪 Testing**: Framework pytest configurado automáticamente
- **🎨 Formateo**: Black con línea máxima de 88 caracteres
- **📁 Análisis**: Directorio `src` incluido en el path de análisis
- **🙈 Exclusiones**: Archivos temporales y cache ocultos automáticamente

## 📚 Contenido Educativo

### Conceptos Python Implementados

- **📦 Estructura de paquetes** (archivos `__init__.py` explicados)
- **🔧 Configuración de entornos virtuales**
- **📝 Buenas prácticas de Git** (`.gitignore`, colaboración)
- **🧪 Testing con pytest**
- **📖 Documentación de código**
- **⚙️ Configuración de IDEs** para trabajo en equipo

### Módulos del Curso

#### 1. **`src/main.py`** - Programa Principal
- Punto de entrada con `if __name__ == "__main__"`
- Ejemplos de variables y tipos de datos
- Funciones básicas y estructuras de control
- Documentación educativa detallada

#### 2. **`src/utils.py`** - Funciones de Utilidad
- Cálculos matemáticos básicos
- Conversiones de unidades
- Estadísticas simples
- Ejemplos prácticos comentados

#### 3. **`tests/test_utils.py`** - Pruebas Unitarias
- Verificación de todas las funciones
- Casos de prueba variados y casos límite
- Manejo de excepciones
- Ejemplos de buenas prácticas en testing

#### 4. **`notebooks/01_introduccion_python.ipynb`** - Tutorial Interactivo
- Configuración paso a paso del entorno
- Conceptos fundamentales de Python
- Ejemplos ejecutables y experimentación

#### 5. **`src/ejemplo_problematico.py`** - Ejemplos para Herramientas de Análisis
- Código con problemas de estilo intencionales
- Ejemplos para demostrar Black, Flake8 y Pylint
- Variables mal nombradas y formateo inconsistente
- Ideal para aprender a usar herramientas de calidad de código

#### 6. **`src/ejemplo_tipos.py`** - Ejemplos de Anotaciones de Tipo
- Demostración de anotaciones de tipo en Python
- Ejemplos para MyPy type checker
- Funciones con y sin anotaciones de tipo
- Casos problemáticos y mejores prácticas

#### 7. **Archivos Destacados**
- **`src/__init__.py`**: Documentación completa sobre paquetes Python
- **`setup.py`**: Script de configuración automática mejorado
- **Scripts de activación**: `activar.bat` y `activar.ps1`

## 🛠️ Herramientas y Dependencias

### Dependencias Principales
```
numpy>=1.24.0          # Computación numérica
pandas>=2.0.0          # Análisis de datos
matplotlib>=3.7.0      # Visualización
requests>=2.31.0       # Peticiones HTTP
```

### Herramientas de Desarrollo
```
pytest>=7.4.0          # Framework de pruebas
black>=23.0.0          # Formateador de código
flake8>=6.0.0          # Linting y análisis
pylint>=2.17.0         # Análisis estático avanzado
```

### Entorno Jupyter
```
jupyter>=1.0.0         # Notebooks interactivos
ipykernel>=6.25.0      # Kernel de Python para Jupyter
```

## 🧹 Limpieza y Mantenimiento

### Scripts de Limpieza Disponibles

```bash
# Opción 1: Script Python multiplataforma
python limpiar.py

# Opción 2: Script Windows
limpiar.bat

# Opción 3: Limpieza integrada en setup
python setup.py  # Incluye limpieza automática
```

### Qué se limpia automáticamente:
- Carpetas `__pycache__/` (cache de Python)
- Carpetas `.pytest_cache/` (cache de pytest)
- Carpetas `.mypy_cache/` (cache de MyPy)
- Archivos `.pyc` compilados
- Archivos temporales del sistema

> **💡 Tip**: Estas carpetas se crean automáticamente y son normales. Están configuradas para ocultarse en VS Code y excluirse de Git.

## 📖 Trabajando con Notebooks

### Configuración Jupyter
```bash
# 1. Activar entorno virtual
.\activar.ps1  # Windows PowerShell
# o
activar.bat    # Windows CMD

# 2. Verificar instalación
jupyter --version

# 3. Iniciar Jupyter
jupyter notebook
# o
jupyter lab
```

### Uso del Notebook Educativo
1. Navega a `notebooks/01_introduccion_python.ipynb`
2. Ejecuta las celdas paso a paso
3. Experimenta con el código
4. Completa los ejercicios propuestos

## 🆘 Solución de Problemas Comunes

### ❓ **Problema: El entorno virtual no se activa**

**Diagnóstico:**
```bash
# Verificar que existe el entorno
dir venv\Scripts\         # Windows
ls venv/bin/              # Linux/Mac
```

**Soluciones:**
```bash
# 1. Ejecutar configuración automática
python setup.py

# 2. Usar scripts de activación
activar.bat               # Windows CMD
.\activar.ps1            # PowerShell

# 3. Activación manual
.\venv\Scripts\Activate.ps1  # PowerShell
.\venv\Scripts\activate.bat  # CMD
```

### ❓ **Problema: VS Code no encuentra el intérprete de Python**

**Solución paso a paso:**
1. Verifica que el entorno virtual esté activado (debe aparecer `(venv)`)
2. En VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter"
3. Selecciona: `.\venv\Scripts\python.exe` (Windows)
4. Si no aparece, ajusta en `.vscode/settings.json`:
   ```json
   {
     "python.defaultInterpreterPath": "./venv/Scripts/python.exe"
   }
   ```

### ❓ **Problema: Errores de importación en tests**

**Verificaciones:**
1. El directorio `src` debe estar en el path de análisis
2. Ejecutar tests desde la raíz del proyecto: `pytest tests/`
3. Verificar configuración en `.vscode/settings.json`:
   ```json
   {
     "python.analysis.extraPaths": ["./src"]
   }
   ```

### ❓ **Problema: VS Code no reconoce las extensiones**

**Solución:**
1. `Ctrl+Shift+P` → "Extensions: Show Recommended Extensions"
2. Instalar todas las extensiones sugeridas
3. Reiniciar VS Code si es necesario

### ❓ **Problema: Aparecen carpetas de cache (__pycache__, .pytest_cache, .mypy_cache)**

**Esto es completamente normal**, pero si molestan:

```bash
# Limpieza automática
python limpiar.py

# Limpieza manual (PowerShell)
Remove-Item -Path "__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".pytest_cache" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".mypy_cache" -Recurse -Force -ErrorAction SilentlyContinue
```

> **Nota**: Estas carpetas mejoran el rendimiento y se recrean automáticamente. Están configuradas para ocultarse en VS Code.

### ❓ **Problema: Jupyter no inicia o no encuentra el kernel**

**Solución:**
```bash
# 1. Activar entorno
.\activar.ps1

# 2. Instalar kernel
python -m ipykernel install --user --name venv --display-name "Python (venv)"

# 3. Iniciar Jupyter
jupyter notebook
```

## 🧪 Ejecutar Pruebas

### Comandos de Testing

```bash
# Todas las pruebas
pytest

# Con reporte de cobertura
pytest --cov=src

# Pruebas específicas
pytest tests/test_utils.py

# Verbose (información detallada)
pytest -v

# Parar en el primer fallo
pytest -x
```

## 🎨 Formateo y Calidad de Código

### Formateo Automático
```bash
# Formatear todo el código
black src/ tests/

# Verificar sin cambiar
black --check src/ tests/
```

### Análisis de Código
```bash
# Linting con Flake8
flake8 src/ tests/

# Análisis con Pylint
pylint src/

# Verificación de tipos con MyPy
mypy --strict src/
```

## 🤝 Flujo de Trabajo Colaborativo

### Primera Configuración
1. **Clonar el repositorio**
2. **Ejecutar `python setup.py`** para configuración automática
3. **Configurar VS Code** según las instrucciones
4. **Leer `.vscode/CONFIGURACION.md`** para entender cada configuración
5. **Instalar extensiones recomendadas**

### Trabajando en Equipo

**✅ Ventajas de nuestro setup:**
- Configuraciones personales no afectan a otros desarrolladores
- Configuraciones del proyecto se mantienen sincronizadas
- Compatible con diferentes sistemas operativos
- Archivos temporales no interfieren con Git

**📝 Convenciones del Código:**
- **Estilo**: Seguimos [PEP 8](https://pep8.org/)
- **Formateo**: Black automático
- **Nombres**: `snake_case` para funciones, `PascalCase` para clases
- **Documentación**: Docstrings obligatorios en todas las funciones

### Contribuir al Proyecto

```bash
# 1. Fork del repositorio
# 2. Crear rama para feature
git checkout -b feature/mi-nueva-funcionalidad

# 3. Hacer cambios y commits
git add .
git commit -m "feat: Agrega nueva funcionalidad"

# 4. Push y Pull Request
git push origin feature/mi-nueva-funcionalidad
```

## 📚 Recursos de Aprendizaje

### Documentación Oficial
- [Documentación de Python](https://docs.python.org/3/)
- [Guía de VS Code para Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Testing con pytest](https://docs.pytest.org/)

### Tutoriales Recomendados
- [Real Python](https://realpython.com/) - Tutoriales avanzados
- [Python Package Index (PyPI)](https://pypi.org/) - Repositorio de paquetes
- [Buenas prácticas de Git](https://git-scm.com/book/en/v2)

### Herramientas Adicionales
- [Black Playground](https://black.vercel.app/) - Probar formateo online
- [Python Tutor](https://pythontutor.com/) - Visualizar ejecución de código
- [Jupyter Documentation](https://jupyter.org/documentation) - Guías de Jupyter

---

**¡Feliz codificación! 🐍✨**

*Repositorio configurado para aprendizaje colaborativo y buenas prácticas de desarrollo en Python.*
