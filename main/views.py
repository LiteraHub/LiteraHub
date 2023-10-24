from django.shortcuts import render

def show_main(request):
    context = {
    }

    return render(request, "landingpage.html", context)
