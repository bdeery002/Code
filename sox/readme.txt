📘 Sox - Wiki & Systems Hub
A centralized Django-based dashboard designed for internal audit and operational tracking. It features a wiki-style blog with markdown support and a dynamic SOX Control dashboard powered by HTMX and SVG workflows.

.
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
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── constants.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── readme.txt
├── requirements.txt
├── sox_controls
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       ├── __init__.py
│   │       └── verify_templates.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_soxcontrol_control_id.py
│   │   ├── 0003_businessprocess_code.py
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
    ├── aboutme.html
    ├── admin
    │   └── csv_upload.html
    ├── base.html
    ├── blog
    │   ├── _entry_list.html
    │   ├── _sidebar.html
    │   ├── edit_entry.html
    │   ├── entry.html
    │   ├── error.html
    │   ├── index.html
    │   ├── new_entry.html
    │   ├── proposal_submitted.html
    │   ├── propose_edit.html
    │   └── search_results.html
    ├── home.html
    └── sox_controls
        ├── index.html
        └── partials
            ├── control_table_rows.html
            └── workflows
                ├── not_found.html
                └── workflow.html

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


🛠 Development & Maintenance Workflow
To keep the dashboard stable and refactor-proof, we maintain a strict Template Registry system.

1. Template Registry (mysite/constants.py)
All template paths, associated view names, and URL mappings are managed in mysite/constants.py under the TEMPLATE_REGISTRY dictionary.

Whenever you:

Add a new template: Create the file in the templates/ folder and add a new entry to TEMPLATE_REGISTRY.

Move or Rename a template: Update the path value in TEMPLATE_REGISTRY to match the new location.

Update a View: Import the registry in your views.py and use the registry keys rather than hardcoding string paths.

2. Verification Procedure
We use a custom management command to validate the registry against your actual file system and URL configuration.Always run this before committing code
python manage.py verify_templates

3. Best Practice for Views
When rendering templates in your views, prefer:
from mysite.constants import TEMPLATE_REGISTRY as T
# ...
return render(request, T["KEY_NAME"]["path"], context)

---
🚀 Next Development Cycle: Portfolio App
Objective: Formalize self-promotion and move static pages to a dedicated, scalable app.

Steps:
1. Create the App:
   python manage.py startapp portfolio

2. Configuration:
   - Add 'portfolio' to INSTALLED_APPS in mysite/settings.py.
   - Create portfolio/urls.py and map the 'about' view.
   - Include 'portfolio.urls' in the root mysite/urls.py.

3. Template Setup:
   - Move templates/aboutme.html to templates/portfolio/about.html.
   - Update the file to extend 'base.html' and use the 'content' block.

4. Registry Update:
   - Register the new template in mysite/constants.py under 'PORTFOLIO_ABOUT'.

5. Validation:
   - Run 'python manage.py verify_templates' to ensure the new app is correctly mapped.
---