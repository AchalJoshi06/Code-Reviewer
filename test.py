# Check Available Gemini Models & Get Fixed Code
# Run this first to see what models are available for your API key

import google.generativeai as genai

def check_available_models(api_key):
    """
    Check what models are available for your API key
    """
    genai.configure(api_key=api_key)
    
    print("🔍 Fetching available models...\n")
    
    try:
        # List all available models
        models = genai.list_models()
        
        print("="*70)
        print("AVAILABLE MODELS")
        print("="*70)
        
        available_models = []
        
        for model in models:
            # Get model info
            model_name = model.name
            display_name = model.display_name
            description = model.description if hasattr(model, 'description') else "N/A"
            
            # Check if it supports generateContent
            supports_generate = False
            if hasattr(model, 'supported_generation_methods'):
                supports_generate = 'generateContent' in model.supported_generation_methods
            
            # Print if it's a Gemini model and supports generateContent
            if 'gemini' in model_name.lower() and supports_generate:
                print(f"\n✅ Model: {model_name}")
                print(f"   Display Name: {display_name}")
                print(f"   Supports generateContent: Yes")
                available_models.append(model_name)
        
        print("\n" + "="*70)
        print(f"Found {len(available_models)} available Gemini models")
        print("="*70)
        
        # Recommend the best model
        if available_models:
            print(f"\n✨ RECOMMENDED MODEL: {available_models[0]}")
            print("Use this in your code:")
            print(f"   model = genai.GenerativeModel('{available_models[0]}')")
        
        return available_models
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Common solutions:")
        print("1. Verify your API key is correct")
        print("2. Check your API key has proper permissions")
        print("3. Visit: https://makersuite.google.com/app/apikey")
        return []

def test_model(api_key, model_name):
    """
    Test if a model works with a simple request
    """
    genai.configure(api_key=api_key)
    
    print(f"\n🧪 Testing model: {model_name}")
    print("-" * 70)
    
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello, please respond with 'Model works!'")
        
        print(f"✅ Model works!")
        print(f"Response: {response.text[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Model test failed: {e}")
        return False

# ============================================================================
# MAIN
# ============================================================================

print("🚀 Gemini Model Checker for Resume Screening")
print("=" * 70)

api_key = input("\n🔑 Enter your Gemini API Key: ").strip()

if not api_key:
    print("❌ API key is required!")
    exit()

# Check available models
available_models = check_available_models(api_key)

# Test the first available model
if available_models:
    test_model(api_key, available_models[0])
    
    print("\n" + "="*70)
    print("✨ NEXT STEPS:")
    print("="*70)
    print(f"1. Replace all instances of 'gemini-1.5-flash' with '{available_models[0]}'")
    print("2. Or use the FIXED version below:")
    print("="*70)

# Provide fixed code snippets
print("\n📝 FIXED CODE SNIPPETS:\n")

print("Option 1: Get model dynamically (RECOMMENDED)")
print("-" * 70)
print("""
def get_working_model(api_key):
    '''Automatically finds and returns the first available Gemini model'''
    genai.configure(api_key=api_key)
    models = genai.list_models()
    
    for model in models:
        if 'gemini' in model.name.lower() and 'generateContent' in model.supported_generation_methods:
            return model.name
    
    raise Exception("No Gemini model found")

# Use it
api_key = "your_api_key"
model_name = get_working_model(api_key)
model = genai.GenerativeModel(model_name)
response = model.generate_content("your prompt here")
""")

print("\n\nOption 2: Use specific model name")
print("-" * 70)
if available_models:
    print(f"# Replace 'gemini-1.5-flash' with '{available_models[0]}'")
    print(f"model = genai.GenerativeModel('{available_models[0]}')")
    print(f"response = model.generate_content(prompt)")
else:
    print("model = genai.GenerativeModel('gemini-2.0-flash')")
    print("response = model.generate_content(prompt)")

print("\n\nOption 3: Try these models in order")
print("-" * 70)
print("""
models_to_try = [
    'gemini-2.0-flash',
    'gemini-1.5-pro',
    'gemini-1.5-flash',
    'gemini-pro'
]

for model_name in models_to_try:
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        print(f"✅ Success with {model_name}")
        break
    except Exception as e:
        print(f"❌ {model_name} failed: {e}")
        continue
""")

print("\n" + "="*70)
print("Done! Now you can update your resume screening code.")
print("="*70)