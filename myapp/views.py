from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import student  # Ensure the model name matches

def index(request):
    students = student.objects.all()
    search_query = request.POST.get('query')

    if search_query:
        students = student.objects.filter(Name__icontains=search_query)

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            student.objects.create(
                Name=name,
                Email=email,
            )
            messages.success(request, "Student added successfully")
            return redirect('index')  # Redirect to avoid resubmission
        
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            update_student = student.objects.get(id=id)
            update_student.Name = name
            update_student.Email = email
            update_student.save()

            messages.success(request, "Student updated successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            delete_student = student.objects.get(id=id)
            delete_student.delete()
            messages.success(request, "Student deleted successfully")


    context = {
        "students": students
    }

    return render(request, 'index.html', context)

def search(request):
    if 'search' in request.GET:
        search=request.GET['search']
        if 'search':
            student=student.objects.order_by(id).filter(Name__icontains=search)
            context={
                'student':student
            }
            return render(request, 'index.html', context)

            
