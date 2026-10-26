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

    if search_term == "peace" or search_term == "quit":
        print(random.choice(goodbyes))
        break

    found = False
    match_count = 0

    with open("data/threats.csv", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required_headers = {
            "threat_name",
            "threat_actor",
            "mitre_id",
            "severity",
            "tactic",
            "description"
        }

        missing_headers = required_headers - set(reader.fieldnames)

        if missing_headers:
            print("\nERROR: Repository validation failed.")
            print(f"Missing headers: {', '.join(missing_headers)}")
            break

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

    if found:
        print(f"\nLookit! {match_count} threat(s) found!")

    if not found:
        print("Alright move along, nothing to see here.")