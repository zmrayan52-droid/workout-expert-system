"""
Flask application for the Workout Expert System web UI.

This module defines two routes:
    GET  /       — serves the input form page
    POST /result — runs the expert engine and displays results

All business logic is delegated to engine.py.
All HTML rendering is delegated to components.py.
"""

import sys
import os

# Add project root to path so we can import engine, facts, data
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from engine import WorkoutExpertSystem
from facts import UserProfile
from ui.components import (
    render_warning,
    render_recommendation_card,
    render_profile_summary,
)

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the home page with the fitness profile input form.

    Returns:
        Rendered index.html template.
    """
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    """Process the form submission and display workout recommendations.

    Reads user profile from the form, runs the expert engine,
    and passes the results to the result template.

    Returns:
        Rendered result.html template with recommendations and warnings.
    """
    # Collect form data
    profile = {
        "age": request.form.get("age", "adult"),
        "goal": request.form.get("goal", "stay_healthy"),
        "level": request.form.get("level", "beginner"),
        "available": request.form.get("available", "medium"),
        "condition": request.form.get("condition", "healthy"),
    }

    # Run the expert engine
    engine = WorkoutExpertSystem()
    engine.reset()
    engine.declare(UserProfile(
        age=profile["age"],
        goal=profile["goal"],
        level=profile["level"],
        available=profile["available"],
        condition=profile["condition"],
    ))
    engine.run()

    # Render HTML components
    warnings_html = ""
    for warning_msg in engine.warnings:
        warnings_html += render_warning(warning_msg)

    recommendations_html = ""
    for rec in engine.recommendations:
        recommendations_html += render_recommendation_card(rec)

    profile_html = render_profile_summary(profile)

    return render_template(
        "result.html",
        profile_html=profile_html,
        warnings_html=warnings_html,
        recommendations_html=recommendations_html,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
