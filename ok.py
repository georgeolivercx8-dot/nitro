import os
import webview

USERNAME = "NITRO"

class Api:
    def close_app(self):
        webview.windows[0].destroy()

file_path = os.path.abspath("index.html")

if not os.path.exists(file_path):
    print("ERROR: profile.html not found next to ok.py")
else:
    print("Launching:", file_path)
    webview.create_window(
        USERNAME,
        file_path,
        fullscreen=True,
        js_api=Api()
    )
    webview.start(debug=False)
