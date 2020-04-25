@echo off
set BUNDLE_DIR=%~dp0
set CLASSPATH="WEB-INF/classes"

for %%i in ("WEB-INF\lib\*.jar") do call :append "%%i"
goto okClasspath

:append
set CLASSPATH=%CLASSPATH%;%1
goto :eof

:okClasspath

set JAVA_OPTS=-Djava.awt.headless=true -Djava.net.preferIPv4Stack=true -Duser.timezone=GMT+08 -Duser.home=%BUNDLE_DIR%_data/

echo "Starting ..."
java %JAVA_OPTS% -cp %CLASSPATH% im.zhaojun.zfile.ZfileApplication
