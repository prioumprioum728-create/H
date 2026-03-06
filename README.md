HelloCall Windows App

Requirements:
- Python 3.x installed
- PyInstaller installed (pip install pyinstaller)
- PyWebView installed (pip install pywebview)

Steps to create .exe:
1. Open Command Prompt in this folder.
2. Run:
   pyinstaller --onefile --windowed hellocall.py
3. Your standalone exe will be in the 'dist' folder.

To run:
- Double-click 'hellocall.exe' in the dist folder.
- Make sure all files are together during testing.
