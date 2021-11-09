

from django.shortcuts import render
from .models import Profile

# Create your views here.
# Till now we have just created template but not storing any data from the template form.
# To store the data from form, we need to instruct
# Get the info from the User by if tag and paste in the db --> name = request.POST.get("name", ""). Also check label
# In Python, we create object to push the data into db


def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        degree = request.POST.get("degree", "")
        university = request.POST.get("university", "")
        skill = request.POST.get("skill", "")
        ambition = request.POST.get("ambition", "")
        work_ex = request.POST.get("work_exp", "")
        school = request.POST.get("school", "")

        profile = Profile(name=name, phone=phone, email=email, degree=degree, university=university, skill=skill,
                          ambition=ambition, work_ex=work_ex, school=school)
        profile.save()

    return render(request, "pdf/accept.html")
