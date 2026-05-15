"""
Utility functions for the Workout Expert System.

This module handles all terminal output formatting, input validation,
and display helpers. The engine never prints directly — it delegates
all user-facing output to functions in this module.
"""


# ---------------------------------------------------------------------------
# Input Validation
# ---------------------------------------------------------------------------

VALID_AGE_GROUPS = ("young", "adult", "senior")
VALID_GOALS = ("lose_weight", "build_muscle", "improve_endurance", "stay_healthy")
VALID_LEVELS = ("beginner", "intermediate", "advanced")
VALID_AVAILABILITY = ("low", "medium", "high")
VALID_CONDITIONS = ("healthy", "joint_pain", "heart_issue", "overweight")


def validate_choice(value, options, field_name="field"):
    """Validate that a value is one of the allowed options.

    Args:
        value (str): The user-provided value.
        options (tuple): Tuple of valid option strings.
        field_name (str): Name of the field (for error messages).

    Returns:
        str: The validated value (lowercased and stripped).

    Raises:
        ValueError: If the value is not in the allowed options.
    """
    cleaned = value.strip().lower()
    if cleaned not in options:
        valid_list = ", ".join(options)
        raise ValueError(
            f"Invalid {field_name}: '{value}'. Must be one of: {valid_list}"
        )
    return cleaned


def validate_age(value):
    """Validate age group input.

    Args:
        value (str): The age group string.

    Returns:
        str: Validated age group.
    """
    return validate_choice(value, VALID_AGE_GROUPS, "age group")


def validate_goal(value):
    """Validate fitness goal input.

    Args:
        value (str): The goal string.

    Returns:
        str: Validated goal.
    """
    return validate_choice(value, VALID_GOALS, "goal")


def validate_level(value):
    """Validate fitness level input.

    Args:
        value (str): The fitness level string.

    Returns:
        str: Validated fitness level.
    """
    return validate_choice(value, VALID_LEVELS, "fitness level")


def validate_availability(value):
    """Validate weekly availability input.

    Args:
        value (str): The availability string.

    Returns:
        str: Validated availability.
    """
    return validate_choice(value, VALID_AVAILABILITY, "availability")


def validate_condition(value):
    """Validate health condition input.

    Args:
        value (str): The condition string.

    Returns:
        str: Validated condition.
    """
    return validate_choice(value, VALID_CONDITIONS, "condition")


# ---------------------------------------------------------------------------
# Display Formatting
# ---------------------------------------------------------------------------

SEPARATOR = "=" * 60
THIN_SEP = "-" * 60


def display_header():
    """Print the application header banner."""
    print()
    print(SEPARATOR)
    print("  💪  WORKOUT EXPERT SYSTEM")
    print("  ──  AI-Powered Fitness Recommendation Engine")
    print(SEPARATOR)
    print()


def display_footer():
    """Print the application footer."""
    print()
    print(THIN_SEP)
    print("  Thank you for using Workout Expert System! 🏋️")
    print("  Stay consistent and enjoy your training.")
    print(THIN_SEP)
    print()


def display_warning(message):
    """Format and print a warning message.

    Args:
        message (str): The warning text to display.
    """
    print()
    print("  +" + "-" * 56 + "+")
    # Wrap message to fit in box
    words = message.split()
    line = "  | "
    for word in words:
        if len(line) + len(word) + 1 > 57:
            print(line.ljust(58) + "|")
            line = "  | " + word
        else:
            line += (" " if len(line) > 4 else "") + word
    if line.strip():
        print(line.ljust(58) + "|")
    print("  +" + "-" * 56 + "+")


def display_recommendation(rec):
    """Format and print a workout recommendation.

    Args:
        rec (dict): Recommendation dictionary with keys:
            workout_type, intensity, frequency, duration, details.
    """
    intensity_icons = {
        "low": "🟢 Low",
        "moderate": "🟡 Moderate",
        "high": "🔴 High",
    }

    print()
    print(SEPARATOR)
    print(f"  🔥 YOUR WORKOUT PLAN")
    print(SEPARATOR)
    print()
    print(f"  💪 Workout Type : {rec['workout_type']}")
    print(f"  📊 Intensity    : {intensity_icons.get(rec['intensity'], rec['intensity'])}")
    print(f"  📅 Frequency    : {rec['frequency']}")
    print(f"  ⏱️  Duration     : {rec['duration']}")
    print()
    print(f"  📋 Exercises:")
    print(THIN_SEP)
    for i, exercise in enumerate(rec["details"], 1):
        print(f"     {i}. {exercise}")
    print(THIN_SEP)


def display_profile_summary(profile):
    """Format and print the user's input profile.

    Args:
        profile (dict): Dictionary with keys: age, goal, level, available, condition.
    """
    labels = {
        "age": "🎂 Age Group",
        "goal": "🎯 Goal",
        "level": "📈 Fitness Level",
        "available": "📅 Availability",
        "condition": "🏥 Condition",
    }

    print()
    print("  YOUR PROFILE:")
    print(THIN_SEP)
    for key, label in labels.items():
        value = profile.get(key, "N/A").replace("_", " ").title()
        print(f"  {label:20s} : {value}")
    print(THIN_SEP)


def prompt_field(prompt_text, validator, options_display):
    """Prompt the user for a field value with validation.

    Keeps prompting until a valid value is entered.

    Args:
        prompt_text (str): The prompt message.
        validator (callable): Validation function that returns cleaned value.
        options_display (str): Display string showing valid options.

    Returns:
        str: The validated value.
    """
    while True:
        print(f"\n  {prompt_text}")
        print(f"  Options: {options_display}")
        try:
            value = input("  > ").strip()
            return validator(value)
        except ValueError as e:
            print(f"  ❌ {e}")
