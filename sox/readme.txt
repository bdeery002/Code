Sox - Wiki Blog
A Django-based wiki-style blog where content is managed through the Django admin and users can propose new entries or edits for review.

Stack

Backend: Django 6
Database: PostgreSQL 17 (Neon — hosted cloud Postgres)
Containerisation: Docker + Docker Compose
Markdown rendering: markdown2
Environment: GitHub Codespaces


Project Structure
sox/
├── blog/               # Main app
│   ├── models.py       # Entry and EntryProposal models
│   ├── views.py        # All views
│   ├── admin.py        # Admin config with approve/reject logic
│   ├── urls.py         # URL routes
│   └── templates/
│       └── blog/
│           ├── layout.html
│           ├── index.html
│           ├── entry.html
│           ├── propose_edit.html
│           └── proposal_submitted.html
├── mysite/             # Django project config
│   ├── settings.py
│   └── urls.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env                # Not committed to git — see below

Database — Neon
This project uses Neon as its hosted Postgres database. Data persists in Neon's cloud independently of the local environment or Codespace.

Postgres version: 17
Region: AWS US East 1 (N. Virginia)
Connection: via DATABASE_URL in .env

To view or query data directly, use the Neon console at console.neon.tech.

Environment Variables — .env
The .env file is not committed to git (it is in .gitignore). If your Codespace is deleted or you move to a new machine, you will need to recreate it manually.
Create a .env file in the project root with the following:
envSECRET_KEY=your-django-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://neondb_owner:your-password@your-neon-host/neondb?sslmode=require&channel_binding=require
To generate a new Django secret key:
bashpython -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
Your Neon connection string can be found in the Neon console under Connect → Connection string.

Important: Never commit .env to git. Your DATABASE_URL contains your Neon password.


Docker Commands
Start the app
bashdocker compose up
Start in background (detached)
bashdocker compose up -d
Start and rebuild the image (use after code or requirements changes)
bashdocker compose up --build
Stop the app
bashdocker compose down
View logs
bashdocker compose logs app
docker compose logs app --tail 30    # last 30 lines only
Run Django management commands
bashdocker compose exec app python manage.py migrate
docker compose exec app python manage.py makemigrations
docker compose exec app python manage.py createsuperuser
docker compose exec app python manage.py shell

Accessing the Site (Codespaces)
Since this runs in GitHub Codespaces, localhost won't work directly.

Open the Ports tab in VS Code (bottom panel)
Find port 8081
Set visibility to Public
Click the globe icon to open in browser

The Django admin is available at /admin on the same URL.

Content Workflow
Publishing content (admin only)

Go to /admin
Log in with your superuser credentials
Under Entries, create or edit entries directly using markdown

User proposals

Visitors can propose new entries or edits via the Propose New Entry link
Proposals appear in the admin under Entry Proposals
To publish a proposal: open it, change status to Approved, and click Save
To reject: change status to Rejected, optionally tick Send rejection email, and click Save


Backup
Since .env is not in git, back up these two things regularly:
1. Recreate .env from Neon console
Keep a secure note of your Neon connection string and Django secret key outside of the Codespace (e.g. a password manager).
2. Export data as a fixture
bashdocker compose exec app python manage.py dumpdata blog > backup.json
Commit backup.json to git. To restore:
bashdocker compose exec app python manage.py loaddata backup.json

Requirements
django
psycopg2
dj-database-url
markdown2
Install locally (if needed outside Docker):
bashpip install -r requirements.txt