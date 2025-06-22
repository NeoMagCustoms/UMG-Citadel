# Vault Imports

The Citadel can import entire project **vaults** to bootstrap complex builds.

## Vault File Structure

A vault is a single JSON file with the extension `.vault.json` and contains:

| Key            | Description                              |
|----------------|------------------------------------------|
| `meta`         | Title, author, version, and description. |
| `blocks`       | Array of fully‑formed UMG blocks.        |
| `sleeves`      | Optional sleeve presets.                 |
| `exportConfig` | Default export settings.                 |

## Import Process

1. Validate the vault against `docs/UMG_SPEC.md`.
2. De‑duplicate block IDs against the current repository.
3. Copy new blocks into `/public/umg_blocks/<type>/`.
4. Update `/data/block_index.json` with the new entries.
5. Register sleeves in `/data/sleeve_presets/` (if present).

An example vault can be found at `data/project_templates/example.vault.json`.
