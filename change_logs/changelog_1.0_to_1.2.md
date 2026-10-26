# Changelog

## v1.2 - Hardened MVP
### Added
- Empty query validation
- Maximum query length validation (50 chars)
- Help command (`help`)
- Multiple exit commands (`peace`, `quit`, `exit`)
- Randomized exit messages
- CSV file missing error handling (`FileNotFoundError`)

### Improved
- Search result formatting
- User guidance and examples
- Search result counting
- General CLI usability

### Fixed
- UTF-8 BOM handling (`utf-8-sig`)
- Clean handling of missing search results

---

## v1.1 - Interactive Search Experience
### Added
- Persistent search loop (`while True`)
- Match counter
- Formatted threat output
- Decorative result separators
- Random farewell message system

### Improved
- Readability of search results
- Interactive user experience

---

## v1.0 - Initial Repository Search
### Added
- Local CSV threat repository
- Threat intelligence dataset
- Free-text searching across all fields
- Threat details display:
  - Threat Name
  - Threat Actor
  - MITRE ID
  - Severity
  - Tactic
  - Description

### Achieved
- Proof of concept for local CTI repository querying