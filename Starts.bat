@ECHO OFF
cls

:ESPECIFIC COMPUTER
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\Layout\st_editor.ui    -o .\Lib\Script\st_editor.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\Layout\st_preview.ui   -o .\Lib\Script\st_preview.py  

py.exe editor.py

