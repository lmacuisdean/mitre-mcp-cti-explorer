# Changelog

## v1.3 - Analyst Query Commands

### Added
- Structured analyst commands:
  - `show all`
  - `show severity <severity>`
  - `show actor <actor>`
  - `show tactic <tactic>`
  - `show mitre <id>`

- Confirmation prompt for `show all`
  - Prevents accidental dumping of the entire repository

- Command validation for incomplete analyst queries:
  - `show severity`
  - `show actor`
  - `show tactic`
  - `show mitre`

- Centralized application configuration section:
  - `MAX_QUERY_LENGTH`
  - `goodbyes`
  - `help_examples`
  - `supported_commands`

### Improved
- Help menu now generated from configuration data
- Script organization and readability
- Separation of:
  - System Commands
  - Analyst Commands
  - Search Engine
  - Error Handling
- Searching can now target specific intelligence fields instead of relying solely on free-text matching

### Refactored
- Reorganized script into logical sections:
  - Imports
  - Application Configuration
  - User Input
  - Validation
  - System Commands
  - Analyst Commands
  - Repository Access
  - Search Engine
  - Result Display
  - Error Handling
  - Search Summary

