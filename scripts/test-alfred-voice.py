#!/usr/bin/env python3
"""Test script for alfred voice notifications"""

import sys
import os
from pathlib import Path

# Add .claude directory to path
claude_dir = Path(__file__).parent.parent / ".claude"
sys.path.insert(0, str(claude_dir))

# Import the handler
from hooks.voice_notifications.handler import play_voice_sound, get_context_aware_sound_name

def test_alfred_voices():
    """Test various alfred voice sounds"""
    
    print("🎵 Testing alfred voice notifications...")
    print("=" * 50)
    
    # Test different sound types
    test_sounds = [
        ("file_read", "Testing file read sound"),
        ("code_edit", "Testing code edit sound"),
        ("search", "Testing search sound"),
        ("system_command", "Testing system command sound"),
        ("work_finished", "Testing work finished sound"),
        ("alert", "Testing alert sound"),
        ("updating_todo_list", "Testing todo list sound"),
    ]
    
    for sound_name, description in test_sounds:
        print(f"\n{description}...")
        try:
            # Test with alfred voice
            play_voice_sound(
                voice="alfred",
                sound_name=sound_name,
                mode="sounds",
                sound_theme="default"
            )
            print(f"✅ {sound_name} played successfully")
        except Exception as e:
            print(f"❌ Failed to play {sound_name}: {e}")
    
    # Test context-aware sounds
    print("\n" + "=" * 50)
    print("Testing context-aware sounds...")
    
    test_contexts = [
        ("Read", {"file_path": "test.py"}, "Python file read"),
        ("Edit", {"file_path": "test.ts"}, "TypeScript file edit"),
        ("Bash", {"command": "git status"}, "Git status command"),
    ]
    
    for tool, args, description in test_contexts:
        print(f"\n{description}...")
        try:
            sound_name = get_context_aware_sound_name(tool, args)
            print(f"  Resolved sound: {sound_name}")
            
            play_voice_sound(
                voice="alfred",
                sound_name=sound_name,
                mode="sounds",
                sound_theme="default"
            )
            print(f"✅ Context-aware sound played successfully")
        except Exception as e:
            print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_alfred_voices()