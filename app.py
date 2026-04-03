#!/usr/bin/env python3
"""
Flask-based Web UI for AI Code Reviewer
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from flask import Flask, render_template, request, jsonify

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    client = genai.Client(api_key=API_KEY)


# Language configuration with file extensions and style guides
LANGUAGE_CONFIG = {
    'python': {
        'extensions': ['.py'],
        'name': 'Python',
        'style_guide': 'PEP 8',
        'comment_style': 'Clean code, proper docstrings'
    },
    'javascript': {
        'extensions': ['.js', '.jsx'],
        'name': 'JavaScript',
        'style_guide': 'ESLint/Airbnb',
        'comment_style': 'JSDoc comments'
    },
    'typescript': {
        'extensions': ['.ts', '.tsx'],
        'name': 'TypeScript',
        'style_guide': 'ESLint/TypeScript',
        'comment_style': 'JSDoc with type annotations'
    },
    'java': {
        'extensions': ['.java'],
        'name': 'Java',
        'style_guide': 'Oracle Java Code Conventions',
        'comment_style': 'Javadoc comments'
    },
    'cpp': {
        'extensions': ['.cpp', '.cc', '.cxx', '.h', '.hpp'],
        'name': 'C++',
        'style_guide': 'Google C++ Style Guide',
        'comment_style': 'Doxygen-style comments'
    },
    'c': {
        'extensions': ['.c', '.h'],
        'name': 'C',
        'style_guide': 'Linux Kernel Coding Style',
        'comment_style': 'Clear function-level comments'
    },
    'csharp': {
        'extensions': ['.cs'],
        'name': 'C#',
        'style_guide': 'Microsoft C# Coding Conventions',
        'comment_style': 'XML documentation'
    },
    'go': {
        'extensions': ['.go'],
        'name': 'Go',
        'style_guide': 'Effective Go',
        'comment_style': 'Godoc comments'
    },
    'rust': {
        'extensions': ['.rs'],
        'name': 'Rust',
        'style_guide': 'Rust Style Guide',
        'comment_style': 'Rustdoc comments'
    },
    'ruby': {
        'extensions': ['.rb'],
        'name': 'Ruby',
        'style_guide': 'Ruby Style Guide',
        'comment_style': 'RDoc/YARD comments'
    },
    'php': {
        'extensions': ['.php'],
        'name': 'PHP',
        'style_guide': 'PSR-12',
        'comment_style': 'PHPDoc comments'
    },
    'swift': {
        'extensions': ['.swift'],
        'name': 'Swift',
        'style_guide': 'Swift API Design Guidelines',
        'comment_style': 'Markdown documentation'
    },
    'kotlin': {
        'extensions': ['.kt', '.kts'],
        'name': 'Kotlin',
        'style_guide': 'Kotlin Coding Conventions',
        'comment_style': 'KDoc comments'
    }
}


def detect_language(filename: str) -> str:
    """Detect programming language from file extension."""
    ext = Path(filename).suffix.lower()
    for lang, config in LANGUAGE_CONFIG.items():
        if ext in config['extensions']:
            return lang
    return 'python'  # Default to Python


def review_code(code: str, language: str = 'python') -> str:
    """Send code to Gemini for review and get feedback."""
    if not API_KEY:
        return "Error: GEMINI_API_KEY environment variable not set."
    
    if language not in LANGUAGE_CONFIG:
        language = 'python'
    
    lang_config = LANGUAGE_CONFIG[language]
    
    try:
        prompt = f"""You are an expert code reviewer for university programming assignments. 
Focus on code style ({lang_config['style_guide']}, naming, organization, {lang_config['comment_style']}) 
and bug detection (logic errors, edge cases, runtime issues, security vulnerabilities). 
Be constructive and explain WHY and HOW to fix issues.

Please review this {lang_config['name']} assignment code:

```{language}
{code}
```"""
        
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"


@app.route('/')
def index():
    """Main page."""
    # Pass language info to template
    languages = {k: v['name'] for k, v in LANGUAGE_CONFIG.items()}
    return render_template('index.html', languages=languages)


@app.route('/api/review', methods=['POST'])
def api_review():
    """API endpoint to review code."""
    data = request.json
    code = data.get('code', '').strip()
    language = data.get('language', 'python')
    
    if not code:
        return jsonify({'error': 'No code provided'}), 400
    
    if not API_KEY:
        return jsonify({'error': 'GEMINI_API_KEY environment variable not set'}), 500
    
    review_result = review_code(code, language)
    return jsonify({'review': review_result})


@app.route('/api/upload', methods=['POST'])
def api_upload():
    """API endpoint to upload and review a code file."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Detect language from file extension
    language = detect_language(file.filename)
    lang_config = LANGUAGE_CONFIG[language]
    
    # Validate file extension
    ext = Path(file.filename).suffix.lower()
    valid_extensions = [ext for config in LANGUAGE_CONFIG.values() for ext in config['extensions']]
    if ext not in valid_extensions:
        return jsonify({'error': f'Unsupported file type. Supported: {", ".join(sorted(set(valid_extensions)))}'}), 400
    
    try:
        code = file.read().decode('utf-8')
        review_result = review_code(code, language)
        return jsonify({
            'review': review_result, 
            'filename': file.filename,
            'language': lang_config['name']
        })
    except UnicodeDecodeError:
        return jsonify({'error': 'File encoding error. Please use UTF-8 encoding.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("Starting Flask Code Reviewer UI...")
    print("Visit http://localhost:5000 in your browser")
    app.run(debug=True, use_reloader=False, host='localhost', port=5000)
