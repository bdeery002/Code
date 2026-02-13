from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = [
    "This is the first section.",
    "This is the second section.",
    "This is the third section."
]

def section(request, num):
    if not (1 <= num <= 3):
        raise Http404("No such section")

    # Detect history restore (or direct visit / refresh / non-HTMX request)
    is_history_restore = request.headers.get('HX-History-Restore-Request') == 'true'
    is_htmx_request    = request.headers.get('HX-Request') == 'true'

    if is_history_restore or not is_htmx_request:
        # Return FULL page (with the correct section pre-loaded)
        context = {
            'section_num': num,           # pass to template if needed
            'section_text': texts[num-1],
        }
        return render(request, "singlepage/index.html", context)

    # Normal HTMX click → return fragment only
    return HttpResponse(texts[num - 1])
