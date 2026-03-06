import webview
import os

# Path to your HTML file
html_file = os.path.join(os.path.dirname(__file__), "hellocall.html")

# Create a window
webview.create_window("HelloCall Dialer", html_file, width=400, height=600)
webview.start()
