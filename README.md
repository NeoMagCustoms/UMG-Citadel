# 🧱 UMG Citadel – Minimal Canon Vault

This vault contains the **foundational modular blocks** required to build a full logic stack in a Bolt-powered UMG web app.

## 📦 Included Blocks

| Block ID              | Type         | Description                                  |
|-----------------------|--------------|----------------------------------------------|
| `product_launch_plan` | Primary      | Root intent: Plan a product launch strategy  |
| `swot_analysis`       | Subject      | Analyze Strengths, Weaknesses, Opportunities |
| `gtm_strategy`        | Instruction  | Channels, audience, and tactics              |
| `blueprint_branding`  | Blueprint    | Controls tone, visuals, and format           |
| `regen_ethics`        | Philosophy   | Ethical framing for AI and content outputs   |

---

## 🐄 Snap Behavior

- All blocks support top-down stacking and horizontal snap logic
- Blocks are `bolt_ready` and structured for modular orchestration

---

## 📁 File Structure

All blocks live in:
- **Block folders**: `/data/blocks/{primary|subject|instruction|philosophy|trigger|directive|blueprint|merge|off}/`
- **Index file**: `/data/block_index.json`
- **Schema reference**: [docs/schema_reference.md](docs/schema_reference.md)

```
/data/blocks/[category]/
```

This vault definition lives in:

```
/data/vaults/vault_index.json
```

---

## 🧠 Usage

Use this stack to prototype any modular AI or startup strategy system in Bolt, with full support for merge, edit, and export behavior.

---

Modular Intelligence Begins Here. 🧱
