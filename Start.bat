@ECHO OFF
cls
 
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\Layout\st_preview.ui   -o .\Lib\Script\st_preview.py  
%localappdata%\programs\Python\Python37-32\Scripts\pyuic5.exe -x .\Lib\Layout\st_edit.ui      -o .\Lib\Script\st_edit.py  
py.exe editor.py

REM pyuic5 -x .\Lib\Layout\st_preview.ui   -o .\Lib\Script\st_preview.py  
REM pyuic5 -x .\Lib\Layout\st_edit.ui      -o .\Lib\Script\st_edit.py  
REM python editor.py