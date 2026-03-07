# Project – Intramurals Players List
# Displays classmates' names using Python Loops
from pyscript import document


# ── LIST OF PLAYERS ──────────────────────────────────────────
# Edit this list with your actual classmates' last names!
players = [
    "Aclaro",
    "Aguilar",
    "Amante",
    "Banzali",
    "Bulo",
    "Bunado",
    "Casimiro",
    "Catam",
    "Co",
    "Dhaliwal",
    "Flores, E.",
    "Flores, S.",
    "Gill",
    "Ignacio",
    "Lajom",
    "Lim",
    "Lucas",
    "Mandia",
    "Matig-A",
    "Medina",
    "Mendez",
    "Miguel",
    "Misa",
    "Ombao",
    "Osea",
    "Santos",
    "Sumndad",
    "Taguibao",
    "Tiu",
    "Tomas",
    "Uy",
    "Woo",
]


def render_players(filter_type="all"):
    """Renders the player list using a for loop based on filter."""
    player_list = document.getElementById("player-list")
    player_count = document.getElementById("player-count")

    # Clear previous list
    player_list.innerHTML = ""

    # Sort alphabetically using a for loop
    sorted_players = []
    for name in sorted(players):
        sorted_players.append(name)

    # Filter using a for loop
    filtered = []
    for name in sorted_players:
        first_letter = name[0].upper()
        if filter_type == "all":
            filtered.append(name)
        elif filter_type == "A-M":
            if "A" <= first_letter <= "M":
                filtered.append(name)
        elif filter_type == "N-Z":
            if "N" <= first_letter <= "Z":
                filtered.append(name)

    # Update count
    player_count.innerHTML = (
        f"Showing <span>{len(filtered)}</span> "
        f"of <span>{len(sorted_players)}</span> players"
    )

    # Build the list using a for loop with enumerate
    for i, name in enumerate(filtered, start=1):
        li = document.createElement("li")
        li.style.animationDelay = f"{i * 0.03}s"
        li.innerHTML = f'<span class="num">{i}</span>{name}'
        player_list.appendChild(li)


# Run on page load
render_players("all")
