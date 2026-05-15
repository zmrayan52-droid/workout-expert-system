"""
Main entry point for the Workout Expert System.

This module provides:
    - Interactive CLI mode: prompts the user for fitness profile inputs
    - Test mode (--test <name>): runs predefined test scenarios
    - Debug mode (--debug): enables verbose rule tracing

Usage:
    python main.py                          # Interactive mode
    python main.py --test beginner_weight_loss  # Single test
    python main.py --test all               # All tests
    python main.py --debug                  # Debug mode
"""

import sys
import argparse

# Force UTF-8 encoding for Windows console compatibility
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from engine import WorkoutExpertSystem
from facts import UserProfile
from data import TEST_SCENARIOS
from utils import (
    display_header,
    display_footer,
    display_warning,
    display_recommendation,
    display_profile_summary,
    prompt_field,
    validate_age,
    validate_goal,
    validate_level,
    validate_availability,
    validate_condition,
)


def run_engine(profile, debug=False):
    """Create, configure, and run the expert engine.

    Args:
        profile (dict): User profile with keys: age, goal, level,
                        available, condition.
        debug (bool): If True, enable verbose rule tracing output.

    Returns:
        tuple: (recommendations list, warnings list)
    """
    engine = WorkoutExpertSystem()
    engine.reset()
    engine.declare(UserProfile(
        age=profile["age"],
        goal=profile["goal"],
        level=profile["level"],
        available=profile["available"],
        condition=profile["condition"],
    ))

    if debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)

    engine.run()
    return engine.recommendations, engine.warnings


def interactive_mode(debug=False):
    """Run the expert system in interactive CLI mode.

    Prompts the user for all 5 profile fields, runs the engine,
    and displays the results.

    Args:
        debug (bool): If True, enable verbose rule tracing.
    """
    display_header()
    print("  Please answer the following questions about your fitness profile.\n")

    age = prompt_field(
        "What is your age group?",
        validate_age,
        "young (15-25) | adult (26-45) | senior (46+)"
    )

    goal = prompt_field(
        "What is your fitness goal?",
        validate_goal,
        "lose_weight | build_muscle | improve_endurance | stay_healthy"
    )

    level = prompt_field(
        "What is your fitness level?",
        validate_level,
        "beginner | intermediate | advanced"
    )

    available = prompt_field(
        "How many days per week can you train?",
        validate_availability,
        "low (1-2) | medium (3-4) | high (5+)"
    )

    condition = prompt_field(
        "Do you have any health conditions?",
        validate_condition,
        "healthy | joint_pain | heart_issue | overweight"
    )

    profile = {
        "age": age,
        "goal": goal,
        "level": level,
        "available": available,
        "condition": condition,
    }

    display_profile_summary(profile)

    recommendations, warnings = run_engine(profile, debug=debug)

    for warning_msg in warnings:
        display_warning(warning_msg)

    for rec in recommendations:
        display_recommendation(rec)

    display_footer()


def test_mode(test_name, debug=False):
    """Run one or all predefined test scenarios.

    Args:
        test_name (str): Name of the test scenario, or 'all' to run all.
        debug (bool): If True, enable verbose rule tracing.
    """
    if test_name == "all":
        scenarios = TEST_SCENARIOS
    else:
        if test_name not in TEST_SCENARIOS:
            print(f"\n  ❌ Unknown test scenario: '{test_name}'")
            print(f"  Available tests: {', '.join(TEST_SCENARIOS.keys())}")
            sys.exit(1)
        scenarios = {test_name: TEST_SCENARIOS[test_name]}

    for name, profile in scenarios.items():
        print("\n" + "=" * 60)
        print(f"  TEST SCENARIO: {name}")
        print("=" * 60)

        display_profile_summary(profile)

        recommendations, warnings = run_engine(profile, debug=debug)

        for warning_msg in warnings:
            display_warning(warning_msg)

        if recommendations:
            for rec in recommendations:
                display_recommendation(rec)
            print("  ✅ Test PASSED — recommendation generated successfully.")
        else:
            print("  ❌ Test FAILED — no recommendation was generated!")

        print()

    if test_name == "all":
        print("═" * 60)
        print(f"  🏁 All {len(scenarios)} test scenarios completed.")
        print("═" * 60)


def main():
    """Parse command-line arguments and run the appropriate mode."""
    parser = argparse.ArgumentParser(
        description="Workout Expert System — AI-powered fitness recommendations"
    )
    parser.add_argument(
        "--test",
        type=str,
        default=None,
        help="Run a test scenario (name or 'all')"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable verbose rule tracing"
    )

    args = parser.parse_args()

    if args.test:
        test_mode(args.test, debug=args.debug)
    else:
        interactive_mode(debug=args.debug)


if __name__ == "__main__":
    main()
