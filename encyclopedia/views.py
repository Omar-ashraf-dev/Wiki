from django.shortcuts import render, redirect
from . import util
import markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_to_HTML(title):
    entry = util.get_entry(title)
    html = markdown.markdown(entry) if entry else None

    return html


def entry(request, title):
    entryPage = util.get_entry(title)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingEntry.html", {
            "entryTitle": title
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": convert_to_HTML(title),
            "entryTitle": title
        })


def deletePage(request):
    input_title = request.POST['title']
    util.delete_entry(input_title)
    return redirect("/")


def search(request):
    if request.method == 'POST':
        input = request.POST['q']
        print(input)
        entries = util.list_entries()
        print(entries)
        search_pages = []

        for entry in entries:
            if input.upper() in entry.upper():
                search_pages.append(entry)

        print(search_pages)
        for entry in entries:
            print("Comparing " + input.upper() + " with " + entry.upper())
            if input.upper() == entry.upper():
                return render(request, "encyclopedia/entry.html", {
                    "entry": convert_to_HTML(input),
                    "entryTitle": entry
                })
        if search_pages != []:
            return render(request, "encyclopedia/search.html", {
                "entries": search_pages
            })
        else:
            return render(request, "encyclopedia/nonExistingEntry.html", {
                "entryTitle": input
            })


def newPage(request):
    return render(request, "encyclopedia/newPage.html")


def save(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        input_text = request.POST['text']
        entries = util.list_entries()
        html = convert_to_HTML(input_title)
        Already_exist_true = "false"
        for entry in entries:
            if input_title.upper() == entry.upper():
                Already_exist_true = "true"

        if Already_exist_true == "true":
            return render(request, "encyclopedia/newPage.html", {
                "already_exist": True,
                "entryTitle": input_title
            })

        else:

            util.save_entry(input_title, input_text)
            return render(request, "encyclopedia/entry.html", {
                "entry": convert_to_HTML(input_title),
                "entryTitle": input_title
            })


def randomPage(request):
    entries = util.list_entries()
    randEntry = random.choice(entries)
    html = convert_to_HTML(randEntry)
    return render(request, "encyclopedia/entry.html", {
        "entry": html,
        "entryTitle": randEntry
    })


def editPage(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        text = util.get_entry(input_title)
        return render(request, "encyclopedia/editPage.html", {
            "entry": text,
            "entryTitle": input_title
        })


def saveEdit(request):
    if request.method == 'POST':
        entryTitle = request.POST['title']
        entry = request.POST['text']
        util.save_entry(entryTitle, entry)
        html = convert_to_HTML(entryTitle)
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": entryTitle
        })
