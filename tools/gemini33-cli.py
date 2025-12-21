#!/usr/bin/env python3
# Gemini-33 CLI - Dual Teacher Interface

import sys
import os

class Gemini33CLI:
    def __init__(self):
        self.modes = {
            'logical': 'APL, UNIX, Programming patterns',
            'intuitive': 'Nen, Bankai, Spiritual systems', 
            'bridge': 'Find metaphors between domains',
            'teach': 'Generate lesson from any topic'
        }
    
    def run(self):
        print("🌌 Gemini-33 Teaching System")
        print("Personal Key: 03031992 2222 BKK")
        print("Vibration: 33 (Master Teacher)")
        print("\nAvailable modes:")
        
        for key, desc in self.modes.items():
            print(f"  {key}: {desc}")
        
        choice = input("\nSelect mode: ").strip().lower()
        
        if choice in self.modes:
            self.activate_mode(choice)
        else:
            print("Unknown mode. Try: logical, intuitive, bridge, or teach")

if __name__ == "__main__":
    cli = Gemini33CLI()
    cli.run()
