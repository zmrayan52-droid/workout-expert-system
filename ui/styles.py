"""
CSS color and typography constants for the Workout Expert System UI.

These constants are used by app.py and components.py to maintain
consistent styling across all templates.
"""

# ---------------------------------------------------------------------------
# Color Palette — Dark Fitness Theme
# ---------------------------------------------------------------------------

BG_PRIMARY = "#0f1117"
BG_CARD = "#1a1d27"
BG_INPUT = "#252836"
ACCENT = "#6c63ff"
ACCENT_HOVER = "#574fd6"
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#a0a3b1"
SUCCESS = "#2ecc71"
WARNING = "#f39c12"
DANGER = "#e74c3c"
BORDER = "#2d3149"

# ---------------------------------------------------------------------------
# Typography
# ---------------------------------------------------------------------------

FONT_FAMILY = "'Inter', 'Segoe UI', sans-serif"

# ---------------------------------------------------------------------------
# Intensity → Color mapping
# ---------------------------------------------------------------------------

INTENSITY_COLORS = {
    "low": SUCCESS,
    "moderate": WARNING,
    "high": DANGER,
}

INTENSITY_LABELS = {
    "low": "Low",
    "moderate": "Moderate",
    "high": "High",
}
