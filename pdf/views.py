from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse  # Send the details in form of HTTP not web
from django.template import loader
import pdfkit
import io  # form to db and vice-versa. Needed for better performance


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


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)  # Get the object means one record with id
    # return render(request, "pdf/resume.html", {
    #     'user_profile': user_profile                # pass this to resume.html template
    # })
    template = loader.get_template("pdf/resume.html")  # load the template in the template
    html = template.render({'user_profile': user_profile})  # convert this to pdf, w.r.t id
    option = {  # option for creating pdf
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }

    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'  # This line missed in commit, but due to this line download
    # attachment is coming before seeing the pdf. Good idea to not expose my /id urls
    return response


def list(request):
    profile = Profile.objects.all()
    return render(request, "pdf/list.html", {'profile': profile})
