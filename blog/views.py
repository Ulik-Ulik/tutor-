from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    name = "Tom"

    music = [
        {'artist': 'Korn', 'album': 'Follow The Leade', 'year': 1998},
        {'artist': 'System of a Down', 'album': 'Toxicity', 'year': 2001},
        {'artist': 'Кино', 'album': 'Ночь', 'year': 1986}
    ]

    context = {
        'name': name,
        'music': music,
    }
    return render(request, template, context)


def john(request):
    template = 'blog/index.html'
    name = "John"

    music = [
        {'artist': 'Korn', 'album': 'Follow The Leade', 'year': 1998},
        {'artist': 'System of a Down', 'album': 'Toxicity', 'year': 2001},
        {'artist': 'Кино', 'album': 'Ночь', 'year': 1986},
        {'artist': 'Korn', 'album': 'Follow The Leade', 'year': 1998},
        {'artist': 'System of a Down', 'album': 'Toxicity', 'year': 2001},
        {'artist': 'Кино', 'album': 'Ночь', 'year': 1986}
    ]

    context = {
        'name': name,
        'music': music,
    }
    return render(request, template, context)
