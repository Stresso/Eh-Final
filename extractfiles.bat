@echo off
mkdir extracted
ChromeCacheView.exe -folder %appdata%\discord\Cache\Cache_Data /copycache "" "" /CopyFilesFolder "%~dp0\extracted"