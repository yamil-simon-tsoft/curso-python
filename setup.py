#!/usr/bin/env python3
"""
Script de configuración inicial para el proyecto Python.
Automatiza la creación del entorno virtual e instalación de dependencias.
"""

import os
import sys
import subprocess
import platform
import shutil
import glob

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

def verificar_entorno_virtual():
    """Verifica si el entorno virtual está correctamente configurado."""
    print("\n🔍 Verificando entorno virtual...")
    
    # Verificar carpeta venv
    if not os.path.exists("venv"):
        print("❌ Carpeta 'venv' no existe")
        return False
    
    # Verificar ejecutables según el sistema operativo
    if platform.system() == "Windows":
        python_exe = os.path.join("venv", "Scripts", "python.exe")
        pip_exe = os.path.join("venv", "Scripts", "pip.exe")
        activate_script = os.path.join("venv", "Scripts", "Activate.ps1")
        activate_bat = os.path.join("venv", "Scripts", "activate.bat")
    else:
        python_exe = os.path.join("venv", "bin", "python")
        pip_exe = os.path.join("venv", "bin", "pip")
        activate_script = os.path.join("venv", "bin", "activate")
        activate_bat = None
    
    # Verificar archivos esenciales
    archivos_verificar = [
        (python_exe, "Python del entorno virtual"),
        (pip_exe, "Pip del entorno virtual"),
        (activate_script, "Script de activación principal")
    ]
    
    if activate_bat:
        archivos_verificar.append((activate_bat, "Script de activación CMD"))
    
    todos_ok = True
    for archivo, descripcion in archivos_verificar:
        if os.path.exists(archivo):
            print(f"✅ {descripcion}: OK")
        else:
            print(f"❌ {descripcion} no encontrado: {archivo}")
            todos_ok = False
    
    # Verificar tamaño del entorno virtual
    try:
        venv_size = sum(
            os.path.getsize(os.path.join(dirpath, filename))
            for dirpath, dirnames, filenames in os.walk("venv")
            for filename in filenames
        ) / (1024 * 1024)  # MB
        print(f"📊 Tamaño del entorno virtual: {venv_size:.1f} MB")
    except Exception as e:
        print(f"⚠️  No se pudo calcular el tamaño: {e}")
    
    return todos_ok

def verificar_python_entorno():
    """Verifica que Python del entorno virtual funciona correctamente."""
    print("\n🐍 Verificando Python del entorno virtual...")
    
    if platform.system() == "Windows":
        python_cmd = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_cmd = os.path.join("venv", "bin", "python")
    
    try:
        # Verificar versión
        resultado = subprocess.run([python_cmd, "--version"], 
                                 capture_output=True, text=True, check=True)
        print(f"✅ Versión: {resultado.stdout.strip()}")
        
        # Verificar ruta del ejecutable
        resultado = subprocess.run([python_cmd, "-c", "import sys; print(sys.executable)"], 
                                 capture_output=True, text=True, check=True)
        print(f"✅ Ejecutable: {resultado.stdout.strip()}")
        
        # Verificar que es del entorno virtual
        if "venv" in resultado.stdout:
            print("✅ Está usando el Python del entorno virtual")
        else:
            print("⚠️  Puede estar usando Python del sistema")
            
        return True
    except Exception as e:
        print(f"❌ Error al verificar Python del entorno: {e}")
        return False

def mostrar_instrucciones_uso():
    """Muestra instrucciones claras de cómo usar el entorno virtual."""
    print("\n" + "="*60)
    print("📋 INSTRUCCIONES DE USO DEL ENTORNO VIRTUAL")
    print("="*60)
    
    if platform.system() == "Windows":
        print("\n1️⃣  ACTIVAR entorno virtual:")
        print("    💻 PowerShell (recomendado):")
        print("       .\\venv\\Scripts\\Activate.ps1")
        print("    💻 Command Prompt:")
        print("       .\\venv\\Scripts\\activate.bat")
        print("    💻 Git Bash:")
        print("       source venv/Scripts/activate")
        
        print("\n2️⃣  VERIFICAR que está activo:")
        print("    ✓ Verás (venv) al inicio del prompt")
        print("    ✓ Ejecuta: where python")
        print("    ✓ Debería mostrar: ...\\venv\\Scripts\\python.exe")
        
    else:
        print("\n1️⃣  ACTIVAR entorno virtual:")
        print("    💻 Terminal:")
        print("       source venv/bin/activate")
        
        print("\n2️⃣  VERIFICAR que está activo:")
        print("    ✓ Verás (venv) al inicio del prompt")
        print("    ✓ Ejecuta: which python")
        print("    ✓ Debería mostrar: .../venv/bin/python")
    
    print("\n3️⃣  EJECUTAR tu código:")
    print("    🐍 python src/main.py")
    print("    🧪 python -m pytest tests/")
    print("    📓 jupyter notebook")
    
    print("\n4️⃣  DESACTIVAR entorno:")
    print("    ⏹️  deactivate")
    print("    ✓ El prompt volverá a la normalidad")
    
    print("\n5️⃣  VERIFICAR ESTADO:")
    print("    🔍 echo $VIRTUAL_ENV     # Linux/Mac")
    print("    🔍 echo %VIRTUAL_ENV%    # Windows CMD")
    print("    🔍 $env:VIRTUAL_ENV      # Windows PowerShell")
    
    print("\n" + "="*60)

def crear_script_activacion():
    """Crea un script de activación simplificado."""
    if platform.system() == "Windows":
        script_content = """@echo off
echo 🐍 Activando entorno virtual de Python...
call venv\\Scripts\\activate.bat
echo ✅ Entorno virtual activado
echo 💡 Para desactivar: deactivate
"""
        with open("activar.bat", "w", encoding="utf-8") as f:
            f.write(script_content)
        print("✅ Creado script 'activar.bat' para activación rápida")
        
        # También crear para PowerShell
        ps_script = """Write-Host "🐍 Activando entorno virtual de Python..." -ForegroundColor Green
& .\\venv\\Scripts\\Activate.ps1
Write-Host "✅ Entorno virtual activado" -ForegroundColor Green
Write-Host "💡 Para desactivar: deactivate" -ForegroundColor Yellow
"""
        with open("activar.ps1", "w", encoding="utf-8") as f:
            f.write(ps_script)
        print("✅ Creado script 'activar.ps1' para PowerShell")
        
    else:
        script_content = """#!/bin/bash
echo "🐍 Activando entorno virtual de Python..."
source venv/bin/activate
echo "✅ Entorno virtual activado"
echo "💡 Para desactivar: deactivate"
"""
        with open("activar.sh", "w") as f:
            f.write(script_content)
        os.chmod("activar.sh", 0o755)  # Hacer ejecutable
        print("✅ Creado script 'activar.sh' para activación rápida")

def limpiar_archivos_temporales():
    """Limpia archivos y carpetas temporales del proyecto."""
    print("\n🧹 Limpiando archivos temporales...")
    
    elementos_limpiados = 0
    
    # Buscar y eliminar carpetas __pycache__
    for root, dirs, files in os.walk('.'):
        # Evitar entrar en el entorno virtual
        if 'venv' in root or '.git' in root:
            continue
            
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"  ✅ Eliminado: {pycache_path}")
                elementos_limpiados += 1
            except Exception as e:
                print(f"  ⚠️  Error eliminando {pycache_path}: {e}")
    
    # Eliminar carpeta .pytest_cache
    pytest_cache = ".pytest_cache"
    if os.path.exists(pytest_cache):
        try:
            shutil.rmtree(pytest_cache)
            print(f"  ✅ Eliminado: {pytest_cache}")
            elementos_limpiados += 1
        except Exception as e:
            print(f"  ⚠️  Error eliminando {pytest_cache}: {e}")
    
    # Eliminar archivos .pyc individuales
    pyc_files = glob.glob("**/*.pyc", recursive=True)
    for pyc_file in pyc_files:
        # Evitar archivos en venv
        if 'venv' not in pyc_file:
            try:
                os.remove(pyc_file)
                print(f"  ✅ Eliminado: {pyc_file}")
                elementos_limpiados += 1
            except Exception as e:
                print(f"  ⚠️  Error eliminando {pyc_file}: {e}")
    
    if elementos_limpiados > 0:
        print(f"✅ Limpieza completada. Se eliminaron {elementos_limpiados} elementos.")
    else:
        print("✅ El proyecto ya estaba limpio.")

def main():
    """Función principal de configuración."""
    print("🐍 CONFIGURACIÓN DEL PROYECTO PYTHON")
    print("=" * 50)
    
    # Verificar Python del sistema
    print(f"🔍 Verificando Python del sistema...")
    print(f"   Versión: {sys.version}")
    print(f"   Ejecutable: {sys.executable}")
    
    # Crear entorno virtual
    print(f"\n📦 Configurando entorno virtual...")
    if not os.path.exists("venv"):
        if platform.system() == "Windows":
            if not ejecutar_comando("python -m venv venv", "Creando entorno virtual"):
                print("❌ Error: No se pudo crear el entorno virtual")
                print("💡 Verifica que Python esté instalado correctamente")
                return False
        else:
            if not ejecutar_comando("python3 -m venv venv", "Creando entorno virtual"):
                print("❌ Error: No se pudo crear el entorno virtual")
                print("💡 Verifica que Python3 esté instalado correctamente")
                return False
    else:
        print("✅ El entorno virtual ya existe")
    
    # Verificación completa del entorno virtual
    if not verificar_entorno_virtual():
        print("❌ Error: Problemas con el entorno virtual")
        return False
    
    # Verificar Python del entorno virtual
    if not verificar_python_entorno():
        print("❌ Error: Problemas con Python del entorno virtual")
        return False
    
    # Determinar comandos según el sistema operativo
    if platform.system() == "Windows":
        pip_cmd = os.path.join("venv", "Scripts", "pip.exe")
        python_cmd = os.path.join("venv", "Scripts", "python.exe")
    else:
        pip_cmd = os.path.join("venv", "bin", "pip")
        python_cmd = os.path.join("venv", "bin", "python")
    
    # Actualizar pip
    ejecutar_comando(f'"{python_cmd}" -m pip install --upgrade pip', 
                    "Actualizando pip")
    
    # Instalar dependencias
    if os.path.exists("requirements.txt"):
        ejecutar_comando(f'"{pip_cmd}" install -r requirements.txt', 
                        "Instalando dependencias")
    else:
        print("⚠️  Archivo requirements.txt no encontrado")
        print("💡 Se instalarán paquetes básicos...")
        paquetes_basicos = ["pytest", "numpy", "pandas", "matplotlib", "jupyter"]
        for paquete in paquetes_basicos:
            ejecutar_comando(f'"{pip_cmd}" install {paquete}', 
                           f"Instalando {paquete}")
    
    # Verificar instalación de paquetes
    print("\n🔍 Verificando paquetes instalados...")
    try:
        resultado = subprocess.run([python_cmd, "-c", 
                                  "import numpy, pandas, matplotlib, pytest; print('✅ Todos los paquetes principales están instalados correctamente')"],
                                 capture_output=True, text=True, check=True)
        print(resultado.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Error al verificar paquetes: {e}")
        print("💡 Algunos paquetes pueden no estar instalados correctamente")
        # Mostrar paquetes instalados
        try:
            resultado = subprocess.run([pip_cmd, "list"], 
                                     capture_output=True, text=True, check=True)
            print("📋 Paquetes instalados:")
            print(resultado.stdout)
        except:
            pass
    
    # Verificar estructura de directorios
    print("\n📁 Verificando estructura del proyecto...")
    directorios_necesarios = ["src", "tests", "notebooks", "docs"]
    for directorio in directorios_necesarios:
        if not os.path.exists(directorio):
            print(f"⚠️  Directorio '{directorio}' no encontrado")
            try:
                os.makedirs(directorio, exist_ok=True)
                print(f"✅ Directorio '{directorio}' creado")
            except Exception as e:
                print(f"❌ Error creando '{directorio}': {e}")
        else:
            print(f"✅ Directorio '{directorio}' existe")
    
    # Limpiar archivos temporales
    limpiar_archivos_temporales()
    
    # Crear scripts de activación
    print("\n🔧 Creando scripts de activación...")
    crear_script_activacion()
    
    # Mensaje final
    print("\n🎉 ¡CONFIGURACIÓN COMPLETADA EXITOSAMENTE!")
    
    # Mostrar instrucciones detalladas
    mostrar_instrucciones_uso()
    
    # Comandos de ejemplo
    print("\n💡 COMANDOS DE EJEMPLO:")
    print(f"   📝 Editar código:     code src/main.py")
    print(f"   🏃 Ejecutar programa: {python_cmd} src/main.py")
    print(f"   🧪 Ejecutar tests:    {python_cmd} -m pytest tests/")
    print(f"   📊 Ver paquetes:      {pip_cmd} list")
    print(f"   🔧 Instalar paquete:  {pip_cmd} install nombre_paquete")
    
    return True

if __name__ == "__main__":
    try:
        if main():
            print("\n✅ Setup completado correctamente")
            sys.exit(0)
        else:
            print("\n❌ Setup falló")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Setup cancelado por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
