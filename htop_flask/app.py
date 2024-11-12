from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <html>
    <head><title>HTop Information</title></head>
    <body>
        <h1>Server Information</h1>
        <p><strong>Name:</strong> Kadapa Masif</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
