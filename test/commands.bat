@echo off
setlocal enabledelayedexpansion

:: Tên tệp chứa danh sách URL
set url_file=urls.txt

:: Tên tệp để lưu kết quả
set output_file=result.txt

:: Khởi tạo danh sách các lệnh hệ thống từ tệp urls.txt
set commands=
for /f %%i in (!url_file!) do (
    set command=C:\Users\namdi\ffuf.exe -u %%i/FUZZ -w C:\Users\namdi\Desktop\craw\path-tra.txt -c -t 10 -p 0.1-0.5 -fs 0
    set commands=!commands! !command!
)

:: Mở tệp với chế độ ghi nối (append)
echo. > %output_file%
for %%command in (!commands!) do (
    %%command% >> %output_file% 2>&1
)

echo Tất cả các lệnh đã thực thi xong và kết quả đã được ghi vào %output_file%
pause
