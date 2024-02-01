# /api/calculate.py
from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        # Aquí iría el código Python que quieres ejecutar
        start_date = data['startDate']
        end_date = data['endDate']
        # Simulando un cálculo con las fechas
        result = f"Procesado desde {start_date} hasta {end_date}"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(result.encode())
        return
