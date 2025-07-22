@echo off
echo 🧹 Limpiando archivos temporales del proyecto...

REM Limpiar carpetas __pycache__
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        if not "%%d"=="*venv*" (
            echo   ✅ Eliminando: %%d
            rmdir /s /q "%%d" 2>nul
        )
    )
)

REM Limpiar .pytest_cache
if exist ".pytest_cache" (
    echo   ✅ Eliminando: .pytest_cache
    rmdir /s /q ".pytest_cache" 2>nul
)

REM Limpiar .mypy_cache
if exist ".mypy_cache" (
    echo   ✅ Eliminando: .mypy_cache
    rmdir /s /q ".mypy_cache" 2>nul
)

REM Limpiar archivos .pyc
for /r . %%f in (*.pyc) do (
    if not "%%f"=="*venv*" (
        echo   ✅ Eliminando: %%f
        del "%%f" 2>nul
    )
)

REM Limpiar archivos .pyo
for /r . %%f in (*.pyo) do (
    if not "%%f"=="*venv*" (
        echo   ✅ Eliminando: %%f
        del "%%f" 2>nul
    )
)

echo.
echo ✨ Limpieza completada!
echo.
pause
