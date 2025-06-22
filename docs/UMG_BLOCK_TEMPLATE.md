# UMG Block Template

This document outlines the canonical JSON schema for a single **UMG block**. All blocks must adhere to this structure before being added to the Citadel.

## Schema

```json
{
  "id": "unique-block-id",
  "type": "business | website | chatbot",
  "molt": "Primary | Subject | Instruction | Philosophy | Trigger | Merged",
  "title": "Human‑readable name",
  "description": "Short summary of the block’s purpose",
  "fields": {},
  "logic": {},
  "snap": {},
  "merge": {},
  "inject": {}
}
```

*See `docs/UMG_SPEC.md` for a full property reference.*

## Usage

1. Copy the schema above into a new `.json` file.
2. Populate the required fields and any optional sections.
3. Place the file in `/public/umg_blocks/<type>/` where `<type>` matches the `type` property.
4. Add an entry for the new block to `/data/block_index.json` so it can be discovered by the builder.
