#!/usr/bin/env python3
"""
Fix Python 3.9 compatibility issues in Claude Code hook files.
Converts Python 3.10+ syntax to Python 3.9 compatible code.
"""

import os
import re
import sys
from pathlib import Path

def fix_file(file_path):
    """Fix Python 3.9 compatibility issues in a single file."""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Fix type union syntax (X | Y -> Union[X, Y])
    # Pattern 1: Simple unions like "str | None"
    pattern1 = r'\b(\w+)\s*\|\s*None\b'
    if re.search(pattern1, content):
        content = re.sub(pattern1, r'Optional[\1]', content)
        changes.append("Fixed X | None -> Optional[X]")
    
    # Pattern 2: Multiple unions like "str | dict | None"
    pattern2 = r'\b(\w+)\s*\|\s*(\w+)\s*\|\s*None\b'
    if re.search(pattern2, content):
        content = re.sub(pattern2, r'Optional[Union[\1, \2]]', content)
        changes.append("Fixed X | Y | None -> Optional[Union[X, Y]]")
    
    # Pattern 3: Simple unions without None like "str | dict"
    pattern3 = r':\s*(\w+)\s*\|\s*(\w+)(?!\s*\|)'
    if re.search(pattern3, content):
        content = re.sub(pattern3, r': Union[\1, \2]', content)
        changes.append("Fixed X | Y -> Union[X, Y]")
    
    # Fix type alias syntax (type X = Y -> X = Y)
    pattern4 = r'^type\s+(\w+)\s*=\s*(.+)$'
    if re.search(pattern4, content, re.MULTILINE):
        content = re.sub(pattern4, r'\1 = \2', content, flags=re.MULTILINE)
        changes.append("Fixed type X = Y -> X = Y")
    
    # Fix dict/list generics (dict[str, X] -> Dict[str, X])
    pattern5 = r'\bdict\['
    if re.search(pattern5, content):
        content = re.sub(pattern5, 'Dict[', content)
        changes.append("Fixed dict[...] -> Dict[...]")
    
    pattern6 = r'\blist\['
    if re.search(pattern6, content):
        content = re.sub(pattern6, 'List[', content)
        changes.append("Fixed list[...] -> List[...]")
    
    # Add necessary imports if we made changes
    if changes and 'from typing import' in content:
        # Check which imports we need to add
        imports_needed = set()
        if 'Optional[' in content and 'Optional' not in content:
            imports_needed.add('Optional')
        if 'Union[' in content and 'Union' not in content:
            imports_needed.add('Union')
        if 'Dict[' in content and 'Dict' not in content:
            imports_needed.add('Dict')
        if 'List[' in content and 'List' not in content:
            imports_needed.add('List')
        
        if imports_needed:
            # Find existing typing import
            import_pattern = r'from typing import ([^\n]+)'
            match = re.search(import_pattern, content)
            if match:
                existing_imports = match.group(1)
                # Parse existing imports
                existing = set(imp.strip() for imp in existing_imports.split(','))
                # Add new imports
                all_imports = existing | imports_needed
                # Sort for consistency
                sorted_imports = sorted(all_imports)
                # Replace import line
                new_import = f"from typing import {', '.join(sorted_imports)}"
                content = re.sub(import_pattern, new_import, content, count=1)
                changes.append(f"Updated typing imports: {', '.join(imports_needed)}")
    
    # Fix StrEnum for Python < 3.11
    if 'from enum import StrEnum' in content:
        # Add custom StrEnum implementation
        strenum_impl = '''from enum import Enum
from typing import Set


class StrEnum(str, Enum):
    """Backport of StrEnum for Python < 3.11"""
    def __str__(self):
        return self.value

'''
        content = content.replace('from enum import StrEnum\nfrom typing import Set\n', strenum_impl)
        content = content.replace('from enum import StrEnum\n', strenum_impl)
        changes.append("Added StrEnum backport for Python < 3.11")
    
    # Only write if we made changes
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        return changes
    
    return []

def main():
    """Fix Python 3.9 compatibility in all hook files."""
    
    # Get the .claude directory
    repo_root = Path(__file__).parent.parent
    claude_dir = repo_root / '.claude'
    
    if not claude_dir.exists():
        print("❌ .claude directory not found!")
        sys.exit(1)
    
    print("🔧 Fixing Python 3.9 compatibility issues...")
    print("=" * 50)
    
    # Find all Python files in hooks directory
    hooks_dir = claude_dir / 'hooks'
    python_files = list(hooks_dir.glob('**/*.py'))
    
    total_fixed = 0
    for py_file in python_files:
        changes = fix_file(py_file)
        if changes:
            print(f"\n✅ Fixed {py_file.relative_to(repo_root)}:")
            for change in changes:
                print(f"   • {change}")
            total_fixed += 1
    
    if total_fixed == 0:
        print("\n✅ All files are already Python 3.9 compatible!")
    else:
        print(f"\n✨ Fixed {total_fixed} files for Python 3.9 compatibility")
    
    # Check Python version
    py_version = sys.version_info
    if py_version.major == 3 and py_version.minor < 9:
        print(f"\n⚠️  Warning: You're running Python {py_version.major}.{py_version.minor}")
        print("   Python 3.9+ is required for full functionality")

if __name__ == "__main__":
    main()