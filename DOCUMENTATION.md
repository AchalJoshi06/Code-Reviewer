# AI Code Reviewer - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Features](#features)
4. [Installation & Setup](#installation--setup)
5. [Usage Guide](#usage-guide)
6. [API Reference](#api-reference)
7. [Configuration](#configuration)
8. [Supported Languages](#supported-languages)
9. [Troubleshooting](#troubleshooting)
10. [Development](#development)

---

## Project Overview

**AI Code Reviewer** is an intelligent code review application designed for university programming assignments. It leverages AI (Groq API with Llama 3.1) to automatically review and provide constructive feedback on student code submissions.

### Purpose
- **Educational Tool**: Helps students understand code style and best practices
- **Automated Feedback**: Provides instant code review without manual assessment
- **Multi-Language Support**: Reviews code across 13+ programming languages
- **Teaching Aid**: Explains WHY issues exist and HOW to fix them

### Key Use Cases
- University assignment submission and feedback
- Student self-directed code improvement
- Teaching code style and quality standards
- Automated code quality checks

---

## Architecture

### System Design

```
┌─────────────────────────────────────────────────────────┐
│                    Flask Web Server                      │
│                    (app.py)                              │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌────────────────────┐        ┌──────────────────────┐ │
│  │   Web Frontend     │        │  API Endpoints       │ │
│  │  (index.html)      │        │  /api/review         │ │
│  │                    │        │  /api/upload         │ │
│  └────────────────────┘        └──────────────────────┘ │
│                                                           │
│  ┌────────────────────────────────────────────────────┐ │
│  │         Code Processing Logic                      │ │
│  │   - Language Detection (detect_language)           │ │
│  │   - Code Review (review_code)                      │ │
│  │   - Prompt Engineering                            │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
└──────────────────────┬─────────────────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │   Groq API Client    │
            │  (llama-3.1-8b)      │
            └──────────────────────┘
```

### Component Overview

| Component | File | Purpose |
|-----------|------|---------|
| Web Server | `app.py` | Main Flask application, routing, API endpoints |
| CLI Tool | `code_reviewer.py` | Command-line interface for batch processing |
| Frontend | `templates/index.html` | User interface for web app |
| Static Assets | `static/` | CSS, JavaScript, images |
| Config | `requirements.txt` | Python dependencies |
| Environment | `.env` | API keys and configuration (not in repo) |

---

## Features

### 1. **Multi-Language Support**
Supports code review for 13+ programming languages with language-specific style guides:
- Python (PEP 8)
- JavaScript (ESLint/Airbnb)
- TypeScript (ESLint/TypeScript)
- Java (Oracle Conventions)
- C/C++ (Google Style Guide)
- C (Linux Kernel Style)
- C# (Microsoft Conventions)
- Go (Effective Go)
- Rust (Rust Style Guide)
- Ruby (Ruby Style Guide)
- PHP (PSR-12)
- Swift (Apple Guidelines)
- Kotlin (Kotlin Conventions)

### 2. **Code Style Analysis**
- Language-specific naming conventions
- Code organization and structure
- Documentation and comments
- Formatting and indentation

### 3. **Bug Detection**
- Logic errors and edge cases
- Runtime issues and exceptions
- Security vulnerabilities
- Performance problems

### 4. **User Interfaces**
- **Web Interface**: Browser-based UI for interactive reviews
- **CLI Interface**: Command-line tool for batch processing
- **API Access**: JSON REST API for integration

### 5. **File Handling**
- Direct code paste in web interface
- File upload support (16MB max)
- Automatic language detection from file extension
- Text file encoding support

### 6. **Interactive Mode**
- Ask follow-up questions about reviews
- Get explanations for feedback
- Clarify complex issues

---

## Installation & Setup

### Prerequisites

- **Python 3.8+** (3.10+ recommended)
- **Groq API Key** (free from [console.groq.com](https://console.groq.com))
- **Windows, macOS, or Linux**

### Step 1: Clone/Setup Project

```bash
cd d:\SE
```

### Step 2: Create Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key

#### Option A: Environment Variable (Recommended)

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY='your-api-key-here'
```

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your-api-key-here
```

**macOS/Linux:**
```bash
export GROQ_API_KEY='your-api-key-here'
```

#### Option B: .env File

Create a `.env` file in the project root:
```
GROQ_API_KEY=your-api-key-here
```

### Step 5: Verify Installation

**Test Web Server:**
```bash
python app.py
# Navigate to http://localhost:5000 in browser
```

**Test CLI:**
```bash
python code_reviewer.py example_assignment.py
```

---

## Usage Guide

### Web Interface

1. **Start the server:**
   ```bash
   python app.py
   ```

2. **Open browser:**
   Navigate to `http://localhost:5000`

3. **Review code:**
   - Select programming language
   - Paste code or upload file
   - Click "Review Code"
   - Read AI-generated feedback

### Command Line Interface

#### Basic Review
```bash
python code_reviewer.py your_file.py
```

#### Interactive Mode (Ask Follow-ups)
```bash
python code_reviewer.py your_file.py --interactive
```

#### Specify Language
```bash
python code_reviewer.py my_code --language javascript
```

#### Review Multiple Files
```bash
python code_reviewer.py file1.py file2.js file3.java
```

### API Usage (for Integration)

#### Review Code via API
```bash
curl -X POST http://localhost:5000/api/review \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def hello():\n    print(\"Hello\")",
    "language": "python"
  }'
```

#### Upload File via API
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "file=@assignment.py"
```

---

## API Reference

### POST /api/review
**Review code provided as text**

**Request:**
```json
{
  "code": "your code here",
  "language": "python"
}
```

**Response:**
```json
{
  "review": "AI-generated review feedback..."
}
```

**Parameters:**
- `code` (string, required): Source code to review
- `language` (string, optional): Programming language (default: 'python')

**Supported Languages:** python, javascript, typescript, java, cpp, c, csharp, go, rust, ruby, php, swift, kotlin

### POST /api/upload
**Review code from uploaded file**

**Request:**
- Form data with file upload
- File types detected automatically by extension

**Response:**
```json
{
  "review": "AI-generated review feedback...",
  "filename": "assignment.py",
  "language": "Python"
}
```

**Limits:**
- Maximum file size: 16MB
- Supported extensions: Based on language configuration

### GET /
**Main web interface**

Returns HTML page with interactive code review interface.

---

## Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GROQ_API_KEY` | API key for Groq service | `gsk_...` |
| `FLASK_ENV` | Flask environment | `development` or `production` |
| `FLASK_DEBUG` | Enable debug mode | `0` or `1` |

### Application Settings (in app.py)

```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file
app.config['JSON_SORT_KEYS'] = False
```

### Language Configuration

Each language is configured with:
- **extensions**: File extensions to recognize
- **name**: Display name
- **style_guide**: Reference style guide
- **comment_style**: Documentation format

Example:
```python
'python': {
    'extensions': ['.py'],
    'name': 'Python',
    'style_guide': 'PEP 8',
    'comment_style': 'Clean code, proper docstrings'
}
```

---

## Supported Languages

### Complete Reference

| Language | Extensions | Style Guide | Comments |
|----------|-----------|------------|----------|
| Python | `.py` | PEP 8 | Docstrings |
| JavaScript | `.js`, `.jsx` | ESLint/Airbnb | JSDoc |
| TypeScript | `.ts`, `.tsx` | ESLint/TypeScript | JSDoc + Types |
| Java | `.java` | Oracle Conventions | Javadoc |
| C++ | `.cpp`, `.cc`, `.cxx`, `.h`, `.hpp` | Google Style | Doxygen |
| C | `.c`, `.h` | Linux Kernel | Function comments |
| C# | `.cs` | Microsoft Conventions | XML Documentation |
| Go | `.go` | Effective Go | Godoc |
| Rust | `.rs` | Rust Style Guide | Rustdoc |
| Ruby | `.rb` | Ruby Style Guide | RDoc/YARD |
| PHP | `.php` | PSR-12 | PHPDoc |
| Swift | `.swift` | Apple Guidelines | Markdown Docs |
| Kotlin | `.kt`, `.kts` | Kotlin Conventions | KDoc |

### Adding New Languages

To add support for a new language, add an entry to `LANGUAGE_CONFIG` in `app.py`:

```python
'newlang': {
    'extensions': ['.ext'],
    'name': 'Language Name',
    'style_guide': 'Style Guide Name',
    'comment_style': 'Comment Format'
}
```

---

## Troubleshooting

### Common Issues

#### 1. "GROQ_API_KEY not set"
**Problem:** API key environment variable not found

**Solution:**
- Verify API key is set: `echo $env:GROQ_API_KEY` (PowerShell) or `echo %GROQ_API_KEY%` (CMD)
- Set it again and restart Flask/CLI
- Check `.env` file exists and has correct permissions
- Restart terminal/IDE after setting environment variable

#### 2. "Connection refused" or "Connection timeout"
**Problem:** Can't connect to Groq API

**Solution:**
- Check internet connection
- Verify API key is valid (test at console.groq.com)
- Check firewall settings
- Verify API key has quota remaining

#### 3. File upload fails
**Problem:** File too large or unsupported format

**Solution:**
- Check file size is under 16MB
- Verify file extension is supported
- Use correct file extension (e.g., `.py` for Python)
- Check file encoding is UTF-8

#### 4. Flask server won't start
**Problem:** Port 5000 already in use

**Solution:**
```bash
# Change port in app.py or run:
python app.py -p 5001
```

#### 5. Review takes too long
**Problem:** Slow API response

**Solution:**
- Check internet connection
- Large code files may take longer to process
- Consider breaking into smaller files
- Try again (temporary API slowness)

---

## Development

### Project Structure
```
d:\SE\
├── app.py                    # Flask web application
├── code_reviewer.py         # CLI tool
├── example_assignment.py    # Example code for testing
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
├── templates/
│   └── index.html          # Web UI template
├── static/                 # Static files (CSS, JS, images)
├── README.md               # Quick start guide
├── DOCUMENTATION.md        # This file
├── Procfile                # Heroku deployment config
└── QUICKSTART.md           # Quick reference
```

### Installing for Development

```bash
# Clone or navigate to project
cd d:\SE

# Create virtual environment
python -m venv .venv
& .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set API key
$env:GROQ_API_KEY='your-key'

# Run Flask in debug mode
$env:FLASK_ENV='development'
python app.py
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | >=3.0.0 | Web framework |
| groq | >=0.9.0 | Groq API client |
| python-dotenv | >=1.0.0 | Environment variables |
| gunicorn | >=22.0.0 | Production server |

### Code Style

The project follows:
- **Python**: PEP 8 standards
- **Naming**: snake_case for functions/variables, UPPER_CASE for constants
- **Documentation**: Docstrings for functions and modules
- **Comments**: Clear explanations of complex logic

### Extending the Application

#### Add New Language Support
1. Add entry to `LANGUAGE_CONFIG` dictionary in `app.py`
2. Test language detection: `python -c "from app import detect_language; print(detect_language('test.ext'))"`

#### Modify Review Prompt
Edit the `review_code()` function's prompt template in `app.py`:
```python
prompt = f"""You are an expert code reviewer...
# Customize instructions here
"""
```

#### Add New Features
- Modify `templates/index.html` for UI changes
- Add routes in `app.py` for new endpoints
- Update requirements.txt if adding dependencies

---

## Deployment

### Heroku Deployment
The project includes `Procfile` for Heroku:
```
web: gunicorn app:app
```

### Environment Variables for Production
Set on your hosting platform:
- `GROQ_API_KEY`: Your API key
- `FLASK_ENV`: Set to `production`

### Performance Considerations
- Review timeout: API may take 10-30 seconds for large files
- Concurrent requests: Flask default handles moderate load
- For high traffic: Consider load balancing with multiple instances

---

## Support & Resources

### Getting Help
1. Check this documentation
2. Review example_assignment.py for usage examples
3. Check AI response for specific feedback explanation
4. Verify API key and connection

### Useful Links
- [Groq Console](https://console.groq.com)
- [Groq Documentation](https://console.groq.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Python PEP 8](https://pep8.org)

### Reporting Issues
Include:
- Error message or unexpected behavior
- Programming language being reviewed
- Code snippet (if safe to share)
- Environment (Windows/Mac/Linux, Python version)

---

## Version History

**v1.0** (Current)
- Multi-language support (13+ languages)
- Web UI with file upload
- CLI interface
- API endpoints
- Groq API integration
- Educational feedback focus

---

**Last Updated:** April 4, 2026  
**Status:** Active Development
