@echo off
REM Virtual environmentni faollashtirish
call .venv\Scripts\activate.bat

REM Loyihaning ildiziga qaytish (agar kerak bo‘lsa)
cd /d %~dp0

REM main.pyni ishga tushirish
python main.py

