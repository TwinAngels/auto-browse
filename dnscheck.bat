REM @echo off
del results.txt 2>nul
for /f "delims=" %%a in (urls.txt) do nslookup %%a >> results.txt
exit