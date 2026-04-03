# Flask UI Quick Start

## Running the Web UI

The Flask-based web UI provides a user-friendly interface to review Python code.

### Step 1: Install Dependencies

If you haven't already, install the required packages:

```bash
pip install -r requirements.txt
```

This will install Flask along with other dependencies.

### Step 2: Set Your API Key

Make sure your GEMINI_API_KEY environment variable is set:

**PowerShell:**
```powershell
$env:GEMINI_API_KEY='your-api-key-here'
```

**Command Prompt:**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY='your-api-key-here'
```

### Step 3: Run the Flask App

```bash
python app.py
```

You should see output like:
```
Starting Flask Code Reviewer UI...
Visit http://localhost:5000 in your browser
```

### Step 4: Open in Browser

Visit **http://localhost:5000** in your web browser.

## Features

### 📝 Paste Code Tab
- Copy and paste Python code directly
- Click "Review Code" to get AI feedback

### 📤 Upload File Tab
- Upload .py files (drag & drop or click to select)
- Supports files up to 16MB

### Review Results
- Get detailed feedback on:
  - Code style (PEP 8 compliance)
  - Naming conventions
  - Code organization
  - Bug detection
  - Logic errors and edge cases
  - How to fix identified issues

## Stopping the Server

Press `Ctrl+C` in the terminal to stop the Flask development server.

## Troubleshooting

- **Port 5000 already in use?** Stop other Flask instances or modify the port in `app.py`
- **API key not set?** You'll see an error message in the app - set the GEMINI_API_KEY environment variable
- **File upload failing?** Make sure the file is UTF-8 encoded and is a valid .py file

## Command Line Usage

The original command-line interface is still available:

```bash
python code_reviewer.py assignment.py
python code_reviewer.py assignment.py --interactive
```
