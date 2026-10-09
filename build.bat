@echo off
rem Build in a clean virtual environment so unrelated packages (PyQt5, pygame, etc.) aren't bundled
if exist venv rmdir /s /q venv
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip pywebview pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed ^
  --name MinecraftDistanceCalculator ^
  --add-data "minecraft_distance_calculator.html;." app.py
echo.
echo Done. Your exe is in the "dist" folder.
pause
