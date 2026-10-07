@echo off
title AutoFix - Servidor Django
echo ====================================================
echo   Iniciando Proyecto AutoFix (Django)
echo ====================================================
echo.

echo [1/3] Activando entorno virtual (.venv)...
call "%~dp0.venv\Scripts\activate.bat"

echo [2/3] Entrando a la carpeta autofix_project...
cd /d "%~dp0autofix_project"

echo [3/3] Levantando servidor local (runserver)...
echo Presiona CTRL+C para detener el servidor.
echo.
python manage.py runserver

pause
