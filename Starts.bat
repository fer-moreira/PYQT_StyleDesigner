@ECHO OFF
cls
 
REM %localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\Layout\st_preview.ui   -o .\Lib\Script\st_preview.py  
REM py.exe editor.py

pyuic5 -x .\Lib\Layout\st_preview.ui   -o .\Lib\Script\st_preview.py  
python editor.py