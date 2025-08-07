#!/usr/bin/env python3
"""
Comprehensive verification script for Claude Code alfred voice setup.
Checks all components and provides actionable fixes.
"""

import sys
import os
import json
import subprocess
from pathlib import Path

# ANSI color codes for better output
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header(text):
    """Print a formatted header."""
    print(f"\n{BOLD}{BLUE}{'=' * 60}{RESET}")
    print(f"{BOLD}{BLUE}{text}{RESET}")
    print(f"{BOLD}{BLUE}{'=' * 60}{RESET}")

def print_success(text):
    """Print success message."""
    print(f"{GREEN}✅ {text}{RESET}")

def print_warning(text):
    """Print warning message."""
    print(f"{YELLOW}⚠️  {text}{RESET}")

def print_error(text):
    """Print error message."""
    print(f"{RED}❌ {text}{RESET}")

def print_info(text):
    """Print info message."""
    print(f"{BLUE}ℹ️  {text}{RESET}")

def check_python_version():
    """Check Python version compatibility."""
    print_header("Python Version Check")
    
    py_version = sys.version_info
    version_str = f"{py_version.major}.{py_version.minor}.{py_version.micro}"
    
    if py_version.major != 3:
        print_error(f"Python 3 required, found Python {py_version.major}")
        return False
    
    if py_version.minor < 9:
        print_error(f"Python 3.9+ required, found Python {version_str}")
        print_info("Install Python 3.9+ from https://www.python.org/downloads/")
        return False
    
    if py_version.minor == 9:
        print_warning(f"Python {version_str} detected - compatibility fixes may be needed")
        print_info("Run: python3 scripts/fix-python39-compatibility.py")
    else:
        print_success(f"Python {version_str} - fully compatible")
    
    return True

def check_pygame():
    """Check if pygame is installed and working."""
    print_header("Pygame Audio Library Check")
    
    try:
        import pygame
        pygame.init()
        pygame.mixer.init()
        print_success(f"pygame {pygame.version.ver} installed and initialized")
        pygame.quit()
        return True
    except ImportError:
        print_error("pygame not installed")
        print_info("Install with one of:")
        print("  • uv add pygame")
        print("  • pip install pygame")
        print("  • pip3 install pygame")
        return False
    except Exception as e:
        print_warning(f"pygame installed but initialization failed: {e}")
        print_info("Check audio permissions in System Settings")
        return False

def check_claude_directory():
    """Check if .claude directory exists and has correct structure."""
    print_header("Claude Directory Structure")
    
    repo_root = Path.cwd()
    claude_dir = repo_root / '.claude'
    
    if not claude_dir.exists():
        print_error(".claude directory not found!")
        print_info("Run installer: curl -sSL https://raw.githubusercontent.com/sergimiral/claude-code-custom-init/main/install.sh | bash")
        return False
    
    print_success(".claude directory exists")
    
    # Check subdirectories
    required_dirs = [
        'agents',
        'commands',
        'hooks',
        'hooks/common',
        'hooks/voice_notifications',
        'hooks/voice_notifications/sounds',
        'hooks/voice_notifications/sounds/alfred',
    ]
    
    all_good = True
    for dir_path in required_dirs:
        full_path = claude_dir / dir_path
        if full_path.exists():
            print_success(f"  ✓ {dir_path}/")
        else:
            print_error(f"  ✗ {dir_path}/ missing")
            all_good = False
    
    return all_good

def check_alfred_sounds():
    """Check if all alfred sound files are present."""
    print_header("Alfred Voice Pack")
    
    sounds_dir = Path.cwd() / '.claude/hooks/voice_notifications/sounds/alfred'
    
    if not sounds_dir.exists():
        print_error("Alfred sounds directory not found!")
        return False
    
    mp3_files = list(sounds_dir.glob('*.mp3'))
    count = len(mp3_files)
    
    if count == 0:
        print_error("No alfred sound files found!")
        return False
    elif count < 55:
        print_warning(f"Only {count}/55 alfred sounds found")
        print_info("Some sounds may be missing")
    else:
        print_success(f"All {count} alfred sounds present")
    
    # Check some key sounds
    key_sounds = [
        'file_read.mp3',
        'code_edit.mp3',
        'system_command.mp3',
        'work_finished.mp3',
        'alert.mp3'
    ]
    
    for sound in key_sounds:
        if (sounds_dir / sound).exists():
            print_success(f"  ✓ {sound}")
        else:
            print_warning(f"  ✗ {sound} missing")
    
    return count >= 50

def check_settings():
    """Check settings.json configuration."""
    print_header("Settings Configuration")
    
    settings_path = Path.cwd() / '.claude/settings.json'
    
    if not settings_path.exists():
        print_error("settings.json not found!")
        print_info("Create .claude/settings.json with alfred configuration")
        return False
    
    try:
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        
        notifications = settings.get('notifications', {})
        mode = notifications.get('mode')
        voice = notifications.get('voice')
        
        issues = []
        
        if mode != 'sounds':
            issues.append(f"mode is '{mode}' but should be 'sounds'")
        
        if voice != 'alfred':
            issues.append(f"voice is '{voice}' but should be 'alfred'")
        
        if issues:
            print_warning("Configuration issues found:")
            for issue in issues:
                print(f"  • {issue}")
            print_info("Fix with: sed -i '' 's/\"voice\": \".*\"/\"voice\": \"alfred\"/g' .claude/settings.json")
            return False
        else:
            print_success("settings.json correctly configured for alfred")
            print(f"  • mode: {mode}")
            print(f"  • voice: {voice}")
            return True
            
    except json.JSONDecodeError:
        print_error("settings.json is not valid JSON")
        return False
    except Exception as e:
        print_error(f"Error reading settings.json: {e}")
        return False

def check_handler():
    """Check if handler.py supports alfred voice pack."""
    print_header("Handler Compatibility")
    
    handler_path = Path.cwd() / '.claude/hooks/voice_notifications/handler.py'
    
    if not handler_path.exists():
        print_error("handler.py not found!")
        return False
    
    with open(handler_path, 'r') as f:
        content = f.read()
    
    # Check for alfred support indicators
    checks = {
        'custom_voice_packs': 'Custom voice pack support',
        '"alfred"': 'Alfred voice pack reference',
        'voice in custom_voice_packs': 'Voice pack detection logic'
    }
    
    all_good = True
    for pattern, description in checks.items():
        if pattern in content:
            print_success(f"  ✓ {description}")
        else:
            print_warning(f"  ✗ {description} not found")
            all_good = False
    
    if not all_good:
        print_info("Handler may need updating for alfred support")
        print_info("Re-run installer to get latest handler")
    
    return all_good

def check_sound_mapping():
    """Check if sound_mapping.json has alfred configuration."""
    print_header("Sound Mapping Configuration")
    
    mapping_path = Path.cwd() / '.claude/hooks/voice_notifications/sound_mapping.json'
    
    if not mapping_path.exists():
        print_error("sound_mapping.json not found!")
        return False
    
    try:
        with open(mapping_path, 'r') as f:
            mapping = json.load(f)
        
        if 'alfred' in mapping:
            print_success("Alfred section found in sound_mapping.json")
            alfred_config = mapping['alfred']
            
            if 'tools' in alfred_config:
                print_success(f"  ✓ {len(alfred_config['tools'])} tool mappings")
            else:
                print_warning("  ✗ No tool mappings")
            
            if 'events' in alfred_config:
                print_success(f"  ✓ {len(alfred_config['events'])} event mappings")
            else:
                print_warning("  ✗ No event mappings")
            
            if 'patterns' in alfred_config:
                print_success(f"  ✓ {len(alfred_config['patterns'])} pattern mappings")
            else:
                print_info("  • No pattern mappings (optional)")
            
            return True
        else:
            print_error("Alfred section missing from sound_mapping.json")
            print_info("The alfred voice pack needs proper mapping configuration")
            return False
            
    except json.JSONDecodeError:
        print_error("sound_mapping.json is not valid JSON")
        return False
    except Exception as e:
        print_error(f"Error reading sound_mapping.json: {e}")
        return False

def test_sound_playback():
    """Test actual sound playback."""
    print_header("Sound Playback Test")
    
    print_info("Testing alfred voice playback...")
    
    try:
        # Add path for imports
        sys.path.insert(0, str(Path.cwd() / '.claude'))
        
        from hooks.voice_notifications.handler import play_voice_sound
        
        # Test a simple sound
        play_voice_sound(
            voice="alfred",
            sound_name="alert",
            mode="sounds",
            sound_theme="default"
        )
        
        print_success("Sound playback successful!")
        print_info("Did you hear the alert sound? If not, check:")
        print("  • System volume is not muted")
        print("  • Audio output device is connected")
        print("  • pygame has audio permissions (macOS)")
        return True
        
    except ImportError as e:
        print_error(f"Could not import handler: {e}")
        print_info("Run: python3 scripts/fix-python39-compatibility.py")
        return False
    except Exception as e:
        print_error(f"Playback failed: {e}")
        return False

def main():
    """Run all verification checks."""
    print(f"{BOLD}{BLUE}")
    print("🔍 Claude Code Alfred Voice Setup Verification")
    print("=" * 60)
    print(f"{RESET}")
    
    results = {
        "Python Version": check_python_version(),
        "Pygame Library": check_pygame(),
        "Directory Structure": check_claude_directory(),
        "Alfred Sounds": check_alfred_sounds(),
        "Settings Config": check_settings(),
        "Handler Support": check_handler(),
        "Sound Mapping": check_sound_mapping(),
    }
    
    # Optional sound test
    if all(results.values()):
        results["Sound Playback"] = test_sound_playback()
    
    # Summary
    print_header("Verification Summary")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for check, result in results.items():
        status = f"{GREEN}PASS{RESET}" if result else f"{RED}FAIL{RESET}"
        print(f"  {check:.<30} [{status}]")
    
    print()
    if passed == total:
        print_success(f"All {total} checks passed! Alfred voice is ready to use.")
    else:
        print_warning(f"{passed}/{total} checks passed")
        print_info("Fix the issues above and run this script again")
        
        if not results.get("Pygame Library"):
            print()
            print_info("Quick fix for pygame:")
            print("  uv add pygame  # or pip install pygame")
        
        if not results.get("Settings Config"):
            print()
            print_info("Quick fix for settings:")
            print("  sed -i '' 's/\"voice\": \".*\"/\"voice\": \"alfred\"/g' .claude/settings.json")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())