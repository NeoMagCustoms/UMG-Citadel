# Canonical UMG Folder Structure (Citadel Bolt‑Aligned)

This structure is optimized for clarity, Bolt compatibility, and ease of block deployment.

```
/data/blocks/                          # Master logic block library (all .json logic blocks)
├── business/
│   ├── 1_plans/                      # Primary business plan types (e.g. SaaS, Startup)
│   ├── subtypes/                     # Pitch decks, bank‑ready variants, one‑pagers
│   ├── 11_embedded_reports/          # SWOT, TAM/SAM/SOM, Exit, etc.
│   ├── blueprint/                    # Style / formatting blocks (pink)
│   ├── 2_financials/
│   │   ├── core_statements/          # Profit & Loss, Balance Sheet, Cash Flow
│   │   └── forecasts_analysis/       # Forecasts, pricing, CAC, LTV
│   ├── 3_tax_compliance/
│   ├── 4_investor_docs/
│   ├── 5_operations/
│   ├── 6_marketing/
│   ├── 7_legal/
│   ├── 8_hr/
│   ├── 9_projects/
│   └── 10_training/
└── trigger/                          # Global triggers (e.g. on_submit)

/data/project_templates/              # Reusable vault skeletons, plan layouts, canvases
/data/sleeve_presets/                 # Custom sleeve layouts (purple wrappers)
/data/vaults/                         # Full JSON stacks for export / import

/docs/                                # Canonical documentation & specs
├── CITADEL_FLOW.md
├── FEATURES.md
├── MERGE_ENGINE.md
├── REPO_STRUCTURE.md
├── SESSION_CONTEXT.md
├── UMG_BLOCK_TEMPLATE.md
├── UMG_SPEC.md
├── VAULT_IMPORTS.md
└── schema_reference.md

/public/                              # Display assets only (icons, SVGs)
├── icons/
└── .gitkeep

/src/                                 # App logic, helpers, orchestration
├── ai/               # Agent logic, future GPT config
│   └── poeAssistant.js
└── utils/
    └── mergeEngine.js
```

> **Guideline:** All block logic lives in `/data/blocks/`, all assets in `/public/`, and engine logic in `/src/`. Follow this tree to keep UMG modular, scalable, and Bolt‑smooth.
