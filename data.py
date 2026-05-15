"""
Static workout database for the Workout Expert System.

This module contains all exercise descriptions, workout plans,
and warning messages. The engine imports from here — no hardcoded
strings should exist in engine.py.
"""

# ---------------------------------------------------------------------------
# Warning Messages
# ---------------------------------------------------------------------------

WARNING_JOINT_PAIN = (
    "⚠️ You have joint pain. Avoid high-impact exercises like running or "
    "jumping. Focus on low-impact activities such as swimming, cycling, "
    "or yoga. Consult a physician before starting any new program."
)

WARNING_HEART_ISSUE = (
    "⚠️ You have a heart condition. Keep your heart rate in a safe zone "
    "and avoid very high-intensity exercises. Always warm up gradually "
    "and stop immediately if you feel dizzy or chest pain. "
    "Medical clearance is strongly recommended."
)

WARNING_OVERWEIGHT = (
    "⚠️ You are overweight. Start with low-impact exercises to protect "
    "your joints. Gradually increase intensity over weeks. Combine "
    "exercise with a balanced diet for best results. "
    "Consider consulting a nutritionist."
)

WARNING_SENIOR = (
    "⚠️ As a senior, prioritize balance and flexibility exercises to "
    "prevent falls. Avoid heavy lifting without supervision. "
    "Include warm-up and cool-down in every session."
)

# ---------------------------------------------------------------------------
# Exercise Database — grouped by workout type
# ---------------------------------------------------------------------------

EXERCISES = {
    "cardio": {
        "name": "Cardio Training",
        "description": "Aerobic exercises that elevate heart rate and burn calories.",
        "exercises": {
            "beginner": [
                "Brisk Walking — 20-30 min at moderate pace",
                "Stationary Cycling — 15-20 min at low resistance",
                "Elliptical Machine — 15 min at easy pace",
                "Dancing — 20 min of freestyle movement",
            ],
            "intermediate": [
                "Jogging — 25-35 min at comfortable pace",
                "Cycling — 30 min at moderate resistance",
                "Jump Rope — 15 min with 30-sec rest intervals",
                "Swimming — 20-30 min of laps",
                "Stair Climbing — 15 min at steady pace",
            ],
            "advanced": [
                "Running — 40-60 min at tempo pace",
                "HIIT Sprints — 20 min (30s sprint / 30s rest)",
                "Rowing Machine — 30 min at high resistance",
                "Cycling — 45-60 min at high intensity",
                "Box Jumps — 4 sets of 12 reps",
            ],
        },
    },
    "strength": {
        "name": "Strength Training",
        "description": "Resistance-based exercises to build muscle mass and strength.",
        "exercises": {
            "beginner": [
                "Bodyweight Squats — 3 sets of 12 reps",
                "Push-ups (knee variation) — 3 sets of 8 reps",
                "Dumbbell Rows — 3 sets of 10 reps (light weight)",
                "Plank Hold — 3 sets of 20 seconds",
                "Lunges — 3 sets of 10 each leg",
            ],
            "intermediate": [
                "Barbell Squats — 4 sets of 10 reps",
                "Bench Press — 4 sets of 8 reps",
                "Deadlifts — 3 sets of 8 reps",
                "Pull-ups — 3 sets of 6-8 reps",
                "Overhead Press — 3 sets of 10 reps",
                "Plank Hold — 3 sets of 45 seconds",
            ],
            "advanced": [
                "Heavy Squats — 5 sets of 5 reps (85% 1RM)",
                "Bench Press — 5 sets of 5 reps (85% 1RM)",
                "Deadlifts — 5 sets of 3 reps (90% 1RM)",
                "Weighted Pull-ups — 4 sets of 6 reps",
                "Military Press — 4 sets of 6 reps",
                "Barbell Rows — 4 sets of 8 reps",
                "Core Circuit — 4 rounds of 3 exercises",
            ],
        },
    },
    "flexibility": {
        "name": "Flexibility & Yoga",
        "description": "Stretching and yoga to improve mobility, balance, and recovery.",
        "exercises": {
            "beginner": [
                "Cat-Cow Stretch — 10 slow repetitions",
                "Standing Hamstring Stretch — 30 sec each leg",
                "Child's Pose — hold 1 minute",
                "Neck and Shoulder Rolls — 2 minutes",
                "Seated Spinal Twist — 30 sec each side",
            ],
            "intermediate": [
                "Sun Salutation (Surya Namaskar) — 5 rounds",
                "Warrior I & II Poses — hold 30 sec each",
                "Pigeon Pose — 1 min each side",
                "Bridge Pose — 3 sets of 30 seconds",
                "Downward Dog — hold 1 minute",
                "Standing Balance (Tree Pose) — 30 sec each leg",
            ],
            "advanced": [
                "Full Yoga Flow — 45-60 min session",
                "Deep Hip Opener Sequence — 15 min",
                "Handstand Practice — 10 min against wall",
                "Advanced Backbends (Wheel Pose) — 3 holds",
                "Crow Pose — 5 attempts, hold 15 sec",
                "Splits Training — 10 min progressive stretch",
            ],
        },
    },
    "hiit": {
        "name": "HIIT (High-Intensity Interval Training)",
        "description": "Short bursts of intense exercise alternated with rest periods.",
        "exercises": {
            "beginner": [
                "Jumping Jacks — 30 sec on / 30 sec rest × 8 rounds",
                "Bodyweight Squats — 20 sec on / 40 sec rest × 6 rounds",
                "Mountain Climbers — 20 sec on / 40 sec rest × 6 rounds",
                "High Knees — 20 sec on / 40 sec rest × 6 rounds",
            ],
            "intermediate": [
                "Burpees — 30 sec on / 20 sec rest × 8 rounds",
                "Kettlebell Swings — 30 sec on / 15 sec rest × 10 rounds",
                "Box Jumps — 30 sec on / 20 sec rest × 8 rounds",
                "Battle Ropes — 30 sec on / 20 sec rest × 8 rounds",
                "Tuck Jumps — 20 sec on / 20 sec rest × 8 rounds",
            ],
            "advanced": [
                "Tabata Protocol — 20 sec max effort / 10 sec rest × 8 rounds × 4 exercises",
                "Sprint Intervals — 200m sprint / 200m walk × 10 rounds",
                "Plyometric Circuit — 5 exercises, 45 sec each, minimal rest",
                "Assault Bike — 30 sec max / 30 sec rest × 12 rounds",
            ],
        },
    },
    "mixed": {
        "name": "Mixed / General Fitness",
        "description": "Balanced combination of cardio, strength, and flexibility.",
        "exercises": {
            "beginner": [
                "Walking — 20 min brisk pace",
                "Bodyweight Circuit (squats, push-ups, lunges) — 2 rounds",
                "Stretching — 10 min full body",
                "Light Dumbbell Exercises — 15 min",
            ],
            "intermediate": [
                "Jogging — 20 min warm-up",
                "Circuit Training (5 exercises, 3 rounds)",
                "Core Work — 15 min (planks, crunches, leg raises)",
                "Cool-down Stretches — 10 min",
            ],
            "advanced": [
                "Running — 30 min tempo run",
                "Superset Strength Circuit — 4 supersets, 4 rounds",
                "Plyometrics — 15 min explosive movements",
                "Yoga Cool-down — 15 min",
            ],
        },
    },
    "low_impact": {
        "name": "Low-Impact Training",
        "description": "Joint-friendly exercises suitable for recovery or medical conditions.",
        "exercises": {
            "beginner": [
                "Water Walking (pool) — 20 min",
                "Seated Leg Raises — 3 sets of 10",
                "Arm Circles with Light Weights — 2 min",
                "Chair Yoga — 15 min routine",
                "Gentle Stretching — 10 min",
            ],
            "intermediate": [
                "Swimming Laps — 20-30 min",
                "Recumbent Bike — 25 min at moderate effort",
                "Resistance Band Exercises — 20 min full body",
                "Tai Chi — 20 min practice",
                "Pilates Mat Work — 25 min",
            ],
            "advanced": [
                "Swimming — 45 min with interval sets",
                "Cycling (low resistance) — 40 min",
                "Advanced Pilates Reformer — 45 min",
                "Kayaking / Rowing — 30 min steady state",
            ],
        },
    },
}

# ---------------------------------------------------------------------------
# Frequency & Duration recommendations
# ---------------------------------------------------------------------------

FREQUENCY = {
    "low": "1-2 days/week",
    "medium": "3-4 days/week",
    "high": "5-6 days/week",
}

DURATION = {
    "beginner": {
        "low": "20-30 minutes per session",
        "medium": "25-35 minutes per session",
        "high": "30-40 minutes per session",
    },
    "intermediate": {
        "low": "30-40 minutes per session",
        "medium": "35-50 minutes per session",
        "high": "45-60 minutes per session",
    },
    "advanced": {
        "low": "40-50 minutes per session",
        "medium": "50-70 minutes per session",
        "high": "60-90 minutes per session",
    },
}

# ---------------------------------------------------------------------------
# Intensity mapping — base intensity before condition adjustments
# ---------------------------------------------------------------------------

INTENSITY = {
    "beginner": "low",
    "intermediate": "moderate",
    "advanced": "high",
}

# ---------------------------------------------------------------------------
# Goal → Workout type mapping
# ---------------------------------------------------------------------------

GOAL_WORKOUT_MAP = {
    "lose_weight": {
        "beginner": "cardio",
        "intermediate": "hiit",
        "advanced": "hiit",
    },
    "build_muscle": {
        "beginner": "strength",
        "intermediate": "strength",
        "advanced": "strength",
    },
    "improve_endurance": {
        "beginner": "cardio",
        "intermediate": "cardio",
        "advanced": "mixed",
    },
    "stay_healthy": {
        "beginner": "flexibility",
        "intermediate": "mixed",
        "advanced": "mixed",
    },
}

# ---------------------------------------------------------------------------
# Test Scenarios — predefined user profiles for automated testing
# ---------------------------------------------------------------------------

TEST_SCENARIOS = {
    "beginner_weight_loss": {
        "age": "young",
        "goal": "lose_weight",
        "level": "beginner",
        "condition": "healthy",
        "available": "medium",
    },
    "advanced_muscle": {
        "age": "adult",
        "goal": "build_muscle",
        "level": "advanced",
        "condition": "healthy",
        "available": "high",
    },
    "senior_health": {
        "age": "senior",
        "goal": "stay_healthy",
        "level": "beginner",
        "condition": "joint_pain",
        "available": "low",
    },
    "endurance_intermediate": {
        "age": "adult",
        "goal": "improve_endurance",
        "level": "intermediate",
        "condition": "healthy",
        "available": "medium",
    },
    "overweight_beginner": {
        "age": "adult",
        "goal": "lose_weight",
        "level": "beginner",
        "condition": "overweight",
        "available": "low",
    },
}
