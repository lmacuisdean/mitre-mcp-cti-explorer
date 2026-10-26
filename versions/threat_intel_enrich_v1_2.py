import csv
import random

goodbyes = [
    "See ya, wouldn't want to be ya...",
    "May your detections be true and your false positives few.",
    "The threat actor has left the chat.",
    "Another day, another IOC.",
    "Stay frosty!",
    "No indicators remaining. Standing down.",
    "Mission complete. Exiting threat matrix.",
    "Keep your logs close and your adversaries closer."
]

while True:

    search_term = input(
        "\nAre you threatening me? ('peace' to exit): "
    ).lower()

    if not search_term.strip():
        print("Error: Human input appears to be missing.")
        continue

    if len(search_term) > 50:
        print("Easy there, Shakespeare. Keep your search under 50 characters.")
        continue

    if search_term in ["peace", "quit", "exit"]:
        print(random.choice(goodbyes))
        break

    if search_term == "help":
        print("\n" + "=" * 60)
        print("Stop it, get some - HELP")
        print("=" * 60)
        print("You can search by:")
        print("  Threat Name  (example: mimikatz)")
        print("  Threat Actor (example: wizard spider)")
        print("  Severity     (example: critical)")
        print("  Tactic       (example: execution)")
        print("  MITRE ID     (example: t1486)")
        print()
        print("Commands:")
        print("  help   - Show this menu")
        print("  peace  - Exit the application")
        print("  quit   - Exit the application")
        print("=" * 60)
        continue

    found = False
    match_count = 0

    try:
        with open("data/threats.csv", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:

                if any(search_term in str(value).lower() for value in row.values()):

                    found = True
                    match_count += 1

                    print("\n" + "=" * 60)
                    print(f"Threat Name : {row['threat_name']}")
                    print(f"Actor       : {row['threat_actor']}")
                    print(f"MITRE ID    : {row['mitre_id']}")
                    print(f"Severity    : {row['severity']}")
                    print(f"Tactic      : {row['tactic']}")
                    print(f"Description : {row['description']}")
                    print("=" * 60)

    except FileNotFoundError:
        print("\nERROR: Threat repository not found.")
        print("Expected location: data/threats.csv")
        print("As Matt Scheurer would say, 'CYBER ATTACK!'")
        break

    if found:
        print(f"\nLookit! {match_count} threat(s) found!")
    else:
        print("Alright move along, nothing to see here.")