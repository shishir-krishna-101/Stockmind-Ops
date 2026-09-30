import os
import glob

def replace_in_file(filepath, old, new):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

files = glob.glob('c:/Users/Demon Slayer/Downloads/Stockmind-Ops/**/*.md', recursive=True)

for file in files:
    # URL replacement
    replace_in_file(file, 'https://github.com/Harshuqt/StockMind.git', 'https://github.com/shishir-krishna-101/StockMind.git')
    replace_in_file(file, 'Harshuqt/StockMind', 'shishir-krishna-101/StockMind')
    
    # Gemini status replacement in STATUS.md
    if file.endswith('STATUS.md'):
        replace_in_file(file, '- **Gemini**: CURRENT (in application repo, application AI)', '- **Gemini**: PLANNED (Application AI and analysis features have not yet been implemented)')
    
    # README.md (root and docs/)
    if file.endswith('README.md') and '02-architecture' not in file:
        replace_in_file(file, 'Google Gemini API (AI)', 'Google Gemini API (AI - Planned)')
        
    # Architecture doc
    if '02-architecture' in file:
        # We need to change the status of Gemini in 02-architecture if we added a tech_template for it.
        # But wait, I didn't add a tech_template for Gemini in Batch 1. I only did React and FastAPI.
        pass

print("Replacements complete.")
