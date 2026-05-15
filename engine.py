"""
Workout Expert Engine — rule-based recommendation system.

This module contains the WorkoutExpertSystem class, a KnowledgeEngine
subclass that uses backward-chaining rules to generate personalized
workout recommendations based on user profile facts.

All rules are organized by category:
    1. Warning rules   — fire when medical conditions are detected
    2. Goal-based rules — match goal + level to recommend workout type
    3. Adjustment rules — modify intensity based on age and conditions
"""

from experta import KnowledgeEngine, Rule, DefFacts, OR, AND, MATCH

from facts import UserProfile, WorkoutRecommendation, Warning
from data import (
    WARNING_JOINT_PAIN,
    WARNING_HEART_ISSUE,
    WARNING_OVERWEIGHT,
    WARNING_SENIOR,
    EXERCISES,
    FREQUENCY,
    DURATION,
    INTENSITY,
    GOAL_WORKOUT_MAP,
)


class WorkoutExpertSystem(KnowledgeEngine):
    """Expert system engine that generates workout recommendations.

    The engine processes a UserProfile fact and produces:
      - One or more Warning facts (if medical conditions are present)
      - One WorkoutRecommendation fact with the full workout plan

    Usage:
        engine = WorkoutExpertSystem()
        engine.reset()
        engine.declare(UserProfile(age='adult', goal='lose_weight',
                                   level='beginner', available='medium',
                                   condition='healthy'))
        engine.run()
    """

    def __init__(self):
        """Initialize the engine and result containers."""
        super().__init__()
        self.recommendations = []
        self.warnings = []

    @DefFacts()
    def initial_facts(self):
        """Declare initial facts when the engine resets.

        This is called automatically by engine.reset().
        No initial facts are needed — the user profile is declared externally.
        """
        yield from ()

    def reset(self, *args, **kwargs):
        """Reset the engine and clear previous results.

        Overrides the parent reset to also clear the result lists.
        """
        super().reset(*args, **kwargs)
        self.recommendations = []
        self.warnings = []

    # -----------------------------------------------------------------------
    # Warning Rules — fire when medical conditions are detected
    # -----------------------------------------------------------------------

    @Rule(UserProfile(condition="joint_pain"))
    def warn_joint_pain(self):
        """WHEN: User has joint_pain condition.
        WHY: High-impact exercises may worsen joint problems.
        ACTION: Declare a warning about joint-safe exercise selection.
        """
        warning = Warning(message=WARNING_JOINT_PAIN)
        self.declare(warning)
        self.warnings.append(WARNING_JOINT_PAIN)

    @Rule(UserProfile(condition="heart_issue"))
    def warn_heart_issue(self):
        """WHEN: User has a heart_issue condition.
        WHY: Intense cardiovascular stress is dangerous with heart conditions.
        ACTION: Declare a warning about heart-safe intensity limits.
        """
        warning = Warning(message=WARNING_HEART_ISSUE)
        self.declare(warning)
        self.warnings.append(WARNING_HEART_ISSUE)

    @Rule(UserProfile(condition="overweight"))
    def warn_overweight(self):
        """WHEN: User is overweight.
        WHY: Excess weight increases joint stress during exercise.
        ACTION: Declare a warning about low-impact starting exercises.
        """
        warning = Warning(message=WARNING_OVERWEIGHT)
        self.declare(warning)
        self.warnings.append(WARNING_OVERWEIGHT)

    @Rule(UserProfile(age="senior"))
    def warn_senior(self):
        """WHEN: User is a senior (46+).
        WHY: Seniors have higher risk of falls and injury.
        ACTION: Declare a warning about balance and safety precautions.
        """
        warning = Warning(message=WARNING_SENIOR)
        self.declare(warning)
        self.warnings.append(WARNING_SENIOR)

    # -----------------------------------------------------------------------
    # Recommendation Rules — goal-based workout selection
    # -----------------------------------------------------------------------

    @Rule(
        UserProfile(
            goal="lose_weight",
            level=MATCH.level,
            available=MATCH.available,
            age=MATCH.age,
            condition=MATCH.condition,
        )
    )
    def recommend_weight_loss(self, level, available, age, condition):
        """WHEN: User's goal is to lose weight.
        WHY: Weight loss requires calorie-burning exercises; type depends on level.
        ACTION: Recommend cardio (beginners) or HIIT (intermediate/advanced),
                adjusted for medical conditions.
        """
        self._generate_recommendation(
            "lose_weight", level, available, age, condition
        )

    @Rule(
        UserProfile(
            goal="build_muscle",
            level=MATCH.level,
            available=MATCH.available,
            age=MATCH.age,
            condition=MATCH.condition,
        )
    )
    def recommend_muscle_building(self, level, available, age, condition):
        """WHEN: User's goal is to build muscle.
        WHY: Muscle growth requires progressive resistance training.
        ACTION: Recommend strength training at the appropriate intensity level.
        """
        self._generate_recommendation(
            "build_muscle", level, available, age, condition
        )

    @Rule(
        UserProfile(
            goal="improve_endurance",
            level=MATCH.level,
            available=MATCH.available,
            age=MATCH.age,
            condition=MATCH.condition,
        )
    )
    def recommend_endurance(self, level, available, age, condition):
        """WHEN: User's goal is to improve endurance.
        WHY: Endurance requires sustained cardiovascular training.
        ACTION: Recommend cardio (beginner/intermediate) or mixed (advanced).
        """
        self._generate_recommendation(
            "improve_endurance", level, available, age, condition
        )

    @Rule(
        UserProfile(
            goal="stay_healthy",
            level=MATCH.level,
            available=MATCH.available,
            age=MATCH.age,
            condition=MATCH.condition,
        )
    )
    def recommend_general_health(self, level, available, age, condition):
        """WHEN: User's goal is to stay healthy.
        WHY: General health benefits from balanced, varied exercise.
        ACTION: Recommend flexibility (beginners) or mixed training (others).
        """
        self._generate_recommendation(
            "stay_healthy", level, available, age, condition
        )

    # -----------------------------------------------------------------------
    # Internal Helper — builds the recommendation from data.py lookups
    # -----------------------------------------------------------------------

    def _generate_recommendation(self, goal, level, available, age, condition):
        """Build and declare a WorkoutRecommendation fact.

        This method looks up the appropriate workout type, exercises,
        frequency, duration, and intensity from data.py, then applies
        condition-based and age-based adjustments.

        Args:
            goal (str): The user's fitness goal.
            level (str): The user's fitness level.
            available (str): The user's weekly availability.
            age (str): The user's age group.
            condition (str): The user's health condition.
        """
        # Determine workout type from goal × level mapping
        workout_key = GOAL_WORKOUT_MAP.get(goal, {}).get(level, "mixed")

        # Override to low-impact if user has joint pain or heart issue
        if condition in ("joint_pain", "heart_issue"):
            workout_key = "low_impact"

        # Override to low-impact for overweight beginners
        if condition == "overweight" and level == "beginner":
            workout_key = "low_impact"

        # Get workout data
        workout_data = EXERCISES.get(workout_key, EXERCISES["mixed"])
        workout_type = workout_data["name"]
        exercises = workout_data["exercises"].get(level, workout_data["exercises"]["beginner"])

        # Determine intensity with adjustments
        intensity = INTENSITY.get(level, "moderate")

        # Lower intensity for medical conditions
        if condition in ("joint_pain", "heart_issue"):
            intensity = "low"
        elif condition == "overweight" and intensity == "high":
            intensity = "moderate"

        # Lower intensity for seniors
        if age == "senior" and intensity == "high":
            intensity = "moderate"

        # Get frequency and duration
        frequency = FREQUENCY.get(available, "3-4 days/week")
        duration = DURATION.get(level, DURATION["beginner"]).get(
            available, "30-40 minutes per session"
        )

        # Declare the recommendation fact
        rec = WorkoutRecommendation(
            workout_type=workout_type,
            intensity=intensity,
            frequency=frequency,
            duration=duration,
            details=exercises,
        )
        self.declare(rec)
        self.recommendations.append({
            "workout_type": workout_type,
            "intensity": intensity,
            "frequency": frequency,
            "duration": duration,
            "details": exercises,
        })
