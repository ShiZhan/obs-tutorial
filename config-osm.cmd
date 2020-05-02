@echo off
rem Setup alias for using local configuration
set SCRIPT_DIR=%~dp0
@doskey osm=osm --osmconfig %SCRIPT_DIR%osm.conf $*

rem Create OSM configuration and save to 'osm.conf'
osm --osmconfig %SCRIPT_DIR%osm.conf config set-context osm-minio --provider=s3 --s3.access_key_id=hust --s3.secret_key=hust_obs --s3.endpoint=http://127.0.0.1:9000
osm --osmconfig %SCRIPT_DIR%osm.conf config view
