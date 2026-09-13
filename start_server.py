#!/usr/bin/env python3
"""
Simple HTTP Server for Keck Microscopy Center Website
Run this script to start a local web server at http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Change to that directory
    os.chdir(script_dir)
    
    print("=" * 60)
    print("🌐 Keck Microscopy Center Website Server")
    print("=" * 60)
    print(f"\n✅ Server starting at: http://localhost:{PORT}")
    print(f"📁 Serving files from: {script_dir}")
    print("\n📝 Press Ctrl+C to stop the server\n")
    
    # Create server
    with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
        # Try to open in default browser
        try:
            webbrowser.open(f'http://localhost:{PORT}')
            print(f"🌍 Opening website in your default browser...\n")
        except:
            print(f"💡 Open your browser and go to: http://localhost:{PORT}\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✋ Server stopped. Goodbye!")
            exit(0)

if __name__ == "__main__":
    main()
