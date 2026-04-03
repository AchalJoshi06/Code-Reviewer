#!/usr/bin/env python3
"""
AI Code Reviewer for University Assignments
Reviews code for style issues and bugs using Gemini AI
Supports: Python, JavaScript, TypeScript, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

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

def load_code_from_file(file_path: str) -> str:
    """Load Python code from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def review_code(code: str, language: str, api_key: str) -> str:
    """Send code to Gemini for review and get feedback."""
    try:
        client = genai.Client(api_key=api_key)
        
        lang_config = LANGUAGE_CONFIG.get(language, LANGUAGE_CONFIG['python'])
        
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
        print(f"Error calling Gemini API: {e}")
        sys.exit(1)

def interactive_chat(code: str, language: str, api_key: str) -> None:
    """Start an interactive chat session about the code."""
    print("\n" + "="*60)
    print("Interactive Review Mode - Ask questions about the code")
    print("Type 'exit' or 'quit' to end the session")
    print("="*60 + "\n")
    
    client = genai.Client(api_key=api_key)
    lang_config = LANGUAGE_CONFIG.get(language, LANGUAGE_CONFIG['python'])
    
    # Initialize chat history with code context
    initial_message = f"I'll help review this {lang_config['name']} assignment code:\n\n```{language}\n{code}\n```\n\nYou're an expert code reviewer. Focus on code style ({lang_config['style_guide']}) and bug detection. Be constructive and educational."
    
    # Send initial context
    response = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents=initial_message
    )
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\nThank you for using AI Code Reviewer!")
            break
        
        if not user_input:
            continue
        
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-exp',
                contents=user_input
            )
            print(f"\nReviewer: {response.text}\n")
        except Exception as e:
            print(f"Error: {e}\n")

def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python code_reviewer.py <path_to_code_file> [--interactive]")
        print("\nSupported languages:")
        for lang, config in LANGUAGE_CONFIG.items():
            exts = ', '.join(config['extensions'])
            print(f"  {config['name']}: {exts}")
        print("\nExamples:")
        print("  python code_reviewer.py assignment.py")
        print("  python code_reviewer.py app.js --interactive")
        print("  python code_reviewer.py Main.java")
        sys.exit(1)
    
    file_path = sys.argv[1]
    interactive_mode = "--interactive" in sys.argv or "-i" in sys.argv
    
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("\nPlease set your API key:")
        print("  Windows (PowerShell): $env:GEMINI_API_KEY='your-key-here'")
        print("  Windows (CMD): set GEMINI_API_KEY=your-key-here")
        print("  Linux/Mac: export GEMINI_API_KEY='your-key-here'")
        sys.exit(1)
    
    # Detect language
    language = detect_language(file_path)
    lang_config = LANGUAGE_CONFIG[language]
    
    # Load and review code
    print(f"Loading code from '{file_path}'...")
    print(f"Detected language: {lang_config['name']}")
    code = load_code_from_file(file_path)
    
    print(f"File size: {len(code)} characters")
    print("\nSending code for review...\n")
    print("="*60)
    
    review_feedback = review_code(code, language, api_key)
    print(review_feedback)
    print("="*60)
    
    # Enter interactive mode if requested
    if interactive_mode:
        interactive_chat(code, language, api_key)

if __name__ == "__main__":
    main()
