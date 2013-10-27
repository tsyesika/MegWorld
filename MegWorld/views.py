from django.shortcuts import render
from django.http import Http404

from datetime import datetime

from MegWorld.models import ServerStatus, Page, NewsItem

def servers(response):
    servers     = ServerStatus.objects.all()
    page        = Page.objects.get(title="Servers")
    sections    = page.sections.all()

    oldest = datetime.now()
    try:
        oldest = servers[0].modified
    except:
        pass

    context = {
        "page":page,
        "servers":ServerStatus.objects.all(),
        "sections":sections,
        "modified":oldest.strftime("%d %b %Y, %I:%M %p %Z"),
    }

    return render(response, "servers.html", context)

def home(response):
    # this has specific news stuff
    page = Page.objects.get(title="Home")
    
    sections = page.sections.all()
    news = NewsItem.objects.order_by('posted').reverse()[:5]

    formatted_news = []
    for item in news:
        formatted_news.append(
            (item.title, item.posted.strftime("%d %b %Y, %I:%M %p %Z"), item.body)
        )

    context = {
        "page":page,
        "sections":sections,
        "news":formatted_news,
    }

    return render(response, "index.html", context)

def default(response, name="Home", edit=""):
    
    try:
        page = Page.objects.get(title=name)
    except:
        raise Http404

    sections = page.sections.all()

    context = {
        "page":page,
        "sections":sections,
        "edit":edit,
    }

    return render(response, "page.html", context)
