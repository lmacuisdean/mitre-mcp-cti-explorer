import csv

while True:

    search_term = input(
        "\nAre you threatening me? ('peace' to exit): "
    ).lower()

    if search_term == "peace":
        print("See ya wouldnt want to be ya...")
        break

    found = False
    match_count = 0

    with open("data/threats.csv", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if any(search_term in str(value).lower() for value in row.values()):

                found = True
                match_count += 1

                print()
                print(f"Threat Name : {row['threat_name']}")
                print(f"Actor       : {row['threat_actor']}")
                print(f"MITRE ID    : {row['mitre_id']}")
                print(f"Severity    : {row['severity']}")
                print(f"Tactic      : {row['tactic']}")
                print(f"Description : {row['description']}")

    if found:
        print(f"\nLookit! {match_count} threat(s) found!")

    if not found:
        print("Alright move along, nothing to see here.")