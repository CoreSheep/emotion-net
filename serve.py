#!/usr/bin/env python3
"""
Simple HTTP server for Emotion Net project
Serves the project locally on http://localhost:8080
"""

import http.server
import socketserver
import os
import webbrowser
import sys
from pathlib import Path

PORT = 8080
PROJECT_DIR = Path(__file__).parent

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

def run_server():
    os.chdir(PROJECT_DIR)

    handler = MyHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Emotion Net Server")
        print(f"=" * 50)
        print(f"📍 Serving files from: {PROJECT_DIR}")
        print(f"🌐 Open your browser at: http://localhost:{PORT}")
        print(f"=" * 50)
        print(f"\n✨ Press Ctrl+C to stop the server\n")

        try:
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
        except Exception as e:
            print(f"⚠️  Could not open browser: {e}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    run_server()
