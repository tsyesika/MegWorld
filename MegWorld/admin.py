from datetime import datetime

from django.contrib import admin
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django import forms

from MegWorld.models import ServerStatus, Page, Section, Status, Ticket, NewsItem


admin.site.unregister(Site)

##
# Website Pages and sections
##
class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ('posted', 'modified')

    def save_model(self, request, obj, form, change):
        obj.posted = datetime.now()
        obj.modified = datetime.now()

admin.site.register(Page)
admin.site.register(Section)

##
# News
##
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted')
    
    fieldsets = (
        (None, {
            'fields':('title', 'body'),
        }),
    )

    max_num = 0

    def save_model(self, request, obj, form, change):
        if not obj.posted:
            obj.posted = datetime.now()
        obj.save()

admin.site.register(NewsItem, NewsAdmin)

##
# server status
##
class ServerStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'location', 'ssl', 'ipv6', 'online', 'modified')
    readonly_fields = ('modified',)

    def save_model(self, request, obj, form, change):
        obj.modified = datetime.now()
        if not obj.ipv6:
            obj.ipv6 = False
        obj.save()

admin.site.register(ServerStatus, ServerStatusAdmin)

##
# Ticket Tracker
##

class TicketAdmin(admin.ModelAdmin):

    list_display = ('subject', 'status', 'assigned', 'posted')
    search_fields = ('subject', 'body', 'assigned', 'posted')

    fieldsets = (
        (None, {
            'fields':('subject', 'body', 'status'),
        }),
        ('Advanced', {
            'classes':('collapse',),
            'fields':('reporter', 'posted', 'assigned'),
        }),

    )

    max_num = 0 #remove the 'add another' link

    def save_model(self, request, obj, form, change):
        if not obj.reporter:
            obj.reporter = request.user
        if not obj.posted:
            obj.posted = datetime.now() 
        if not obj.assigned:
            obj.assigned = request.user # should be changed later
        if not obj.status:
            status = Status.objects.get(name='open')
            obj.status = status # open and closed can't be removed.
        obj.save()


# registerryyy
#admin.site.register(Ticket, TicketAdmin)
#admin.site.register(Status)
