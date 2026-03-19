import os
import sys

# ensure workspace root is on python path so we can import the game logic module
# FIX: Added this path setup with Copilot so pytest can import logic_utils reliably.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess

def test_winning_guess():
    # guessing the secret should return "Win" and a celebratory message
    # FIX: Updated with AI help to assert both outcome and user-facing message.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be Too High and message
    # FIX: Added regression check (with Copilot) to confirm the hint says LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # hint should direct the player downward

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be Too Low and message
    # FIX: Added regression check (with Copilot) to confirm the hint says HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message