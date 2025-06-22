# 🧠 UMG Block Schema Reference (Bolt-Compatible)

This document defines the canonical structure for all UMG Citadel blocks, as used in the Bolt hackathon web app.

---

## 🔷 REQUIRED FIELDS

| Field                  | Type       | Description |
|------------------------|------------|-------------|
| `block_id`             | string     | Unique ID for the block (e.g. `product_launch_plan`) |
| `label`                | string     | Human-readable name |
| `category`             | string     | Folder and logic grouping (`business/plan`) |
| `description`          | string     | What this block does |
| `molt_type`            | string     | One of: `Primary`, `Subject`, `Instruction`, `Blueprint`, `Philosophy`, `Trigger`, `Merge`, `Off` |
| `editable_fields`      | object     | User-editable zones: `content`, `style`, `behavior` |
| `bolt_ready`           | boolean    | Always `true` for Bolt-supported blocks |
| `snap_config`          | object     | Defines how block connects to others (see below) |
| `runtime_behavior_flags` | object  | Controls block behavior in logic flow |
| `canto_overlay`        | object     | Fit, category, and usage hints |
| `ledger`               | object     | Author, verifier, timestamps, and edit history |

---

## 🔁 `snap_config` Format

```json
"snap_config": {
  "snap_zone": "bottom | left | right",
  "mergeable_with": ["block_id_1", "block_id_2"],
  "priority": 1
}
```

- `snap_zone`: Controls where block connects in logic graph
- `mergeable_with`: Optional list of valid merge targets
- `priority`: Integer for rendering/merge order (higher = stronger)

---

## ⚙️ `runtime_behavior_flags`

```json
"runtime_behavior_flags": {
  "is_active": true,
  "is_primary_directive": false,
  "philosophy_constraint_applied": false
}
```

- Use to control visibility, execution, ethical filters

---

## 🧠 `canto_overlay`

```json
"canto_overlay": {
  "category_code": "BP | PHIL | INST | SUB",
  "snap_to": ["Primary", "Instruction"],
  "fit_score": 0.9,
  "status": "template",
  "origin_session": "citadel_forge"
}
```

- Used by Bolt and agents to suggest, auto-connect, or rate-fit blocks

---

## 🔒 `ledger`

```json
"ledger": {
  "originator": "Christopher L Haynes",
  "verified_by": "PoeUMG",
  "created_at": "AUTO",
  "edit_log": []
}
```

Tracks authorship and block validation.

---

## 🧱 Valid `molt_type` Values

| MOLT Type     | Purpose |
|---------------|---------|
| `Primary`     | Top-level directive |
| `Subject`     | Topical or domain scope |
| `Instruction` | Logical or operational rule |
| `Blueprint`   | Visual/style formatting |
| `Philosophy`  | Ethical tone or worldview |
| `Trigger`     | Execution condition |
| `Merge`       | Secondary detail/data block |
| `Off`         | Disabled/draft block |

---

## ⚙️ Example Minimal Block

```json
{
  "block_id": "cta_email",
  "label": "Email Call to Action",
  "category": "marketing/funnels",
  "description": "Final CTA for the launch sequence.",
  "molt_type": "Instruction",
  "editable_fields": {
    "content": "",
    "style": "",
    "behavior": ""
  },
  "bolt_ready": true,
  "export_target": ["bolt"],
  "snap_config": {
    "snap_zone": "bottom",
    "mergeable_with": [],
    "priority": 1
  },
  "runtime_behavior_flags": {
    "is_active": true
  },
  "canto_overlay": {
    "category_code": "INST",
    "snap_to": ["Primary"],
    "fit_score": 0.87
  },
  "ledger": {
    "originator": "Christopher L Haynes",
    "verified_by": "PoeUMG",
    "created_at": "AUTO",
    "edit_log": []
  }
}
```

---

## ✅ Final Notes

- All blocks must be lowercase filenames using `_` (not camelCase)
- Block files go in `/data/blocks/[category]/`
- This schema will power Bolt’s UI rendering, snapping, and orchestration

Citadel Approved 🧱📘️🧱
