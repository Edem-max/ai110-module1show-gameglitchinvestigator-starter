from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting Bug Fix 1: hint messages were swapped ---

def test_hint_go_lower_when_guess_too_high():
    # BUG FIX 1: When guess > secret, player needs to go LOWER.
    # The original code incorrectly returned "Go HIGHER!" in this case.
    outcome, _ = check_guess(80, 40)
    assert outcome == "Too High", "Guess above secret should return 'Too High'"

def test_hint_go_higher_when_guess_too_low():
    # BUG FIX 1: When guess < secret, player needs to go HIGHER.
    # The original code incorrectly returned "Go LOWER!" in this case.
    outcome, _ = check_guess(10, 70)
    assert outcome == "Too Low", "Guess below secret should return 'Too Low'"


# --- Tests targeting Bug Fix 1 (continued): secret was cast to string on even attempts ---

def test_check_guess_with_integer_secret():
    # BUG FIX 1: Secret must always be compared as an integer.
    # Original code converted secret to str on even attempts, causing
    # lexicographic comparisons that broke hints (e.g. "5" > "90" is False).
    outcome1, _ = check_guess(5, 90)
    outcome2, _ = check_guess(95, 90)
    assert outcome1 == "Too Low"   # 5 < 90, should go higher
    assert outcome2 == "Too High"  # 95 > 90, should go lower

def test_check_guess_not_affected_by_string_secret():
    # BUG FIX 1: Passing a string secret (the old bug) would cause wrong results
    # for numbers like 5 vs "90" due to lexicographic ordering ("5" > "90").
    # Now secret is always an int, so this comparison must be numeric.
    outcome, _ = check_guess(5, 90)
    assert outcome != "Too High", (
        "5 < 90 numerically — should be 'Too Low', not 'Too High'"
    )


# --- Tests targeting range fix: all difficulties now use the same range (1–100) ---

def test_all_difficulties_same_range():
    # FIX: Range is fixed at 1–100 for all difficulties so the number pool
    # never changes — only the attempt count varies per difficulty.
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        assert low == 1 and high == 100, (
            f"Expected range 1–100 for {difficulty}, got {low}–{high}"
        )

def test_range_does_not_vary_by_difficulty():
    # FIX: Easy and Hard must return the same range; previously they differed.
    easy_range = get_range_for_difficulty("Easy")
    hard_range = get_range_for_difficulty("Hard")
    assert easy_range == hard_range, (
        "All difficulties should share the same range (1–100)"
    )
