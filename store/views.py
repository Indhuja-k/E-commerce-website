from django.http import HttpResponse

def homepage(request):
    return HttpResponse("✅ Welcome to Swiftora Store Homepage!")
