# AETHER CODING STANDARDS
Version: 1.0
Status: Active

---

# 1. Purpose

This document defines the mandatory coding standards for every source file developed within the AETHER platform.

Every contributor, AI system, automation, and future developer shall follow these standards without exception.

---

# 2. Core Principles

- Readability before cleverness.
- Simplicity before complexity.
- Consistency before preference.
- Modularity before duplication.
- Maintainability before speed.

---

# 3. File Header

Every Python file shall begin with:

"""
=========================================================
AETHER

Module Name

Version

Author

=========================================================
"""

---

# 4. Naming Rules

Classes:
PascalCase

Example:

ApplicationController

NavigationManager

ResearchEngine

---

Functions:

snake_case

Example:

load_project()

save_workspace()

generate_report()

---

Variables:

snake_case

Example:

current_page

project_manager

research_data

---

Constants:

UPPER_CASE

Example:

MAX_PROJECTS

DEFAULT_THEME

APP_VERSION

---

# 5. File Size

Target:

Less than 500 lines.

Maximum:

1000 lines.

If exceeded:

Split into modules.

---

# 6. Class Rules

Each class shall have one responsibility.

Large classes must be divided.

Inheritance should be minimized.

Composition is preferred.

---

# 7. Function Rules

Functions should perform one logical task.

Target:

Less than 40 lines.

Maximum:

80 lines.

---

# 8. Comments

Explain WHY.

Avoid comments that only explain WHAT.

Good:

# Load configuration before UI starts.

Bad:

# Set x = 5

---

# 9. Imports

Standard Library

↓

Third Party

↓

AETHER Modules

Never mix the order.

---

# 10. Documentation

Every public class shall include a docstring.

Every public function shall include a docstring.

---

# 11. Error Handling

Never ignore exceptions.

Catch only expected exceptions.

Provide meaningful error messages.

---

# 12. Logging

No print() statements outside debugging.

Production events shall use the Logger.

---

# 13. Testing

Every new module should be testable independently.

---

# 14. Git

One feature

↓

One commit

One bug fix

↓

One commit

---

# 15. Definition of Done

A task is complete only when:

✓ Code compiles.

✓ No errors.

✓ Documentation updated.

✓ Tested.

✓ Git committed.