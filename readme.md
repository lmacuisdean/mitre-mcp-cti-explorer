Threat Intel Enrichment
A Python-based threat intelligence repository and analyst lookup tool that combines local threat data with live MITRE ATT&CK Enrichment through a locally hosted Model Context Protocol (MCP) server.

This project demonstrates how MCP can be used as a security Enrichment layer rather than embedding ATT&CK knowledge directly into an application.

Why I Built This
This project was developed to explore practical applications of threat intelligence Enrichment and Model Context Protocol (MCP) integration.

The goal was to build a lightweight analyst-focused tool capable of searching threat intelligence data locally while dynamically Enrichmenting results with MITRE ATT&CK intelligence through an MCP service.

The project demonstrates:

Python development
Threat intelligence workflows
MITRE ATT&CK integration
MCP client/server communication
Security automation concepts
MCP-based tooling integration
Features
Threat Repository Search
Search threats by:

Threat Actor
Severity
Tactic
MITRE ATT&CK Technique ID
General keyword matching
Structured Analyst Commands
The application supports the following analyst-focused commands:

help
show all
show severity <severity>
show actor <actor>
show tactic <tactic>
show mitre <id>

peace
quit
exit
Examples:

show severity critical
show actor wizard spider
show tactic impact
show mitre t1486
Keyword Search
In addition to structured commands, the application supports free-text searches across all fields in the threat repository.

Examples:

mimikatz
lockbit
wizard spider
critical
impact
t1486
The keyword engine searches across all threat record fields and returns matching results automatically.

MITRE ATT&CK MCP Integration
Local MITRE ATT&CK MCP Server
Official MCP Python SDK
HTTP-based MCP communication
Live ATT&CK Enrichment
Live ATT&CK Enrichment
Threat records automatically retrieve:

Technique Name
ATT&CK Technique ID
Official ATT&CK Description
from the MITRE ATT&CK framework using an MCP service.

Direct ATT&CK Technique Lookup
The application can query ATT&CK techniques directly through the MITRE MCP server, even when a technique is not present in the local repository.

Example:

show mitre t1558
Output:

MITRE ATT&CK LOOKUP

Technique   : Steal or Forge Kerberos Tickets
Attack ID   : T1558
Description : Adversaries may attempt to subvert Kerberos authentication...
This allows Threat Intel Enrichment to operate as both a threat repository and a lightweight ATT&CK knowledge explorer.

Architecture
                ┌──────────────────┐
                │  User Query      │
                └────────┬─────────┘
                         │
                         ▼
             ┌─────────────────────────┐
             │ Threat Intel Enrichment │
             └──────┬────────┬─────────┘
                    │        │
                    │        │
                    ▼        ▼
         Threat Repository    MITRE MCP Server
               (CSV)          (ATT&CK Data)
                    │        ▲
                    └────────┘
                     Enrichment
Threat Intel Enrichment supports two workflows:

Repository Search
Threat Search
      ↓
Repository Match
      ↓
MITRE Enrichment
Direct ATT&CK Lookup
ATT&CK Technique Query
        ↓
MITRE MCP Query
        ↓
ATT&CK Technique Information
This design separates local threat data from ATT&CK knowledge, allowing Enrichment to be sourced dynamically through MCP rather than stored directly inside the application.

Demo Workflow
show mitre t1486
        ↓
Threat Repository Lookup
        ↓
MITRE ID Identified
        ↓
MITRE MCP Query
        ↓
ATT&CK Technique Retrieved
        ↓
Enrichmented Analyst Output
Project Structure

---

threat_intel_Enrichment/
│
├── data/
│   └── threats.csv
│
├── modules/
│
├── main.py
│
├── threat_intel_Enrichment_v1_0.py
├── threat_intel_Enrichment_v1_1.py
├── threat_intel_Enrichment_v1_2.py
├── threat_intel_Enrichment_v1_3.py
├── threat_intel_Enrichment_v1_4.py
│
├── changelog_1.0_to_1.2.md
├── changelog_1.2_to_1.3.md
├── changelog_1.3_to_1.4.md
│
├── requirements.txt
└── README.md
Requirements
Python
Python 3.13+
Dependencies
pip install mcp mitre-mcp
Installation
Create Virtual Environment
uv venv --seed
Activate:

source .venv/Scripts/activate
Install Dependencies
uv pip install --link-mode copy mcp mitre-mcp
Verify installation:

python -c "from mcp import Client; print('MCP OK')"
Expected output:

MCP OK
Running the MITRE MCP Server
Start the MCP server:

mitre-mcp --http --port 8080
Expected output:

MITRE ATT&CK MCP Server is ready
MCP Endpoint: http://localhost:8080/mcp
Leave the server running while using the application.

Running Threat Intel Enrichment
In a second terminal:

source .venv/Scripts/activate

python main.py
Usage Examples
Display Help
help
Search by Severity
show severity critical
Search by Threat Actor
show actor wizard spider
Search by Tactic
show tactic impact
Search by ATT&CK Technique
show mitre t1486
Example Output
============================================================

Threat Name : LockBit
Actor       : LockBit Group
MITRE ID    : T1486
Severity    : Critical
Tactic      : Impact
Description : Ransomware operation known for encrypting data
              to disrupt victim operations

------------------------------------------------------------
MITRE ATT&CK Enrichment
------------------------------------------------------------

Technique   : Data Encrypted for Impact
Attack ID   : T1486

Description : Adversaries may encrypt data on target
              systems or on large numbers of systems
              in a network to interrupt availability
              of system and network resources...

Lookit! 4 threat(s) found!
MITRE ATT&CK Integration
The integrated MITRE ATT&CK MCP service was validated against:

867 Techniques
15 Tactics
193 Threat Groups
845 Software Entries
268 Mitigations
The application currently performs live Enrichment using:

get_technique_by_id
from the MITRE ATT&CK MCP server.

Version History
v1.0
Initial CLI threat lookup functionality
v1.1
Expanded threat repository
Improved search capability
v1.2
Structured analyst commands
MITRE ATT&CK mappings
v1.3
Repository improvements
Enhanced command handling
User experience refinements
v1.4
MITRE ATT&CK MCP integration
Official MCP Python SDK implementation
Local HTTP MCP server deployment
Live ATT&CK technique Enrichment
Dynamic ATT&CK lookups using MITRE IDs
Planned Enhancements
Future improvements under consideration:

ATT&CK mitigation Enrichment
ATT&CK software Enrichment
ATT&CK tactic Enrichment
MITRE threat group correlation
ATT&CK relationship mapping
Result caching
SQLite backend
JSON export
CSV export
REST API interface
Learning Objectives
This project was built to gain hands-on experience with:

Python development
Threat intelligence workflows
MITRE ATT&CK
Model Context Protocol (MCP)
Security automation
AI-enabled tooling
Data Enrichment pipelines
License
This project was developed for educational, portfolio, and professional development purposes.