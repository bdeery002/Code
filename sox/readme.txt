📘 Sox - Wiki & Systems Hub
A centralized Django-based dashboard designed for internal audit and operational tracking. It features a wiki-style blog with markdown support and a dynamic SOX Control dashboard powered by HTMX and SVG workflows.


├── Dockerfile
├── backup.json
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_entryproposal.py
│   │   ├── 0003_entryproposal_send_rejection_email.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docker-compose.yml
├── env_example
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── main
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── readme.txt
├── requirements.txt
├── sox_controls
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_soxcontrol.py
│   │   ├── 0003_soxcontrol_sub_process.py
│   │   ├── 0004_businessprocess_remove_soxcontrol_process_name_and_more.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── components
└── templates
    ├── admin
    │   └── csv_upload.html
    ├── blog
    │   ├── _entry_list.html
    │   ├── edit_entry.html
    │   ├── entry.html
    │   ├── error.html
    │   ├── index.html
    │   ├── new_entry.html
    │   ├── proposal_submitted.html
    │   ├── propose_edit.html
    │   └── search_results.html
    ├── home.html
    ├── layout.html
    └── sox_controls
        ├── base_sox.html
        ├── index.html
        ├── partials
        │   ├── control_table_rows.html
        │   └── workflows
        │       ├── otc_workflow.html
        │       └── p2p_workflow.html
        └── sox_controls_detail.html
🚦 To-Do List (Roadmap)
Phase 1: Operational Core (COMPLETED)

[x] Relational Modeling: SoxControl connected to BusinessProcess via ForeignKeys.

[x] SVG Mapping: Clickable P2P/OTC workflows that trigger live table filtering.

[x] Bulk Upload: CSV utility for mass-importing audit controls.

Phase 2: User Experience & Polish (Current)

[ ] Sync Validation: Create a "Sync Check" view to ensure SVG slugs exist in the database.

[ ] UX Indicators: Add HTMX "Loading" indicators for slower database queries.

[ ] The "Gated" View: Finalize the logic that masks control details for unauthenticated users.

Phase 3: Automation & Scalability (The "Elite" Phase)

[ ] Dynamic SVG Generation: Move from static .html SVG files to a template-driven loop.

Logic: Loop through SubProcess models to draw nodes and arrows dynamically based on a sequence_order field.

[ ] Visual Consistency Engine: Implement a slugification system to ensure database subprocess names always match SVG interaction IDs.

[ ] Automated Backups: Schedule weekly dumpdata to backup.json to track the Neon DB state in Git.

Why this "To-Do" matters
By adding Dynamic SVG Generation to your roadmap, you are acknowledging the "Challenge of Consistency" we discussed. Instead of spending hours fixing typos between your SVG and your Database, you are planning to make the Database the "Single Source of Truth."

Would you like me to show you how to add a step_number field to your SoxControl model so you can begin sorting them for this future dynamic loop?