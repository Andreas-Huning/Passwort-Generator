@echo off
echo =============================
echo  Python zu EXE Konvertierung
echo =============================

REM === Name des Hauptskripts ===
set SCRIPT_NAME=main.py

REM === Icon-Datei im Unterordner "assets" ===
set ICON_FILE=assets\favicon.ico

REM === Prüfen, ob PyInstaller installiert ist ===
where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo [FEHLER] PyInstaller ist nicht installiert!
    echo Installiere es mit: pip install pyinstaller
    pause
    exit /b
)

REM === Build-Info ===
echo [INFO] Baue EXE (GUI-Modus, keine Konsole)...

REM === Kompilierung mit PyInstaller ===
pyinstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --icon=%ICON_FILE% ^
    --add-data "assets\favicon.ico;assets" ^
    --paths=config ^
    --paths=utils ^
    %SCRIPT_NAME%

REM === Aufräumen ===
echo [INFO] Räume auf...
rmdir /s /q build
del /q %SCRIPT_NAME:.py=.spec%
for /d %%G in (__pycache__) do rmdir /s /q "%%G" >nul 2>nul
for /r %%F in (__pycache__\*) do del /q "%%F" >nul 2>nul

REM === Fertig ===
echo.
echo [FERTIG] Die EXE wurde erstellt: dist\%SCRIPT_NAME:.py=.exe%
pause
