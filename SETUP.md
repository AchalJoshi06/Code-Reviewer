# Setup Instructions

## Step 1: Get Your API Key

1. Go to https://aistudio.google.com/apikey
2. Click "Create API Key" 
3. Copy your API key

## Step 2: Add Your API Key to .env

Open the file `.env` in the `d:\SE` folder and replace `your-api-key-here` with your actual key:

```
GEMINI_API_KEY=paste-your-key-here
```

**Example:**
```
GEMINI_API_KEY=AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q
```

## Step 3: Run the Code Reviewer

```powershell
cd d:\SE
d:\SE\.venv\Scripts\python.exe code_reviewer.py example_assignment.py
```

## Step 4: Try Interactive Mode

```powershell
d:\SE\.venv\Scripts\python.exe code_reviewer.py your_file.py --interactive
```

That's it! No more environment variable headaches.
