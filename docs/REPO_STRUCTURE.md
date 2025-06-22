# 📂 NeoUMG Citadel Git Structure Blueprint (Bolt-Ready)

This document defines the canonical structure, rules, and operator instructions for maintaining the UMG Citadel GitHub repository. This ensures Bolt compatibility, schema consistency, and developer clarity.

---

## 📽️ 1. Core Directory Layout

```
UMG-Citadel/
│
├── /data/
│   ├── block_index.json
│   ├── vault_index.json
│   ├── project_templates/
│   │   └── pitch_deck_starter.vault.json
│   ├── sleeve_presets/
│   │   ├── bolt_color_sleeve_stack.json
│   │   └── default_merge_stack.json
│   └── umg_blocks/
│       ├── business/
│       ├── chatbot/
│       ├── website/
│       ├── philosophy/
│       └── blueprint/
│
├── /docs/
│   ├── README.md
│   ├── MOLT_TYPE_GUIDE.md
│   ├── COLOR_SYSTEM.md
│   ├── MERGE_ENGINE.md
│   ├── VAULT_IMPORTS.md
│   └── CITADEL_FLOW.md
│
├── /public/
│   ├── icons/
│   └── *.svg
│
├── /src/
│   ├── utils/
│   │   └── mergeEngine.js
│   └── ai/
│       └── poeAssistant.js
```

---

## ✅ 2. Block Template Standard

All `.json` blocks must follow the **UMG Schema v3.0**, including:

- `"molt_type"` (one of 8)
- `"bolt_ready": true`
- `"code_modules": []` (not `code_injection`)
- `"ledger"` with authorship + edit log
- `"runtime_behavior_flags"` and `"snap_config"`

Each block must be added to:
- `/data/umg_blocks/{category}/`
- `/data/block_index.json`

---

## ✅ 3. Markdown Docs (Located in /docs)

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `MOLT_TYPE_GUIDE.md` | Canonical molt_type rules |
| `COLOR_SYSTEM.md` | Color coding by type |
| `MERGE_ENGINE.md` | Logic rules for snap and merge |
| `VAULT_IMPORTS.md` | Rules for importing/exporting vaults |
| `CITADEL_FLOW.md` | UX structure (sleeves, stacks, blocks) |

---

## ✅ 4. Operator Rules for Adding Content

| Task | Behavior |
|------|----------|
| Add Block | Save to `/data/umg_blocks/{category}/`, append to block_index.json |
| Add Vault | Save as `.vault.json` to `/data/project_templates/` |
| Add Sleeve Preset | Save to `/data/sleeve_presets/` |
| Add Icon | Save to `/public/icons/` |
| Add Doc | Save to `/docs/` using Markdown |
| Add Logic | Save to `/src/utils/` or `/src/ai/` depending on function |

---

## ✅ 5. Bolt Export Readiness

Each block must include:

```json
"export_config": {
  "bolt_ready": true,
  "deployable": true,
  "formats": ["json", "tsx", "md"]
}
```

This ensures only deployable blocks are loaded into Bolt and UI-rendered.

---

## ✅ 6. Example Bolt Instruction Template

```
Please add a new block to /data/umg_blocks/business/

- Label: “Exit Strategy Plan”
- MOLT: Primary
- Description: Strategy for IPO or acquisition exits
- Code modules: frontend + prompt
- Mark bolt_ready: true and deployable: true
- Use schema v3.0 and ledger origin: "Christopher L Haynes", verified_by: "PoeUMG"
```

---

## 🧠 TL;DR

- ✅ Canonical block schema enforced
- ✅ All logic + markdown lives in predictable folders
- ✅ Operator = logic compiler + gatekeeper
- ✅ You = architect of logic for Bolt app and beyond

© NeoUMG 2025 – Structured by PoeUMG + Christopher Lars Haynes
