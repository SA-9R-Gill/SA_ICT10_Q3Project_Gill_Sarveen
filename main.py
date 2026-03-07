# Seatwork 2 – Intramurals Eligibility Checker
from pyscript import document


def intrams_checker(event):
    output = document.getElementById("output")
    image = document.getElementById("image")

    # Clear output
    output.innerHTML = ""
    image.innerHTML = ""

    # Get inputs
    registration = document.querySelector('input[name="registration"]:checked')
    clearance = document.querySelector('input[name="clearance"]:checked')

    if registration is None or clearance is None:
        output.innerHTML = "⚠️ Please complete all required fields."
        return

    registration = registration.value
    clearance = clearance.value
    grade = int(document.getElementById("level").value)
    section = document.getElementById("section").value

    # Eligibility checks
    if registration != "registered":
        output.innerHTML = "❌ Not Eligible.<br>Please finish online registration."
        return

    if clearance != "cleared":
        output.innerHTML = "❌ Not Eligible.<br>Medical clearance required."
        return

    if grade < 7 or grade > 10:
        output.innerHTML = "❌ Only Grades 7–10 may join Intramurals."
        return

    # Team data (SIMPLE & SAFE)
    teams = {
        "emerald": ("Blue Bears", "blue_bears.jpg", "#0d6efd"),
        "ruby": ("Red Bulldogs", "red_bulldogs.jpg", "#dc3545"),
        "sapphire": ("Yellow Tigers", "yellow_tigers.jpg", "#ffc107"),
        "topaz": ("Green Hornets", "green_hornets.jpg", "#198754"),
    }

    team_name, team_image, team_color = teams[section]

    # Output text
    output.innerHTML = (
        "🎉 <b>Congratulations!</b><br>"
        "You are eligible for Intramurals.<br>"
        f"Your team is <span style='color:{team_color}'>{team_name}</span>."
    )

    # Output image
    image.innerHTML = (
        f"<img src='{team_image}' "
        f"style='max-width:200px; margin-top:15px; "
        f"border-radius:12px; box-shadow:0 8px 20px rgba(0,0,0,0.3);'>"
    )
