# Quick Start Guide

## 🔴 CRITICAL: Do NOT Open HTML Files Directly!

**Do NOT** double-click HTML files to open them. This will NOT work!

Navigation links require an HTTP server to function properly.

## ✅ Correct Startup Methods

### Method 1: Easiest (Recommended)

#### For Windows Users:
1. Save all files to a folder
2. Find `start_server.bat` 
3. **Double-click** `start_server.bat`
4. Website automatically opens in your browser ✅

#### For Mac Users:
1. Save all files to a folder
2. Open Terminal (Applications > Utilities > Terminal)
3. Run: `bash start_server.sh`
4. Website automatically opens in your browser

#### For Linux Users:
1. Save all files to a folder
2. Open Terminal
3. Navigate: `cd /path/to/folder`
4. Run: `bash start_server.sh`
5. Website automatically opens in your browser

### Method 2: Manual Server Startup

#### Windows (Command Prompt):
```
# Navigate to folder
cd C:\Users\YourName\Downloads\keck-website

# Start server
python -m http.server 8000
```

#### Mac/Linux (Terminal):
```bash
# Navigate to folder
cd ~/Downloads/keck-website

# Start server
python3 -m http.server 8000
```

Then open in browser: **http://localhost:8000**

## 🎯 What You'll See:

✅ All navigation links now work
✅ Home button works
✅ Equipment page loads
✅ Services & Rates page loads
✅ Schedule page with working booking form
✅ Policies page loads
✅ Contact page loads
✅ All email buttons work
✅ Perfect navigation between all pages

## ❓ Troubleshooting

**Q: Which Python version should I use?**
A: Python 3 is recommended. Python 2 also works.

**Q: Browser didn't open automatically**
A: Manually type: http://localhost:8000 in your address bar

**Q: How do I stop the server?**
A: Press **Ctrl + C** in the terminal/command prompt

**Q: Port 8000 is already in use**
A: Use a different port: `python3 -m http.server 8001`

**Q: Why can't I just open the HTML directly?**
A: Browser security restrictions. Relative paths only work with HTTP servers, not with file:// protocol.

## 🚀 Get Started Now

Choose one of the methods above. All navigation should now work perfectly!
