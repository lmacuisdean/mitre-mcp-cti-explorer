# Changelog: Version 1.3 → 1.4

## Threat Intel Enrich v1.4
**Release Date:** October 2026

### Overview

Version 1.4 introduces live MITRE ATT&CK enrichment through a locally hosted Model Context Protocol (MCP) server. Search results are now automatically enriched with ATT&CK framework data based on associated MITRE technique IDs.

---

## Added

### MITRE ATT&CK MCP Integration

- Integrated the official MITRE ATT&CK MCP Server.
- Added support for HTTP-based MCP communication.
- Configured local MCP endpoint:
  - `http://localhost:8080/mcp`
- Implemented ATT&CK lookups using the official MCP Python SDK.

### Automatic ATT&CK Enrichment

Search results now automatically retrieve:

- ATT&CK Technique Name
- ATT&CK Technique ID
- Official ATT&CK Technique Description

using the MITRE ID mapped to each threat record.

### Live Analyst Context

Threat records are now enriched in real time:

```text
Threat Name : LockBit
Actor       : LockBit Group
MITRE ID    : T1486

------------------------------------------------------------
MITRE ATT&CK ENRICHMENT
------------------------------------------------------------
Technique   : Data Encrypted for Impact
Attack ID   : T1486
Description : Adversaries may encrypt data...