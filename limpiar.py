#!/usr/bin/env python3
"""
Script de limpieza para el proyecto Python.
Elimina archivos y carpetas temporales como __pycache__ y .pytest_cache.
"""

import os
import shutil
import glob

def limpiar_proyecto():
    """Limpia archivos y carpetas temporales del proyecto."""
    print("🧹 Iniciando limpieza del proyecto...")
    
    # Obtener el directorio del proyecto (donde está este script)
    proyecto_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cambiar al directorio del proyecto
    os.chdir(proyecto_dir)
    
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
                print(f"  ❌ Error eliminando {pycache_path}: {e}")
    
    # Eliminar carpeta .pytest_cache
    pytest_cache = ".pytest_cache"
    if os.path.exists(pytest_cache):
        try:
            shutil.rmtree(pytest_cache)
            print(f"  ✅ Eliminado: {pytest_cache}")
            elementos_limpiados += 1
        except Exception as e:
            print(f"  ❌ Error eliminando {pytest_cache}: {e}")
    
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
                print(f"  ❌ Error eliminando {pyc_file}: {e}")
    
    # Eliminar archivos .pyo
    pyo_files = glob.glob("**/*.pyo", recursive=True)
    for pyo_file in pyo_files:
        if 'venv' not in pyo_file:
            try:
                os.remove(pyo_file)
                print(f"  ✅ Eliminado: {pyo_file}")
                elementos_limpiados += 1
            except Exception as e:
                print(f"  ❌ Error eliminando {pyo_file}: {e}")
    
    print(f"\n🎉 Limpieza completada. Se eliminaron {elementos_limpiados} elementos.")
    
    if elementos_limpiados == 0:
        print("✨ El proyecto ya estaba limpio.")

if __name__ == "__main__":
    limpiar_proyecto()
