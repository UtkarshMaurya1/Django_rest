from django.http import HttpResponse

def home_page(request):
    print("homepage requested")
    return HttpResponse("<h1>this is homepage</h1>")

