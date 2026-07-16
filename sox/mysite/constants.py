# mysite/constants.py

# A centralized registry for all templates in the system.
# Format: "CONSTANT_NAME": {"path": "...", "view": "...", "url": "..."}

# mysite/constants.py

TEMPLATE_REGISTRY = {
    # ADMIN
    "ADMIN_CSV": {"path": "admin/csv_upload.html", "view": "admin.csv_upload", "url": "/admin/csv-upload/", "models": "None", "role": "page"},

    # BLOG
    "BLOG_INDEX":     {"path": "blog/index.html", "view": "blog.index", "url": "/blog/", "models": "Entry", "role": "page"},
    "BLOG_ENTRY":     {"path": "blog/entry.html", "view": "blog.entry_detail", "url": "/blog/<slug>/", "models": "Entry", "role": "page"},
    "BLOG_EDIT":      {"path": "blog/edit_entry.html", "view": "blog.edit_entry", "url": "/blog/<slug>/edit/", "models": "Entry", "role": "page"},
    "BLOG_NEW":       {"path": "blog/new_entry.html", "view": "blog.new_entry", "url": "/blog/new/", "models": "Entry", "role": "page"},
    "BLOG_LIST":      {"path": "blog/_entry_list.html", "view": "blog.index (partial)", "url": "N/A (partial)", "models": "Entry", "role": "partial"},
    "BLOG_ERROR":     {"path": "blog/error.html", "view": "blog.error_view", "url": "/blog/error/", "models": "None", "role": "page"},
    "BLOG_PROPOSE":   {"path": "blog/propose_edit.html", "view": "blog.propose_edit", "url": "/blog/<slug>/propose/", "models": "Entry, EntryProposal", "role": "page"},
    "BLOG_SUBMITTED": {"path": "blog/proposal_submitted.html", "view": "blog.proposal_success", "url": "/blog/proposal/done/", "models": "None", "role": "page"},
    "BLOG_SEARCH":    {"path": "blog/search_results.html", "view": "blog.search", "url": "/blog/search/", "models": "Entry", "role": "partial"},

    # PORTFOLIO (New)
    "PORTFOLIO_ABOUT": {"path": "portfolio/about.html", "view": "portfolio.about", "url": "/about/", "models": "None", "role": "page"},

    # SOX CONTROLS
    "SOX_INDEX":      {"path": "sox_controls/index.html", "view": "sox.index", "url": "/controls/list/", "models": "SoxControl, BusinessProcess", "role": "page", "htmx_target": "body"},
    "SOX_ROWS":       {"path": "sox_controls/partials/control_table_rows.html", "view": "sox.hx_rows", "url": "/controls/hx/rows/", "models": "SoxControl", "role": "partial", "htmx_target": "#control-table-body"},
    "SOX_WORKFLOW":   {"path": "sox_controls/partials/workflows/workflow.html", "view": "sox.workflow", "url": "/controls/workflow/", "models": "BusinessProcess, SubProcess", "role": "partial", "htmx_target": "#workflow-container"},
    "SOX_WORKFLOW_NOT_FOUND": {"path": "sox_controls/partials/workflows/not_found.html", "view": "sox.load_workflow (partial)", "url": "N/A", "models": "None", "role": "partial", "htmx_target": "#workflow-container"},
}