#!/usr/bin/env python3
"""Test script for Zoe (Premium) voice"""

import sys
from pathlib import Path

# Add .claude directory to path
claude_dir = Path(__file__).parent.parent / ".claude"
sys.path.insert(0, str(claude_dir))

# Import the handler
from hooks.voice_notifications.handler import play_voice_sound

def test_zoe_voice():
    """Test Zoe premium voice"""
    
    print("🎤 Testing Zoe (Premium) voice...")
    print("=" * 50)
    
    test_messages = [
        ("task_complete", "Task complete"),
        ("file_read", "Reading file"),
        ("code_edit", "Editing code"),
        ("work_finished", "Work finished"),
    ]
    
    for sound_name, description in test_messages:
        print(f"\nTesting: {description}...")
        try:
            # Test with Zoe voice mode
            play_voice_sound(
                voice="Zoe",
                sound_name=sound_name,
                mode="voice",  # IMPORTANT: voice mode, not sounds
                sound_theme="default"
            )
            print(f"✅ Zoe said: {description}")
        except Exception as e:
            print(f"❌ Failed: {e}")
    
    print("\n" + "=" * 50)
    print("📝 Note: Zoe should speak the messages, not play sounds")
    print("If you don't hear Zoe:")
    print("1. Check System Settings → Accessibility → Spoken Content")
    print("2. Download Zoe (Premium) voice if needed")
    print("3. Make sure settings.json has mode='voice' not 'sounds'")

if __name__ == "__main__":
    test_zoe_voice()