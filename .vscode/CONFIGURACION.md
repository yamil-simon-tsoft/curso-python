# 🔧 Guía de Configuración de VS Code

Este archivo explica cada configuración en `settings.example.json` para ayudar a los colaboradores a entender y personalizar su entorno de desarrollo.

## 📋 Instrucciones de Uso

1. Copia `settings.example.json` a `settings.json`
2. Ajusta las configuraciones según tu sistema operativo y preferencias
3. Instala las extensiones recomendadas desde `extensions.json`

```bash
# Copiar configuración
copy .vscode\settings.example.json .vscode\settings.json
```

## 🐍 Configuración del Intérprete de Python

```json
"python.defaultInterpreterPath": "./venv/Scripts/python.exe"
```

**📍 Ajustar según tu sistema operativo:**
- **Windows**: `"./venv/Scripts/python.exe"`
- **macOS/Linux**: `"./venv/bin/python"`

**¿Qué hace?** Le dice a VS Code dónde encontrar el intérprete de Python del entorno virtual.

## 🔄 Activación del Entorno Virtual

```json
"python.terminal.activateEnvironment": true,
"python.terminal.activateEnvInCurrentTerminal": true
```

**¿Qué hace?** Activa automáticamente el entorno virtual cuando abres una terminal en VS Code.

## 🔍 Configuración de Linting

```json
"python.linting.enabled": true,
"python.linting.pylintEnabled": false,
"python.linting.flake8Enabled": false,
"python.linting.banditEnabled": false,
"python.linting.mypyEnabled": false
```

**🎯 Personalizable:** Cada desarrollador puede habilitar/deshabilitar según sus preferencias.

**Opciones populares:**
- **pylint**: Análisis completo y estricto
- **flake8**: Verificación de estilo PEP 8
- **mypy**: Verificación de tipos
- **bandit**: Análisis de seguridad

## 🧠 Análisis de Código

```json
"python.analysis.autoImportCompletions": true,
"python.analysis.extraPaths": ["./src"]
```

**¿Qué hace?**
- `autoImportCompletions`: Sugiere imports automáticamente
- `extraPaths`: Incluye el directorio `src/` para que reconozca los imports del proyecto

**⚠️ IMPORTANTE:** `extraPaths` es esencial para que funcionen las pruebas y los imports.

## 🎨 Formateo de Código

```json
"python.formatting.provider": "black",
"python.formatting.blackArgs": ["--line-length=88"]
```

**🎯 Personalizable:** Puedes cambiar el formateador según tu preferencia.

**Opciones:**
- **black**: Formateador popular y opinionado
- **autopep8**: Más configurable
- **yapf**: Altamente personalizable

## 🧪 Configuración de Testing

```json
"python.testing.pytestEnabled": true,
"python.testing.unittestEnabled": false,
"python.testing.pytestArgs": ["tests"]
```

**🚨 ESENCIAL:** Estas configuraciones son importantes para el proyecto.

**¿Qué hace?**
- Habilita pytest como framework de testing
- Deshabilita unittest
- Define `tests/` como directorio de pruebas

## 📁 Asociaciones de Archivos

```json
"files.associations": {
    "*.py": "python"
}
```

**¿Qué hace?** Asegura que VS Code reconozca todos los archivos `.py` como Python.

## 🙈 Exclusiones de Archivos

```json
"files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/venv": true,
    "**/*.pyc": true
},
"search.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/venv": true,
    "**/*.pyc": true
}
```

**¿Qué hace?** Oculta archivos temporales y de cache para mantener limpio el explorador de archivos.

**Archivos excluidos:**
- `__pycache__/`: Cache de Python
- `.pytest_cache/`: Cache de pytest  
- `venv/`: Entorno virtual
- `*.pyc`: Archivos compilados de Python

## ✨ Configuraciones del Editor

```json
"editor.formatOnSave": true,
"editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
}
```

**🎯 Personalizable:** Ajusta según tus preferencias de trabajo.

**¿Qué hace?**
- `formatOnSave`: Formatea automáticamente el código al guardar
- `organizeImports`: Organiza y limpia los imports al guardar

## 📓 Jupyter Notebooks

```json
"jupyter.defaultKernel": "python3"
```

**¿Qué hace?** Configura el kernel por defecto para Jupyter Notebooks.

## 🔧 Personalización Recomendada

### Para principiantes:
```json
{
    // Configuración mínima
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe", // Ajustar OS
    "python.terminal.activateEnvironment": true,
    "python.analysis.extraPaths": ["./src"],
    "python.testing.pytestEnabled": true
}
```

### Para desarrolladores avanzados:
```json
{
    // Configuración completa con linting
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    }
}
```

## 🆘 Solución de Problemas

### ❌ VS Code no encuentra el intérprete
**Solución:** Ajusta `python.defaultInterpreterPath` según tu SO.

### ❌ Los imports no funcionan en las pruebas
**Solución:** Verifica que `python.analysis.extraPaths` incluya `"./src"`.

### ❌ No aparecen las pruebas en el panel de Testing
**Solución:** Asegúrate de que `python.testing.pytestEnabled` esté en `true`.

### ❌ El código no se formatea automáticamente
**Solución:** 
1. Instala la extensión Black Formatter
2. Verifica que `editor.formatOnSave` esté en `true`

## 📚 Extensiones Recomendadas

Ver `extensions.json` para la lista completa de extensiones que complementan esta configuración.

---

**💡 Tip:** Después de hacer cambios en `settings.json`, reinicia VS Code para asegurar que se apliquen todas las configuraciones.
