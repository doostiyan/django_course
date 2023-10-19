from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, template_name="hello.html",context={
        "user": "ehsan",
        "is_valid": False
    })