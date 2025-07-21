# Curso Python - Repositorio Colaborativo

Este repositorio contiene material educativo y ejercicios prácticos para el curso de Python.

## � Estructura del Proyecto

```
Repositorio Curso Python/
├── src/                    # Código fuente principal
│   ├── __init__.py        # Configuración del paquete
│   ├── main.py            # Archivo principal
│   ├── utils.py           # Funciones de utilidad
│   └── script.py          # Script generador de Excel
├── tests/                  # Pruebas unitarias
│   ├── __init__.py
│   └── test_utils.py      # Pruebas para utils.py
├── notebooks/             # Jupyter Notebooks educativos
│   └── 01_introduccion_python.ipynb
├── .vscode/               # Configuraciones de VS Code
│   ├── settings.example.json  # Plantilla de configuración
│   └── extensions.json   # Extensiones recomendadas
├── docs/                  # Documentación
├── venv/                  # Entorno virtual (no incluido en Git)
├── .gitignore            # Archivos excluidos del control de versiones
├── pyproject.toml        # Configuración del proyecto
├── requirements.txt      # Dependencias
├── setup.py              # Script de configuración
└── README.md             # Este archivo
```

## 🚀 Configuración Inicial

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd "Repositorio Curso Python"
```

### 2. Crear entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
# o ejecutar:
python setup.py
```

### 4. Configurar VS Code

#### Opción A: Configuración automática
1. Abre el proyecto en VS Code
2. Instala las extensiones recomendadas (aparecerá una notificación)
3. Copia `.vscode/settings.example.json` a `.vscode/settings.json`
4. Ajusta la ruta del intérprete según tu sistema operativo

#### Opción B: Configuración manual
```bash
# Copiar configuración de ejemplo
copy .vscode\settings.example.json .vscode\settings.json

# Editar según tu sistema operativo:
# Windows: "./venv/Scripts/python.exe"
# macOS/Linux: "./venv/bin/python"
```

## 🔧 Configuraciones del IDE

### Extensiones Recomendadas
- **Python**: Soporte completo para Python
- **Black Formatter**: Formateo automático de código
- **Flake8**: Linting y análisis de código
- **Jupyter**: Soporte para notebooks
- **Pylint**: Análisis adicional de código
- **MyPy**: Verificación de tipos

### Configuraciones Importantes
- **Intérprete**: Configurado para usar el entorno virtual local
- **Testing**: Configurado para usar pytest
- **Formateo**: Black con línea máxima de 88 caracteres
- **Análisis**: Incluye el directorio `src` en el path
- **Exclusiones**: Oculta archivos temporales y cache

## 📝 Archivos de Configuración

### ⚠️ Importante para Colaboradores

**NO subir al repositorio:**
- `.vscode/settings.json` (configuraciones personales)
- `.vscode/launch.json` (configuraciones de debug personales)
- `venv/` (entorno virtual)
- `__pycache__/` (archivos de cache)
- `*.xlsx` (archivos Excel generados)

**SÍ incluir en el repositorio:**
- `.vscode/settings.example.json` (plantilla compartida)
- `.vscode/extensions.json` (extensiones recomendadas)
- `requirements.txt` (dependencias del proyecto)

### ¿Por qué esta estructura?

1. **Flexibilidad**: Cada desarrollador puede tener sus preferencias personales
2. **Consistencia**: Las configuraciones esenciales del proyecto se mantienen
3. **Compatibilidad**: Funciona en Windows, macOS y Linux
4. **Colaboración**: Facilita el trabajo en equipo sin conflictos

## 🏃‍♂️ Ejecutar el Proyecto

### Archivo Principal
```bash
cd src
python main.py
```

### Script Generador de Excel
```bash
cd src
python script.py
```

### Ejecutar Tests
```bash
pytest tests/
```

### Activar entorno virtual
```bash
# Windows PowerShell
.\activar.ps1

# Windows CMD
activar.bat

# Manual
venv\Scripts\activate
```

## 🤝 Colaboración

### Primera vez trabajando en el proyecto
1. Clona el repositorio
2. Configura tu entorno virtual
3. Copia `settings.example.json` a `settings.json`
4. Ajusta las configuraciones según tu sistema
5. Instala las extensiones recomendadas

### Trabajando en equipo
- Las configuraciones personales del IDE no se sincronizarán
- Las configuraciones esenciales del proyecto sí se mantendrán
- Cada desarrollador puede personalizar su experiencia sin afectar a otros
- Los archivos generados (Excel, cache) no se suben al repositorio

### Resolución de problemas comunes

#### "No se encuentra el intérprete de Python"
1. Verifica que el entorno virtual esté activado
2. Ajusta la ruta en `.vscode/settings.json`:
   - Windows: `"./venv/Scripts/python.exe"`
   - macOS/Linux: `"./venv/bin/python"`

#### "Errores de importación en tests"
1. Verifica que `python.analysis.extraPaths` incluya `"./src"`
2. Ejecuta tests desde la raíz del proyecto

#### "VS Code no reconoce las extensiones"
1. Abre la paleta de comandos (Ctrl+Shift+P)
2. Ejecuta "Extensions: Show Recommended Extensions"
3. Instala las extensiones sugeridas

## 📚 Contenido Educativo

### Conceptos aprendidos
- **Estructura de paquetes Python** (archivos `__init__.py`)
- **Configuración de entornos virtuales**
- **Buenas prácticas de Git** (`.gitignore`, colaboración)
- **Testing con pytest**
- **Documentación de código**
- **Configuración de IDEs** para trabajo colaborativo

### Archivos destacados
- `src/main.py`: Ejemplo de punto de entrada con `if __name__ == "__main__"`
- `src/__init__.py`: Documentación completa sobre paquetes Python
- `script.py`: Generación de archivos Excel con `openpyxl`

## 📚 Recursos Adicionales

- [Documentación de Python](https://docs.python.org/3/)
- [Guía de VS Code para Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Buenas prácticas de Git](https://git-scm.com/book/en/v2)
- [Testing con pytest](https://docs.pytest.org/)

---

**¡Feliz codificación! 🐍✨**
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