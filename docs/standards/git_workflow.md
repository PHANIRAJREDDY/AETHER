# AETHER GIT WORKFLOW
Version: 1.0
Status: Active

---

# Purpose

This document defines the official Git workflow for the AETHER project.

Every code change shall follow this workflow.

---

# Branch Strategy

Main Branch

main

Development Branch

develop

Feature Branches

feature/<feature-name>

Bug Fixes

bugfix/<bug-name>

Release Branches

release/<version>

Hot Fixes

hotfix/<version>

---

# Feature Workflow

1. Create feature branch

↓

2. Implement feature

↓

3. Test feature

↓

4. Update documentation

↓

5. Update CHANGELOG

↓

6. Commit

↓

7. Merge into develop

---

# Commit Message Format

feat: New feature

fix: Bug fix

docs: Documentation update

refactor: Internal improvements

style: Formatting

test: Tests

build: Build system

chore: Maintenance

Examples

feat: Added Navigation Manager

fix: Resolved startup configuration issue

docs: Updated architecture specification

---

# Pull Request Checklist

✓ Code compiles

✓ No known errors

✓ Documentation updated

✓ Tests completed

✓ Standards followed

---

# Release Workflow

Update VERSION

↓

Update CHANGELOG

↓

Tag Release

↓

Merge into main

↓

Archive Release

---

# Rule

No code shall be merged unless it satisfies the Definition of Done.