from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.conf import settings
from models import Demo
import json


@cache_page(settings.CACHING_POLICIES.get('persistent'))
def demos(request):
    results = []
    demos = Demo.objects.all()
    for demo in demos:
        results.append(demo.to_dict())
    return HttpResponse(content=json.dumps({'demos': results}),
                        content_type="application/json")


@cache_page(settings.CACHING_POLICIES.get('persistent'))
def demo(request, slug):
    "Dispatch to JSON or HTML response"
    if not Demo.objects.filter(slug=slug).exists():
        return HttpResponseNotFound()

    accept = request.META.get('ACCEPT', "text/html")

    if accept.startswith("application/json") or accept.startswith("text/json"):
        return demo_as_json(request, slug)
    elif accept.startswith("text/html"):
        return demo_as_html(request, slug)
    else:
        # Return a "501 Not Implemented"
        return HttpResponse(status=501)


def demo_as_json(request, slug):
    # This query should have been catched.
    return HttpResponse(
        content=json.dumps(Demo.objects.get(slug=slug).to_dict()),
        content_type="application/json",
        status_code=200)


def demo_as_html(request, slug):
    template = "demos/{0}.html".format(slug)
    return render(request, template, {})
