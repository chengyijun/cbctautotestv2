@echo off
echo =========package start=========
rd /s/q build
rd /s/q dist
d:\venvs\py39\Scripts\pyinstaller.exe main.spec
echo =========package end=========
