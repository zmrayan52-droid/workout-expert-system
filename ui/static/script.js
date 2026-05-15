/**
 * Workout Expert System — Form Validation Script
 *
 * Validates that all radio button groups have a selection
 * before allowing form submission.
 */

(function () {
    "use strict";

    const form = document.getElementById("workout-form");
    if (!form) return;

    const requiredGroups = ["age", "goal", "level", "available", "condition"];
    const errorBox = document.getElementById("validation-error");

    form.addEventListener("submit", function (e) {
        let allValid = true;

        for (const groupName of requiredGroups) {
            const radios = form.querySelectorAll(`input[name="${groupName}"]`);
            const checked = Array.from(radios).some((r) => r.checked);
            if (!checked) {
                allValid = false;
                break;
            }
        }

        if (!allValid) {
            e.preventDefault();
            if (errorBox) {
                errorBox.style.display = "block";
                errorBox.style.animation = "none";
                // Trigger reflow to restart animation
                errorBox.offsetHeight;
                errorBox.style.animation = "shake 0.4s ease-in-out";
            }
        } else {
            if (errorBox) {
                errorBox.style.display = "none";
            }
        }
    });

    // Add visual feedback when radio cards are selected
    const allRadios = form.querySelectorAll('input[type="radio"]');
    allRadios.forEach(function (radio) {
        radio.addEventListener("change", function () {
            // Hide error when user starts selecting
            if (errorBox) {
                errorBox.style.display = "none";
            }

            // Add ripple effect to selected card
            const card = this.closest(".radio-card");
            if (card) {
                const content = card.querySelector(".card-content");
                content.style.animation = "none";
                content.offsetHeight;
                content.style.animation = "card-select 0.3s ease-out";
            }
        });
    });

    // Card select micro-animation
    const style = document.createElement("style");
    style.textContent = `
        @keyframes card-select {
            0% { transform: scale(0.95); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1) translateY(-2px); }
        }
    `;
    document.head.appendChild(style);
})();
