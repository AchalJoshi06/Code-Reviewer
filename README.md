# AI Code Reviewer for University Assignments

An intelligent code reviewer that uses Google Gemini AI to analyze university assignment submissions. **Now supports 13+ programming languages!** Provides feedback on code style, formatting, and potential bugs.

## Features

✅ **Multi-Language Support** - Python, JavaScript, TypeScript, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin  
✅ **Code Style Review** - Language-specific style guides (PEP 8, ESLint, Google C++, PSR-12, etc.)  
✅ **Bug Detection** - Logic errors, edge cases, runtime issues, and security vulnerabilities  
✅ **Interactive Mode** - Ask follow-up questions about the code and get explanations  
✅ **Educational Focus** - Explains WHY something is an issue and HOW to fix it  
✅ **Web UI & CLI** - Both browser-based and command-line interfaces

## Prerequisites

- Python 3.8+
- Google Gemini API key (get it from [aistudio.google.com/apikey](https://aistudio.google.com/apikey))

## Installation

1. **Clone or create the project directory**
   ```bash
   cd d:\SE
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   **Option A: Environment Variable (Recommended)**
   
   Windows (PowerShell):
   ```powershell
   $env:GEMINI_API_KEY='your-api-key-here'
   ```
   
   Windows (Command Prompt):
   ```cmd
   set GEMINI_API_KEY=your-api-key-here
   ```
   
   Linux/Mac:
   ```bash
   export GEMINI_API_KEY='your-api-key-here'
   ```
   
   **Option B: .env File**
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

## Usage

### Web UI (Flask)

1. **Start the web server:**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to: `http://localhost:5000`

3. **Choose your method:**
   - **Paste Code**: Select language from dropdown, paste code, and click "Review Code"
   - **Upload File**: Drag & drop or select a code file (auto-detects language)

### Command Line (CLI)

**Basic Review** - Review any supported code file:
```bash
python code_reviewer.py path/to/file.py
python code_reviewer.py app.js
python code_reviewer.py Main.java
python code_reviewer.py program.cpp
```

**Interactive Mode** - Get initial review, then ask follow-up questions:
```bash
python code_reviewer.py path/to/file.py --interactive
# or
python code_reviewer.py app.js -i
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

### Code Style & Formatting
- PEP 8 compliance
- Naming conventions (variables, functions, classes)
- Code organization and structure
- Comments and documentation quality
- Whitespace and indentation

### Bug Detection
- Logic errors
- Unhandled edge cases
- Potential runtime errors
- Resource management issues
- Type-related problems

## Example Assignment

Here's what the reviewer looks for:

```python
# ❌ Issues that will be caught:
def calc(x,y):  # Poor naming, no docstring
    a = x+ y  # Inconsistent spacing
    if a > 0: print(a)  # Should be on separate line
    return a
    unreachable_code = True  # Dead code

# ✅ Better version:
def calculate_sum(x: int, y: int) -> int:
    """Calculate and return the sum of two integers."""
    total = x + y
    if total > 0:
        print(total)
    return total
```

## Tips for Best Reviews

1. **Include docstrings** - Helps the reviewer understand intent
2. **Copy the actual file** - Don't retype; use actual assignment code
3. **Ask specific questions** - "Why is this bad?" "How do I fix this?"
4. **Review before submission** - Use this as a learning tool before final submission

## API Costs

- This tool uses Google Gemini API for free with generous usage limits
- Check [Google AI Studio](https://aistudio.google.com/) for pricing details
- Typical review: Free tier usually sufficient for student assignments

## Troubleshooting

### "GEMINI_API_KEY not set"
Make sure you've set the environment variable correctly (see Installation section)

### "File not found"
Use the correct path to your Python file:
```bash
python code_reviewer.py ./assignments/my_code.py
```

### "API Error"
- Check your API key is valid at [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- Ensure you have active Gemini API access
- Check your internet connection

## Limitations

- Reviews Python code only
- Works best with assignment code that's less than ~4000 lines
- Feedback is based on AI analysis; always review suggestions yourself
- Not a substitute for human code review

## License

MIT - Free to use and modify

