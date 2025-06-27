#!/usr/bin/env python3
"""
Script de configuración inicial para el proyecto Python.
Automatiza la creación del entorno virtual e instalación de dependencias.
"""

import os
import sys
import subprocess
import platform

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando y maneja errores."""
    print(f"🔄 {descripcion}...")
    try:
        if platform.system() == "Windows":
            resultado = subprocess.run(comando, shell=True, check=True, 
                                     capture_output=True, text=True)
        else:
            resultado = subprocess.run(comando.split(), check=True, 
                                     capture_output=True, text=True)
        print(f"✅ {descripcion} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {descripcion}: {e}")
        if e.stdout:
            print(f"Salida: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def main():
    """Función principal de configuración."""
    print("🐍 Configuración del Proyecto Python")
    print("=" * 40)
    
    # Verificar Python
    print(f"🔍 Verificando Python...")
    print(f"Versión de Python: {sys.version}")
    
    # Crear entorno virtual
    if not os.path.exists("venv"):
        if platform.system() == "Windows":
            if not ejecutar_comando("python -m venv venv", "Creando entorno virtual"):
                print("❌ Error: No se pudo crear el entorno virtual")
                print("Verifica que Python esté instalado correctamente")
                return False
        else:
            if not ejecutar_comando("python3 -m venv venv", "Creando entorno virtual"):
                print("❌ Error: No se pudo crear el entorno virtual")
                print("Verifica que Python3 esté instalado correctamente")
                return False
    else:
        print("✅ El entorno virtual ya existe")
    
    # Verificar que el entorno virtual se creó correctamente
    if platform.system() == "Windows":
        venv_python = os.path.join("venv", "Scripts", "python.exe")
        venv_pip = os.path.join("venv", "Scripts", "pip.exe")
    else:
        venv_python = os.path.join("venv", "bin", "python")
        venv_pip = os.path.join("venv", "bin", "pip")
    
    if not os.path.exists(venv_python):
        print("❌ Error: El entorno virtual no se creó correctamente")
        return False
    
    # Activar entorno virtual e instalar dependencias
    if platform.system() == "Windows":
        pip_cmd = os.path.join("venv", "Scripts", "pip.exe")
        python_cmd = os.path.join("venv", "Scripts", "python.exe")
    else:
        pip_cmd = os.path.join("venv", "bin", "pip")
        python_cmd = os.path.join("venv", "bin", "python")
    
    # Actualizar pip
    ejecutar_comando(f"{python_cmd} -m pip install --upgrade pip", 
                    "Actualizando pip")
    
    # Instalar dependencias
    if os.path.exists("requirements.txt"):
        ejecutar_comando(f"{pip_cmd} install -r requirements.txt", 
                        "Instalando dependencias")
    
    # Verificar instalación
    print("\n🔍 Verificando instalación...")
    try:
        resultado = subprocess.run([python_cmd, "-c", 
                                  "import numpy, pandas, matplotlib, pytest; print('✅ Todos los paquetes principales están instalados')"],
                                 capture_output=True, text=True, check=True)
        print(resultado.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Error al verificar paquetes: {e}")
        print("Algunos paquetes pueden no estar instalados correctamente")
    except Exception as e:
        print(f"⚠️  Advertencia: {e}")
    
    # Verificar que los directorios del proyecto existen
    directorios_necesarios = ["src", "tests", "notebooks", "docs"]
    for directorio in directorios_necesarios:
        if not os.path.exists(directorio):
            print(f"⚠️  Directorio '{directorio}' no encontrado")
        else:
            print(f"✅ Directorio '{directorio}' existe")
    
    print("\n🎉 ¡Configuración completada!")
    print("\nPróximos pasos:")
    print("1. Activar el entorno virtual:")
    if platform.system() == "Windows":
        print("   .\\venv\\Scripts\\Activate.ps1")
        print("   # O en Command Prompt: .\\venv\\Scripts\\activate.bat")
    else:
        print("   source venv/bin/activate")
    print("2. Ejecutar el programa principal:")
    print(f"   {python_cmd} src/main.py")
    print("3. Ejecutar las pruebas:")
    print(f"   {python_cmd} -m pytest tests/")
    print("4. Abrir el notebook:")
    print(f"   {python_cmd} -m jupyter notebook notebooks/01_introduccion_python.ipynb")

if __name__ == "__main__":
    main()
