@echo off
chcp 65001 >nul
REM Windows 批处理文件拼接脚本

setlocal enabledelayedexpansion

REM 配置
set "INPUT_DIR=E:\Python程序设计\上机考试复习"
set "OUTPUT_FILE=E:\Python程序设计\上机考试复习\merged.py"
set "FILE_EXT=*.py"

echo 开始拼接文件...
echo 输入目录: %INPUT_DIR%
echo 输出文件: %OUTPUT_FILE%
echo 文件类型: %FILE_EXT%

REM 检查目录是否存在
if not exist "%INPUT_DIR%" (
    echo 错误: 目录 %INPUT_DIR% 不存在
    pause
    exit /b 1
)

REM 清空输出文件
type nul > "%OUTPUT_FILE%"

set COUNT=0

REM 处理每个文件
for %%f in ("%INPUT_DIR%\%FILE_EXT%") do (
    echo 处理: %%~nxf
    
    REM 添加分隔符
    echo. >> "%OUTPUT_FILE%"
    echo ======================================== >> "%OUTPUT_FILE%"
    echo 文件: %%~nxf >> "%OUTPUT_FILE%"
    echo ======================================== >> "%OUTPUT_FILE%"
    echo. >> "%OUTPUT_FILE%"
    
    REM 追加文件内容
    type "%%f" >> "%OUTPUT_FILE%"
    
    set /a COUNT+=1
)

echo.
echo 完成!
echo 共处理 %COUNT% 个文件
for %%F in ("%OUTPUT_FILE%") do set "SIZE=%%~zF"
echo 输出文件大小: %SIZE% 字节

pause