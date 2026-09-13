#!/bin/bash

echo ""
echo "============================================================"
echo "  Keck Microscopy Center Website Server"
echo "============================================================"
echo ""
echo "🌐 Server starting at: http://localhost:8000"
echo ""
echo "📝 Press Ctrl+C to stop the server"
echo ""

# Change to the script's directory
cd "$(dirname "$0")"

# Try to open in default browser
if command -v open &> /dev/null; then
    # macOS
    open "http://localhost:8000"
elif command -v xdg-open &> /dev/null; then
    # Linux
    xdg-open "http://localhost:8000"
fi

# Start the server
python3 -m http.server 8000
