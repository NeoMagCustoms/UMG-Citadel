
import pandas as pd

# Define cleanup task list
cleanup_tasks = [
    {"task_id": "CLEAN-001", "issue": "Duplicate block file", "path": "umg_blocks/5_operations/process_systems/automation_scripts_macros.json"},
    {"task_id": "CLEAN-002", "issue": "Duplicate (marked duplicate)", "path": "umg_blocks/5_operations/process_systems/automation_scripts_macros_duplicate.json"},
    {"task_id": "CLEAN-003", "issue": "Placeholder content: 'Loading...'", "path": "umg_blocks/9_analytics/9B_event_tracking/placeholder.md"},
    {"task_id": "CLEAN-004", "issue": "Legacy aggregate block file", "path": "incoming_master/category_29_search_query_blocks.json"},
    {"task_id": "CLEAN-005", "issue": "Legacy aggregate block file", "path": "scripts/incoming_master/category_7_legal_docs.json"},
    {"task_id": "CLEAN-006", "issue": "Orphaned plan file, possible dupe", "path": "business/1_plans/startup_plan.json"},
    {"task_id": "CLEAN-007", "issue": "Stray file name spacing", "path": "ui/hover_tooltips_and_info icons.json"},
    {"task_id": "CLEAN-008", "issue": "Stray file name spacing", "path": "handoff_to human_escalation_logic.json"},
    {"task_id": "CLEAN-009", "issue": "Missing Messaging category", "path": "category_28_messaging_comms_blocks.json"},
    {"task_id": "CLEAN-010", "issue": "Empty folder (.gitkeep only)", "path": "business/9_projects/.gitkeep"},
]

# Create DataFrame
df = pd.DataFrame(cleanup_tasks)

# Export to CSV
df.to_csv("cleanup_tasks.csv", index=False)
print("✅ Cleanup task list saved as cleanup_tasks.csv")
