# Quick Start Guide

## 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

## 2. Set Your API Key

### Windows PowerShell:
```powershell
$env:GEMINI_API_KEY='your-api-key-from-aistudio.google.com'
```

### Windows Command Prompt:
```cmd
set GEMINI_API_KEY=your-api-key-from-aistudio.google.com
```

## 3. Try the Example
```powershell
python code_reviewer.py example_assignment.py
```

## 4. Review Your Own Code
```powershell
python code_reviewer.py your_assignment.py --interactive
```

## Get Your API Key

1. Go to https://aistudio.google.com/apikey
2. Click "Create API Key"
3. Copy the key and use it in step 2 above

## Questions?

See README.md for detailed documentation!
