from django.db import models
from django.contrib.auth.models import User

##
# Pages for MegWorld site
##
class Section(models.Model):
    title       = models.CharField(max_length=200)
    body        = models.TextField()
    author      = models.ForeignKey(User)
    posted      = models.DateTimeField('Publish date', blank=True, null=True)
    modified    = models.DateTimeField('Modified date', blank=True, null=True)

    def __unicode__(self):
        return self.title

class Page(models.Model):
    title       = models.CharField(max_length=200)
    sections    = models.ManyToManyField(Section)

    def __unicode__(self):
        return self.title

##
# news items
##
class NewsItem(models.Model):
    title        = models.CharField(max_length=200)
    body        = models.TextField()
    posted        = models.DateTimeField('Posted date')
    
    def __unicode(self):
        return self.title

##
# IRC Specific stuff
##
class User(models.Model):
    nickname    = models.CharField(max_length=75)
    realname    = models.CharField(max_length=75)
    ident       = models.CharField(max_length=75)

##
# Server status page
##
class ServerStatus(models.Model):
    name        = models.CharField(max_length=255, unique=True, null=True)
    address     = models.CharField(max_length=255, unique=True, null=True)
    ssl         = models.BooleanField(default=False)
    ipv6        = models.BooleanField(default=False)
    online      = models.BooleanField(default=False)
    location    = models.CharField(max_length=255, blank=True)
    modified    = models.DateTimeField('last checked', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Server Statuses"

    def __unicode__(self):
        if self.name is None:
            return self.address.split(".")[0].capitalize()
        return self.name.capitalize()


##
# Ticket tracker system
##
class Comment(models.Model):
    poster      = models.ForeignKey(User)
    body        = models.TextField()
    date        = models.DateTimeField('Post date')

    def __unicode__(self):
        return body[:30]

class Status(models.Model):
    name        = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Statuses"

class Ticket(models.Model):
    subject        = models.CharField(max_length=200)
    body        = models.TextField()
    status        = models.ForeignKey(Status, null=True, blank=True)
    reporter     = models.ForeignKey(User, related_name="reporter", blank=True, null=True)
    posted        = models.DateTimeField('Post date', blank=True)
    assigned    = models.ForeignKey(User, related_name="assigned", blank=True, null=True)
    comments     = models.ManyToManyField(Comment, blank=True)

    def __unicode__(self):
        return unicode("%s (%s)" % (self.subject[:30], self.status.name))
