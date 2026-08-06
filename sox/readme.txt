SoX Wiki & Systems Hub
A centralized Django-based dashboard for internal audit and operational tracking. Features a wiki-style blog with markdown support and dynamic control dashboards (SOX and ITGC) powered by HTMX and interactive SVG workflows.

Tech Stack
• Backend: Django 4.x, Python 3.12.1
• Database: PostgreSQL
• Frontend: HTMX, JavaScript, CSS
• Visualization: Dynamic SVG workflows
• Containerization: Docker & Docker Compose
• Authentication: Django's default django.contrib.auth

Quick Start

Prerequisites
• Docker & Docker Compose installed

• Create environment file
Copy env_example to .env and update with your configuration:

cp env_example .env
Required variables:

• DATABASE_URL: PostgreSQL connection string
• SECRET_KEY: Django secret key (generate a new one for production)

Build and start containers

docker compose up
Access the application

Navigate to http://localhost:8000

Admin panel: http://localhost:8000/admin

Project Structure
sox/
├── about/              # About page app
├── blog/               # Wiki-style blog with markdown support
├── itgc/               # IT General Controls dashboard
├── sox_controls/       # SAP SOX Controls dashboard
├── mysite/             # Django project settings
│   ├── constants.py    # Template registry & configurations
│   ├── settings.py     # Django settings
│   └── urls.py         # URL routing
├── templates/          # HTML templates
├── static/             # CSS & JavaScript assets
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies

Modules
📝 Blog (/blog)
A wiki-style article platform with markdown support.

Status: Placeholder for future articles

Features:

Create and edit entries (currently public, will be restricted to author)

View published entries

Search functionality

Planned: Hide edit/propose features from unauthenticated users; transition to author-only writing space

🎛️ SOX Controls (/sox_controls)
Dynamic dashboard for SAP Business Process Controls.

Workflow:

Processes → displayed as tabs at the top

SubProcesses → nodes in an interactive SVG workflow

Controls → table filtered by process and subprocess selection

Features:

Click a process tab to load its workflow

Click a subprocess node to filter the control list

Multi-column filtering (Control ID, Process, Sub-Process, Risk, Description)

Bulk CSV upload for mass-importing controls

Responsive HTMX-powered filtering with real-time updates

Models:

BusinessProcess: Parent container for processes

SubProcess: Workflow nodes (ordered by sequence_order)

SoxControl: Individual audit controls linked to subprocesses

🔐 ITGC (/itgc)
IT General Controls dashboard using a similar architecture to SOX Controls.

Workflow:

Layers → displayed as tabs (Application, Database, Infrastructure, etc.)

Categories → nodes in an interactive SVG workflow

Controls → table filtered by layer and category selection

Features:

Filter by layer and category

Dynamic SVG category workflow with primary and secondary flows

Real-time control list filtering

Form-based search across categories, descriptions, and risk levels

Models:

ITGCLayer: Parent container for IT control layers

ITGCCategory: Workflow nodes (ordered by sequence_order)

ITGCControl: Individual IT controls linked to categories

ℹ️ About (/about)
Simple informational page about the organization or project.

Development Workflow
Template Registry System
All template paths and view mappings are managed in mysite/constants.py under the TEMPLATE_REGISTRY dictionary. This prevents hardcoded paths and keeps the codebase refactor-proof.

Best practices:

Adding a new template:

Create the template file in templates/

Add a new entry to TEMPLATE_REGISTRY in mysite/constants.py

Moving or renaming a template:

Update the file location

Update the corresponding entry in TEMPLATE_REGISTRY

Using templates in views:

from mysite.constants import TEMPLATE_REGISTRY as T

def my_view(request):
    return render(request, T["KEY_NAME"]["path"], context)
Verification Command
Before committing code changes, verify that all templates and URLs are properly registered:

docker compose exec app python manage.py verify_templates
This command validates:

All templates in the registry exist on the filesystem

All view names map correctly to URL configurations

No orphaned templates or missing entries

Database Migrations
When you modify any model:

Create migration:

docker compose exec app python manage.py makemigrations <app_name>
Apply migration:

docker compose exec app python manage.py migrate
Example:

docker compose exec app python manage.py makemigrations sox_controls
docker compose exec app python manage.py migrate
Key Features
HTMX-Powered Filtering
Real-time table filtering without page reloads

Dropdown, button, and input-based filtering

Debounced search (300ms delay on keyup)

Maintains filter state across interactions

Dynamic SVG Workflows
Interactive process/category nodes render as clickable SVG elements

Nodes automatically position based on sequence_order field

Primary and secondary node flows with visual distinction

Responsive viewBox scaling for mobile compatibility

CSV Bulk Upload
Mass-import controls via CSV file

Located in Django admin under sox_controls app

Supports batch updates and error reporting

Roadmap
Phase 1: Operational Core ✅
[x] Relational modeling (SoxControl ↔ BusinessProcess, etc.)

[x] SVG workflow mapping with clickable process nodes

[x] Bulk CSV upload utility

Phase 2: User Experience & Polish (In Progress)
[ ] Sync validation: Ensure SVG slugs match database entries

[ ] HTMX loading indicators for slow queries

[ ] Gated view logic for unauthenticated users

[ ] Blog edit feature lockdown (author-only access)

Phase 3: Automation & Scalability (Planned)
[ ] Dynamic SVG Generation: Convert static HTML SVG files to template-driven loops

Generate nodes and arrows from SubProcess and ITGCCategory models

Use sequence_order field as the single source of truth

[ ] Visual Consistency Engine: Slugification system to auto-sync database names with SVG IDs

[ ] Automated Backups: Weekly dumpdata to backup.json for version control

Troubleshooting
After adding a new SubProcess/ITGCCategory
Run the verification command to ensure slugs match:

docker compose exec app python manage.py verify_templates
Database connection issues
Check that DATABASE_URL in .env points to a running PostgreSQL instance and the credentials are correct.

HTMX filtering not working
Ensure HTMX JavaScript is loaded in base.html

Check browser console for errors

Verify that hx-get URLs match your URL configuration

Contributing
Create a feature branch

Make changes following the template registry pattern

Run migrations if models changed

Run verify_templates command before committing

Submit a pull request


---
Some useful things to note
If you change the model run you need to create the migration first:


docker compose exec app python manage.py makemigrations sox_controls

Then run migrate:

docker compose exec app python manage.py migrate