from django.contrib import admin
from .models import Entry, EntryProposal

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')


@admin.register(EntryProposal)
class EntryProposalAdmin(admin.ModelAdmin):
    list_display = ('proposed_title', 'entry', 'proposer_name', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('proposed_title', 'proposer_name')
    actions = ['approve_proposals']

    def approve_proposals(self, request, queryset):
        for proposal in queryset.filter(status='pending'):
            if proposal.entry:
                # Edit existing entry
                proposal.entry.title = proposal.proposed_title
                proposal.entry.content = proposal.proposed_content
                proposal.entry.save()
            else:
                # Create new entry
                Entry.objects.create(
                    title=proposal.proposed_title,
                    content=proposal.proposed_content
                )
            proposal.status = 'approved'
            proposal.save()
        self.message_user(request, f"{queryset.count()} proposal(s) approved.")
    
    approve_proposals.short_description = "Approve selected proposals"