Sox - Wiki & Systems Hub
A centralized Django-based dashboard. It features a wiki-style blog with markdown support and an upcoming system for tracking flight/operational controls via CSV imports.

🏗 Project Structure
Your structure is now centralized for easier maintenance:

Plaintext
sox/
├── blog/                # Wiki Logic (Models, Views, Forms)
├── main/                # Core App (Home page, Global logic)
├── mysite/              # Project Configuration (Settings, Root URLs)
├── static/              # Global Assets (CSS, JS, Components)
├── templates/           # Global Frontend (Layout, Home, App Overrides)
│   ├── blog/            # Blog-specific templates & fragments
│   ├── layout.html      # The Master Baseplate
│   └── home.html        # The Central Hub
└── manage.py
🛠 Tech Stack
Backend: Django 6.0.2

Database: PostgreSQL 17 (Hosted via Neon)

Frontend: Django Templates (ready for JS/React components)

Environment: Docker + GitHub Codespaces

🚦 To-Do List (Roadmap)
Phase 1: The controls App (Current Priority)
[ ] App Setup: Run python manage.py startapp controls.

[ ] Data Modeling: Define a Control model to store CSV data (e.g., ID, Status, Description, Last Checked).

[ ] CSV Logic: Create a view and utility function to parse uploaded .csv files using Python’s csv module or pandas.

[ ] Dashboard Integration: Create a templates/controls/_control_list.html fragment and include it in home.html.

Phase 2: User Experience & Interactivity
[ ] HTMX Integration: Add HTMX to layout.html to allow the "Random Page" button to refresh content without a full page reload.

[ ] Search Improvements: Enhance the search view to support partial matches and highlighted results.

[ ] Markdown Editor: Implement a "Preview" mode for the proposal form so users can see their Markdown before submitting.

Phase 3: Systems & Monitoring
[ ] API Endpoints: Begin building JSON views in views.py to prepare for future JS/React components in static/js/components/.

[ ] Automated Backups: Script a weekly dumpdata to backup.json to ensure the Neon DB state is tracked in Git.

💾 Database & Backups
This project uses Neon cloud Postgres. Data persists independently of your Codespace.

To Backup Data:

Bash
docker compose exec app python manage.py dumpdata blog > backup.json
To Restore Data:

Bash
docker compose exec app python manage.py loaddata backup.json
🚀 Quick Start
Recreate .env: Ensure SECRET_KEY and DATABASE_URL (from Neon) are set.

Launch: docker compose up --build

Ports: Ensure port 8081 is set to Public in the Codespaces Ports tab.

Run this before closing your session:
`docker compose exec app python manage.py dumpdata blog > backup.json`