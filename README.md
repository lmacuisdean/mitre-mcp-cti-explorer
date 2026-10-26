# Threat Intel Enrichment 

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v1.4.0-orange)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![MCP](https://img.shields.io/badge/Model_Context_Protocol-MCP-purple)

A Python-based threat intelligence repository and analyst lookup tool that combines local threat data with live MITRE ATT&CK enrichment through a locally hosted Model Context Protocol (MCP) server.

This project demonstrates how MCP can be used as a security enrichment layer rather than embedding ATT&CK knowledge directly into an application.

---

## Table of Contents

- [Why I Built This](#why-i-built-this)
- [Features](#features)
- [Architecture](#architecture)
- [Demo Workflow](#demo-workflow)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the MITRE MCP Server](#running-the-mitre-mcp-server)
- [Running Threat Intel Enrich](#running-threat-intel-enrich)
- [Usage Examples](#usage-examples)
- [Example Output](#example-output)
- [MITRE ATT&CK Integration](#mitre-attck-integration)
- [Version History](#version-history)
- [Planned Enhancements](#planned-enhancements)
- [Learning Objectives](#learning-objectives)
- [License](#license)

---

## Why I Built This

This project was developed to explore practical applications of threat intelligence enrichment and Model Context Protocol (MCP) integration.

The goal was to build a lightweight analyst-focused tool capable of searching threat intelligence data locally while dynamically enriching results with MITRE ATT&CK intelligence through an MCP service.

The project demonstrates:

- Python development
- Threat intelligence workflows
- MITRE ATT&CK integration
- MCP client/server communication
- Security automation concepts
- MCP-based tooling integration

---

## Features

### Threat Repository Search

Search threats by:

- Threat Actor
- Severity
- Tactic
- MITRE ATT&CK Technique ID
- General keyword matching

### Structured Analyst Commands

```text
help
show all
show severity <severity>
show actor <actor>
show tactic <tactic>
show mitre <id>

peace
quit
exit
```

Examples:

```text
show severity critical
show actor wizard spider
show tactic impact
show mitre t1486
```

### Keyword Search

The application supports free-text searches across all fields in the repository.

Examples:

```text
mimikatz
lockbit
wizard spider
critical
impact
t1486
```

### MITRE ATT&CK MCP Integration

- Local MITRE ATT&CK MCP Server
- Official MCP Python SDK
- HTTP-based MCP communication
- Live ATT&CK enrichment

### ATT&CK Enrichment

Threats mapped to MITRE ATT&CK techniques automatically retrieve:

- Technique Name
- ATT&CK Technique ID
- ATT&CK Description

### Direct ATT&CK Technique Lookup

The application can query ATT&CK techniques directly through the MITRE MCP server, even when a technique is not present in the local repository.

Example:

```text
show mitre t1558
```

Output:

```text
MITRE ATT&CK LOOKUP

Technique   : Steal or Forge Kerberos Tickets
Attack ID   : T1558
Description : Adversaries may attempt to subvert Kerberos authentication...
```

This allows the application to function as both a threat repository and a lightweight ATT&CK knowledge explorer.

---

## Architecture

```text
                ┌──────────────────┐
                │    User Query    │
                └────────┬─────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Threat Intel Enrich │
              └──────┬────────┬─────┘
                     │        │
                     │        │
                     ▼        ▼
        Threat Repository    MITRE MCP Server
              (CSV)          (ATT&CK Data)
                     │        ▲
                     └────────┘
                     Enrichment
```

### Repository Search Workflow

```text
Threat Search
      ↓
Repository Match
      ↓
MITRE Enrichment
```

### Direct ATT&CK Lookup Workflow

```text
ATT&CK Technique Query
        ↓
MITRE MCP Query
        ↓
ATT&CK Technique Information
```

---

## Demo Workflow

```text
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
Enriched Analyst Output
```

---

## Project Structure

```text
mitre-mcp-cti-explorer/
│
├── data/
│   └── threats.csv
│
├── change_logs/
│   ├── changelog_1.0_to_1.2.md
│   ├── changelog_1.2_to_1.3.md
│   └── changelog_1.3_to_1.4.md
│
├── versions/
│   ├── threat_intel_enrich_v1_0.py
│   ├── threat_intel_enrich_v1_1.py
│   ├── threat_intel_enrich_v1_2.py
│   ├── threat_intel_enrich_v1_3.py
│   └── threat_intel_enrich_v1_4.py
│
├── main.py
├── release.md
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Requirements

### Python

```text
Python 3.13+
```

### Dependencies

```text
mcp>=2.3.0
mitre-mcp>=0.4.0
```

---

## Installation

Create a virtual environment:

```bash
uv venv --seed
```

Activate it:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
uv pip install --link-mode copy -r requirements.txt
```

Verify installation:

```bash
python -c "from mcp import Client; print('MCP OK')"
```

Expected output:

```text
MCP OK
```

---

## Running the MITRE MCP Server

```bash
mitre-mcp --http --port 8080
```

Expected output:

```text
MITRE ATT&CK MCP Server is ready
MCP Endpoint: http://localhost:8080/mcp
```

Leave this terminal running.

---

## Running Threat Intel Enrich

Open a second terminal:

```bash
source .venv/Scripts/activate

python main.py
```

---

## Usage Examples

Display help:

```text
help
```

Search by severity:

```text
show severity critical
```

Search by actor:

```text
show actor wizard spider
```

Search by tactic:

```text
show tactic impact
```

Search by ATT&CK technique:

```text
show mitre t1486
```

Direct ATT&CK lookup:

```text
show mitre t1558
```

---

## Example Output

```text
============================================================

Threat Name : LockBit
Actor       : LockBit Group
MITRE ID    : T1486
Severity    : Critical
Tactic      : Impact

------------------------------------------------------------
MITRE ATT&CK ENRICHMENT
------------------------------------------------------------

Technique   : Data Encrypted for Impact
Attack ID   : T1486

Description : Adversaries may encrypt data on target systems
              or on large numbers of systems in a network...

Lookit! 4 threat(s) found!
```

---

## MITRE ATT&CK Integration

The integrated MITRE ATT&CK MCP service was validated against:

- 867 Techniques
- 15 Tactics
- 193 Threat Groups
- 845 Software Entries
- 268 Mitigations

Current ATT&CK retrieval is performed using:

```text
get_technique_by_id
```

from the MITRE ATT&CK MCP server.

---

## Version History

### v1.0

- Initial CLI threat lookup functionality

### v1.1

- Expanded threat repository
- Improved search capability

### v1.2

- Structured analyst commands
- MITRE ATT&CK mappings

### v1.3

- Repository improvements
- Enhanced command handling
- User experience refinements

### v1.4

- MITRE ATT&CK MCP integration
- Official MCP Python SDK implementation
- Local HTTP MCP server deployment
- Live ATT&CK technique enrichment
- Direct ATT&CK technique lookup
- MCP-powered ATT&CK exploration

---

## Planned Enhancements

- ATT&CK mitigation enrichment
- ATT&CK software enrichment
- ATT&CK tactic enrichment
- MITRE threat group correlation
- ATT&CK relationship mapping
- Result caching
- SQLite backend
- JSON export
- CSV export
- REST API interface

---

## Learning Objectives

This project was built to gain practical experience with:

- Python development
- Threat intelligence workflows
- MITRE ATT&CK
- Model Context Protocol (MCP)
- Security automation
- Data enrichment pipelines
- AI-enabled tooling integration

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
