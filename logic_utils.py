def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored this helper from app.py into logic_utils.py with Copilot Agent to make game rules testable.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    # default to normal range if unknown difficulty
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Added AI-assisted input validation for empty and non-numeric guesses.
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        # allow floats and convert to int
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low".  Message is a hint
    for the player (higher/lower arrow and text).
    """
    # FIX: Used Copilot suggestion, then corrected hint direction logic after manual play-testing.
    # normalize types so strings can be compared to ints if needed
    try:
        if guess == secret:
            return "Win", "🎉 Correct!"

        if guess > secret:
            # guess is too high, tell the player to go lower
            return "Too High", "📉 Go LOWER!"
        else:
            # guess is too low, tell the player to go higher
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # non-comparable types - coerce to string and compare
        g = str(guess)
        s = str(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Scoring behavior was extracted with AI help so score updates can be unit-tested separately.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
