# 🟡 UMG Citadel Git Folder Structure (Base Layer + Block Genesis + Orchestration Extensions + Color System)

This scaffold defines the canonical folder layout for the UMG Citadel repository.
It follows the logic defined in the Universal Modular Generation framework and supports full Bolt integration and agent orchestration via MCP, LangChain, or OpenAI.

---

## 📁 Root Directory
```
/ (root)
├── README.md                  # Project overview + quickstart
├── /data/                     # UMG blocks + logic
├── /docs/                     # Canonical specifications + logic docs
├── /public/                   # Icons, UI visuals
├── /src/                      # App + merge engine logic
```

---

## 📁 /data/
```
/data/
├── blocks/                  # All logic blocks, sorted by molt_type
│   ├── primary/
│   ├── subject/
│   ├── instruction/
│   ├── philosophy/
│   ├── trigger/
│   ├── directive/
│   ├── blueprint/
│   ├── merge/
│   ├── off/
│
├── block_index.json         # Block listing for Bolt sidebar
├── vaults/                  # Saved block stacks (coming later)
├── vault_index.json         # Reference index of vaults
├── project_templates/       # Optional vault blueprints
├── sleeve_presets/          # Optional UI sleeves
```

> ✅ Ensure block_index.json exists (even if empty: `[]`).

---

## 📁 /docs/
```
/docs/
├── README.md (optional local)
├── schema_reference.md       # Canonical field + type definitions
├── UMG_BLOCK_TEMPLATE.md     # The JSON format to create each block
├── MERGE_ENGINE.md           # Explains how blocks merge + override
├── CITADEL_FLOW.md           # Explains stack assembly + execution
├── REPO_STRUCTURE.md         # Explains this whole layout
├── SESSION_CONTEXT.md        # Prompt structure and AI planning
├── VAULT_IMPORTS.md          # How to manage `.vault.json` files
├── UMG_SPEC.md               # Abstract spec for MOLT + logic layers
├── ORCHESTRATION_EXTENSION_GUIDE.md # How to use agent orchestration + MCP
├── COLOR_SYSTEM.md           # Full visual logic + color map of MOLT types
```

---

## 🎨 UMG BLOCK COLOR SYSTEM v2.0

| MOLT Type   | Color     | Hex Code | Symbolic Meaning                     |
|-------------|-----------|----------|--------------------------------------|
| Primary     | Blue      | #2563EB  | Foundation. Directive mission.       |
| Subject     | Green     | #10B981  | Domain anchor. Contextual seed.      |
| Instruction | Yellow    | #FACC15  | Logic, limits, operational steps     |
| Philosophy  | Orange    | #FB923C  | Tone, worldview, ethics layer        |
| Blueprint   | Pink      | #EC4899  | Style, layout, visual formatting     |
| Merge       | Slate     | #374151  | Structural reconciliation logic      |
| Trigger     | Red       | #EF4444  | Activator. Timing-based entry logic  |
| Directive   | Purple    | #8B5CF6  | Strategic overlay. Tactical lens     |
| Off         | LightGray | #D1D5DB  | Muted block. Archived logic          |
| Sleeve (bg) | Black     | #111827  | Container section background         |
| Sleeve Text | Yellow    | #FACC15  | UI visibility for container labels   |

### 📝 UI Application Guidelines
| Context           | Behavior                                      |
|------------------|-----------------------------------------------|
| Metadata/Docs     | Color is used in text or labels               |
| Block Sidebar     | Background color = block color, white text   |
| Block Editor View | Background = block color, inputs = white     |
| Sleeves           | Background = black, text = yellow             |
| Merged Blocks     | Shown via badge or border, not a unique color|

✅ Purpose: consistent and intuitive visual feedback for stacking, merging, and navigation.

---

# ✅ Operator Tasks – Block Genesis + Agent-Ready Extensions

## 1. Each block must include:
- `block_id`, `label`, `molt_type`, `category`
- `editable_fields`, `bolt_ready`, `ledger`
- `snap_config`, `runtime_behavior_flags`, `cantocore`, `cyentcore`

## 2. Optional: Advanced Fields for Agent Integration
```json
"code_modules": [
  {
    "slot": "langchain_function",
    "language": "python",
    "logic": "def run_tool(input): return call_external_tool(input)"
  }
],
"agent_orchestration": {
  "agent_type": "function_router",
  "dispatch_on": ["trigger", "directive"],
  "requires_context": true
},
"runtime_behavior_flags": {
  "is_active": true,
  "is_exportable": true,
  "requires_user_confirmation": false
}
```

## 3. block_index.json Example:
```json
[
  {
    "block_id": "launch_plan_core",
    "label": "Product Launch Plan",
    "category": "startup",
    "molt_type": "Primary"
  }
]
```

## 4. Reference Docs:
- `/docs/UMG_BLOCK_TEMPLATE.md`
- `/docs/ORCHESTRATION_EXTENSION_GUIDE.md`
- `/docs/schema_reference.md`
- `/docs/COLOR_SYSTEM.md`

Once these templates are followed, the system will support:
- Human-written prompts
- AI code orchestration
- LangChain function stacks
- Bolt drag-and-drop UI logic

🧱 The blocks now speak. You may begin, one at a time.
