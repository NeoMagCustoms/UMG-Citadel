# Merge Engine

This document describes how the Citadel’s **merge engine** combines multiple UMG blocks into a single executable sleeve or export.

## Responsibilities

1. Validate incoming blocks against the Cantocore + Ledger schemas.
2. Resolve property collisions using the priority rules below.
3. Apply `merge` directives (`append`, `override`, `concat`, etc.).
4. Output a final JSON object ready for export (HTML, JSON, Bolt runtime).

## Priority Rules

| Rank | MOLT Type | Notes |
|------|-----------|-------|
| 1    | **Trigger**     | Highest authority; can override any field. |
| 2    | **Instruction** | Overrides *Subject* and *Primary*. |
| 3    | **Subject**     | Overrides *Primary* only. |
| 4    | **Primary**     | Fallback/default values. |

## Roadmap

The first implementation lives in `src/utils/mergeEngine.js` and currently performs a shallow merge.

Planned milestones:

- Deep merge with array concatenation.
- Conflict reporting & diagnostics.
- Plug‑in hooks for custom merge strategies.
