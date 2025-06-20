@echo off

echo Installing dependencies...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies
    pause
    exit /b
)

echo.

python -m geektrust sample_input\input1.txt

echo.

python -m geektrust sample_input\input2.txt



echo.
echo Done!
pause
