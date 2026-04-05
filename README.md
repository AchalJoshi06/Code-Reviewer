# AI Code Reviewer

An intelligent code reviewer powered by **Groq API with Llama 3.1-8b** that analyzes code submissions and provides instant, educational feedback. **Supports 13+ programming languages!** Perfect for students, educators, and self-learners.

**Live Demo:** https://code-reviewer-3d9h.onrender.com/

## Features

✅ **Multi-Language Support** - Python, JavaScript, TypeScript, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin  
✅ **Code Style Review** - Language-specific style guides (PEP 8, ESLint, Google C++, PSR-12, etc.)  
✅ **Bug Detection** - Logic errors, edge cases, security vulnerabilities, performance issues  
✅ **Interactive Mode** - Ask follow-up questions about the code  
✅ **Educational Focus** - Explains WHY and HOW, not just WHAT  
✅ **Multiple Interfaces** - Web UI, CLI tool, and REST API  

## Prerequisites

- Python 3.8+
- Groq API key (free tier available at [console.groq.com](https://console.groq.com/))

## Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/AchalJoshi06/Code-Reviewer.git
   cd Code-Reviewer
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv .venv
   
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   
   # Windows (Command Prompt)
   .\.venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Groq API key**
   - Visit [console.groq.com](https://console.groq.com/)
   - Sign up for free account
   - Create API key in API keys section

5. **Set environment variable**
   
   **Windows (PowerShell):**
   ```powershell
   $env:GROQ_API_KEY='your-api-key-here'
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   set GROQ_API_KEY=your-api-key-here
   ```
   
   **Linux/Mac:**
   ```bash
   export GROQ_API_KEY='your-api-key-here'
   ```
   
   **Persistent (.env file):**
   ```bash
   echo "GROQ_API_KEY=your-api-key-here" > .env
   ```

## Usage

### Web Interface (Recommended for Most Users)

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open browser:** `http://localhost:5000`

3. **Choose input method:**
   - **Paste Code** - Select language, paste code, submit
   - **Upload File** - Drag & drop or browse file (auto-detects language)

4. **View Results** - Structured feedback with explanations

### Command Line (CLI)

**Review a single file:**
```bash
python code_reviewer.py path/to/file.py
python code_reviewer.py app.js
python code_reviewer.py Main.java
```

**Interactive mode** (ask follow-up questions):
```bash
python code_reviewer.py path/to/file.py --interactive
# or
python code_reviewer.py app.js -i
```

**Batch processing** (multiple files):
```bash
python code_reviewer.py *.py
python code_reviewer.py src/*.js
```

### REST API

**Review code via HTTP:**
```bash
curl -X POST http://localhost:5000/api/review \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def hello():\n    print(\"Hello\")",
    "language": "python"
  }'
```

**File upload via API:**
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "file=@path/to/file.py"
```

## Supported Languages

| Language   | Extensions | Style Guide |
|------------|------------|-------------|
| Python     | .py        | PEP 8 |
| JavaScript | .js, .jsx  | ESLint/Airbnb |
| TypeScript | .ts, .tsx  | ESLint/TypeScript |
| Java       | .java      | Oracle Java Code Conventions |
| C++        | .cpp, .cc, .cxx, .h, .hpp | Google C++ Style Guide |
| C          | .c, .h     | Linux Kernel Coding Style |
| C#         | .cs        | Microsoft C# Conventions |
| Go         | .go        | Effective Go |
| Rust       | .rs        | Rust Style Guide |
| Ruby       | .rb        | Ruby Style Guide |
| PHP        | .php       | PSR-12 |
| Swift      | .swift     | Swift API Design Guidelines |
| Kotlin     | .kt, .kts  | Kotlin Coding Conventions |

## Example

```bash
python code_reviewer.py my_assignment.py --interactive
```

Output:
1. **Initial Review** - Structured feedback on style issues and potential bugs
2. **Interactive Chat** - Ask the reviewer questions about specific issues

## What Gets Reviewed

The AI analyzes code across **5 dimensions**:

### 1. **Style & Conventions**
- Naming standards (variables, functions, classes)
- Indentation and whitespace
- Import organization
- Language-specific conventions

### 2. **Bug Detection**
- Logic errors and edge cases
- Exception handling
- Type mismatches
- Potential runtime errors

### 3. **Performance**
- Algorithm efficiency
- Redundant operations
- Data structure selection
- Resource management

### 4. **Security**
- Input validation
- Authentication issues
- Data exposure risks
- Cryptography concerns

### 5. **Best Practices**
- DRY principle
- SOLID principles
- Code documentation
- Maintainability

## Example Review Output

Here's what feedback looks like:

```
### Code Review for Python Assignment

**Positive Aspects:**
✓ Clear function naming communicates intent  
✓ Proper use of type hints
✓ Good error handling

**Areas for Improvement:**

1. Missing Docstring (Style)
   WHY: PEP 257 requires docstrings for all public functions
   HOW: Add triple-quoted string after function definition:
   
   def calculate_sum(x: int, y: int) -> int:
       """Calculate and return the sum of two integers."""
       return x + y

2. No Input Validation (Bug Risk)
   WHY: Function crashes with None or non-numeric inputs
   HOW: Add type checking or use try-except:
   
   def calculate_sum(x: int, y: int) -> int:
       if not isinstance(x, int) or not isinstance(y, int):
           raise TypeError("Inputs must be integers")
       return x + y

3. Unused Import (Style)
   WHY: Reduces code clarity and may slow execution
   HOW: Remove unused imports from top of file

**Overall:** Good foundation. Add documentation for production use.
```

## Tips for Best Results

1. **For Web UI** - Use for quick feedback on smaller programs
2. **For CLI** - Better for batch processing and integration with scripts
3. **Ask specific questions** - "Why is this bad?" "How do I improve?"
4. **Use interactive mode** - Get deeper explanations with follow-ups
5. **Review before submission** - Use as a learning tool, not just validation

## API & Performance

- **Groq API** - Free tier available with generous usage limits
- **Response Time** - 5-30 seconds depending on code size
- **Max File Size** - 16MB
- **Concurrent Users** - 10+ (rate-limited by Groq free tier at 30 req/min)

For production use, upgrade your Groq plan at [console.groq.com](https://console.groq.com/)

## Troubleshooting

### "GROQ_API_KEY not set"
Make sure environment variable is set correctly:
```bash
# Check if set (Linux/Mac)
echo $GROQ_API_KEY

# Check if set (Windows PowerShell)
$env:GROQ_API_KEY
```

### "Connection refused" on `localhost:5000`
- Make sure Flask is running: `python app.py`
- Check port 5000 isn't in use: `netstat -ano | findstr :5000` (Windows)
- Try a different port: Set `FLASK_PORT=5001` and use `localhost:5001`

### "File not found"
Use correct file path:
```bash
python code_reviewer.py ./file.py
python code_reviewer.py ../folder/file.js
```

### "Language not recognized"
Make sure file has correct extension: `.py`, `.js`, `.java`, `.cpp`, etc.

### "API Error / Connection timeout"
- Verify API key is valid at [console.groq.com](https://console.groq.com/)
- Check internet connection
- Verify Groq API service status
- Try again (free tier has rate limits)

## Limitations

- Code analysis is **static only** - doesn't execute code to find runtime bugs
- Works best with code < 4000 lines
- Feedback based on AI analysis - manual review recommended
- Single-file analysis (no multi-file project support yet)
- Rate-limited on free tier (30 req/min)

## Deployment

### Deploy to Render (Recommended)

1. **Push to GitHub** (see Quick Start below)
2. **Connect to Render:**
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect GitHub repo
   - Set environment variable: `GROQ_API_KEY`
   - Deploy automatically

3. **Access your live app:**
   - URL: `https://code-reviewer-3d9h.onrender.com/`

### Local Production

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn app:app -w 4 -b 0.0.0.0:5000
```

## Quick Start

```bash
# 1. Clone repo
git clone https://github.com/AchalJoshi06/Code-Reviewer.git
cd Code-Reviewer

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# or: source .venv/bin/activate  # Linux/Mac

# 3. Install packages
pip install -r requirements.txt

# 4. Set API key
$env:GROQ_API_KEY='your-key-here'

# 5. Run web UI
python app.py

# 6. Or use CLI
python code_reviewer.py myfile.py --interactive

# 7. Or deploy to Render (see Deployment section above)
```

## License

MIT - Free to use and modify

