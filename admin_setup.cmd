@echo off
REM ----------------------------------------------------------------------
REM |
REM |  admin_setup.cmd
REM |
REM |  David Brownell <db@DavidBrownell.com>
REM |      2019-04-16 21:54:19
REM |
REM ----------------------------------------------------------------------
REM |
REM |  Copyright David Brownell 2019
REM |  Distributed under the Boost Software License, Version 1.0. See
REM |  accompanying file LICENSE_1_0.txt or copy at
REM |  http://www.boost.org/LICENSE_1_0.txt.
REM |
REM ----------------------------------------------------------------------
REM Setup activites that require admin access

regsvr32 /s "%~dp0Tools\Performance Tools\v16.0.0\Windows\Team Tools\Performance Tools\msdia140.dll"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Unable to register "%~dp0Tools\Performance Tools\v16.0.0\Windows\Team Tools\Performance Tools\msdia140.dll"
    exit /B %ERRORLEVEL%
)

echo This file is used to communicate that admin_setup has been run and completed successfully. Please do not remove this file, as it will cause other tools to prompt you to run admin_setup.cmd again. > "%~dp0admin_setup.complete"

echo.
echo.
echo The setup activities were successful - you may close this command prompt.
echo.
echo.
