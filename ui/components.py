"""
Reusable HTML component renderers for the Workout Expert System UI.

Each function returns an HTML string for a specific UI element.
These are used by app.py to inject dynamic content into templates.
"""

from ui.styles import INTENSITY_COLORS, INTENSITY_LABELS


def render_warning(message):
    """Return an HTML warning alert box.

    Args:
        message (str): The warning text to display.

    Returns:
        str: HTML string for a styled warning alert.
    """
    return f"""
    <div class="warning-card">
        <div class="warning-icon">&#9888;&#65039;</div>
        <div class="warning-text">{message}</div>
    </div>
    """


def render_recommendation_card(rec):
    """Return an HTML card displaying a workout recommendation.

    Args:
        rec (dict): Recommendation with keys:
            workout_type, intensity, frequency, duration, details.

    Returns:
        str: HTML string for the recommendation card.
    """
    intensity_badge = render_intensity_badge(rec["intensity"])
    exercises_html = ""
    for i, exercise in enumerate(rec["details"], 1):
        exercises_html += f'<li><span class="exercise-num">{i}</span>{exercise}</li>\n'

    return f"""
    <div class="recommendation-card">
        <div class="rec-header">
            <h2 class="rec-title">&#128170; {rec['workout_type']}</h2>
            {intensity_badge}
        </div>
        <div class="rec-stats">
            <div class="stat-item">
                <span class="stat-icon">&#128197;</span>
                <div class="stat-content">
                    <span class="stat-label">Frequency</span>
                    <span class="stat-value">{rec['frequency']}</span>
                </div>
            </div>
            <div class="stat-item">
                <span class="stat-icon">&#9201;&#65039;</span>
                <div class="stat-content">
                    <span class="stat-label">Duration</span>
                    <span class="stat-value">{rec['duration']}</span>
                </div>
            </div>
        </div>
        <div class="exercises-section">
            <h3 class="exercises-title">&#128203; Your Exercises</h3>
            <ol class="exercises-list">
                {exercises_html}
            </ol>
        </div>
    </div>
    """


def render_intensity_badge(level):
    """Return an HTML colored badge for the intensity level.

    Args:
        level (str): Intensity level — 'low', 'moderate', or 'high'.

    Returns:
        str: HTML string for the intensity badge.
    """
    color = INTENSITY_COLORS.get(level, "#a0a3b1")
    label = INTENSITY_LABELS.get(level, level.title())
    return f'<span class="intensity-badge" style="background-color: {color}20; color: {color}; border: 1px solid {color}40;">{label} Intensity</span>'


def render_profile_summary(profile):
    """Return an HTML summary card showing the user's input profile.

    Args:
        profile (dict): Dictionary with keys: age, goal, level, available, condition.

    Returns:
        str: HTML string for the profile summary card.
    """
    labels = {
        "age": ("&#127874;", "Age Group"),
        "goal": ("&#127919;", "Goal"),
        "level": ("&#128200;", "Fitness Level"),
        "available": ("&#128197;", "Availability"),
        "condition": ("&#127973;", "Condition"),
    }

    rows = ""
    for key, (icon, label) in labels.items():
        value = profile.get(key, "N/A").replace("_", " ").title()
        rows += f"""
        <div class="profile-row">
            <span class="profile-icon">{icon}</span>
            <span class="profile-label">{label}</span>
            <span class="profile-value">{value}</span>
        </div>
        """

    return f"""
    <div class="profile-card">
        <h3 class="profile-title">Your Profile</h3>
        {rows}
    </div>
    """
