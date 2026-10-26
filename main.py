# ============================================================
# IMPORTS
# ============================================================
import asyncio
from mcp import Client
import csv
import random

# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

MAX_QUERY_LENGTH = 50

goodbyes = [
    "See ya, wouldn't want to be ya...",
    "May your detections be true and your false positives few.",
    "The threat actor has left the chat.",
    "Another day, another IOC.",
    "Stay frosty!",
    "No indicators remaining. Standing down.",
    "Mission complete. Exiting threat matrix.",
    "Alright move along, nothing to see here."
]

help_examples = [
    "Threat Name  (example: mimikatz)",
    "Threat Actor (example: wizard spider)",
    "Severity     (example: critical)",
    "Tactic       (example: execution)",
    "MITRE ID     (example: t1486)"
]

supported_commands = [
    "help - Show this menu",
    "show all - Display all threat records",
    "show severity <severity> - Display all threats of a specific severity",
    "show actor <actor> - Display threats associated with a threat actor",
    "show tactic <tactic> - Display threats associated with a specific tactic",
    "show mitre <id> - Display threats mapped to a MITRE technique",
    "peace, quit or exit - Exits the application"
]

# ============================================================
# MITRE MCP ENRICHMENT
# ============================================================

async def enrich_mitre(technique_id):

    try:

        async with Client("http://localhost:8080/mcp") as client:

            result = await client.call_tool(
                "get_technique_by_id",
                {
                    "technique_id": technique_id.upper(),
                    "domain": "enterprise-attack"
                }
            )

            return result.structured_content

    except Exception as e:
        return {"error": str(e)}


# ============================================================
# MAIN APPLICATION LOOP
# ============================================================

def main():

    while True:

        # --------------------------------------------------------
        # USER INPUT
        # --------------------------------------------------------

        search_term = input("\nAre you threatening me? ('peace' to exit): ").lower()

        # --------------------------------------------------------
        # SEARCH CONTROL VARIABLES
        # --------------------------------------------------------

        found = False
        match_count = 0

        show_all = False
        show_name = None
        show_severity = None
        show_actor = None
        show_tactic = None
        show_mitre = None

        # --------------------------------------------------------
        # INPUT VALIDATION
        # --------------------------------------------------------

        if not search_term.strip():
            print("Error: Human input appears to be missing.")
            continue

        if len(search_term) > MAX_QUERY_LENGTH:
            print("Easy there, Shakespeare. Keep your search under 50 characters.")
            continue

        # --------------------------------------------------------
        # SYSTEM COMMANDS
        # --------------------------------------------------------

        if search_term in ["peace", "quit", "exit"]:
            print(random.choice(goodbyes))
            break

        if search_term == "help":

            print("\n" + "=" * 60)
            print("Stop it, get some - HELP")
            print("=" * 60)

            print("You can search by:")

            for example in help_examples:
                print(f"  {example}")

            print()
            print("Commands:")

            for command in supported_commands:
                print(f"  {command}")

            print("=" * 60)
            continue

        # --------------------------------------------------------
        # ANALYST COMMANDS
        # --------------------------------------------------------

        if search_term.startswith("show threat name "):
            show_name = search_term.replace(
                "show threat name ",
                ""
            ).strip()

        if search_term == "show severity":
            print("Usage: show severity <severity>")
            continue

        if search_term == "show actor":
            print("Usage: show actor <actor>")
            continue

        if search_term == "show tactic":
            print("Usage: show tactic <tactic>")
            continue

        if search_term == "show mitre":
            print("Usage: show mitre <id>")
            continue

        if search_term == "show all":

            confirm = input(
                "\nWARNING: This may annoy your scroll wheel. Continue? (y/n): "
            ).lower()

            if confirm == "y":
                show_all = True
            else:
                print("Whew, close call!")
                continue

        if search_term.startswith("show severity "):
            show_severity = search_term.replace(
                "show severity ",
                ""
            ).strip()

        if search_term.startswith("show actor "):
            show_actor = search_term.replace(
                "show actor ",
                ""
        ).strip()

        if search_term.startswith("show tactic "):
            show_tactic = search_term.replace(
                "show tactic ",
                ""
            ).strip()

        if search_term.startswith("show mitre "):
            show_mitre = search_term.replace(
                "show mitre ",
                ""
        ).strip()

        # --------------------------------------------------------
        # THREAT REPOSITORY ACCESS
        # --------------------------------------------------------

        try:

            with open(
                "data/threats.csv",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.DictReader(file)

                # ------------------------------------------------
                # SEARCH ENGINE
                # ------------------------------------------------

                for row in reader:

                    if (
                        show_all
                        or (show_severity and show_severity == row["severity"].lower())
                        or (show_actor and show_actor == row["threat_actor"].lower())
                        or (show_tactic and show_tactic == row["tactic"].lower())
                        or (show_mitre and show_mitre == row["mitre_id"].lower())
                        or (show_name and show_name == row["threat_name"].lower())
                        or any(search_term in str(value).lower() for value in row.values())
                    ):

                        found = True
                        match_count += 1

                        # ----------------------------------------
                        # RESULT DISPLAY
                        # ----------------------------------------

                        print("\n" + "=" * 60)
                        print(f"Threat Name : {row['threat_name']}")
                        print(f"Actor       : {row['threat_actor']}")
                        print(f"MITRE ID    : {row['mitre_id']}")
                        print(f"Severity    : {row['severity']}")
                        print(f"Tactic      : {row['tactic']}")
                        print(f"Description : {row['description']}")

                        enrichment = asyncio.run(
                            enrich_mitre(row["mitre_id"])
                        )

                        technique = enrichment["technique"]

                        print("\n" + "-" * 60)
                        print("MITRE ATT&CK ENRICHMENT")
                        print("-" * 60)

                        print(f"Technique   : {technique['name']}")
                        print(f"Attack ID   : {technique['mitre_id']}")
                        print(f"Description : {technique['description']}")

        # --------------------------------------------------------
        # ERROR HANDLING
        # --------------------------------------------------------

        except FileNotFoundError:
            print("\nERROR: Threat repository not found.")
            print("Expected location: data/threats.csv")
            print("As Matt S. would say, 'CYBER ATTACK!'")
            break

        # --------------------------------------------------------
        # SEARCH SUMMARY
        # --------------------------------------------------------

        if found:
            print(f"\nLookit! {match_count} threat(s) found!")

        elif show_mitre:

            enrichment = asyncio.run(
                enrich_mitre(show_mitre)
            )

            if "technique" in enrichment:

                technique = enrichment["technique"]

                print("\n" + "=" * 60)
                print("MITRE ATT&CK LOOKUP")
                print("=" * 60)

                print(f"Technique   : {technique['name']}")
                print(f"Attack ID   : {technique['mitre_id']}")
                print(f"Description : {technique['description']}")

            else:
                print("Bruh, no threats found and no ATT&CK technique exists.")

        else:
            print("Bruh, no threats found. Maybe try 'Help' for search tips.")

# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()