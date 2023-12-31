from django.shortcuts import render
from django.http import HttpResponse
from .models import TableInTarget
from .forms import UserForm


def TableInTarget_list(request):
    TableInTargets = TableInTarget.objects.all()
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main/table_inQCS.html', {'TableInTargets': TableInTargets, 'form': form})

def index(request):
    return render(request, 'main/indexQCS.html')

def user_info2(request):
    return render(request, 'main/user_infoQCS.html')

def team_info(request):
    return render(request, 'main/teamQCS.html')

def contact_info(request):
    return render(request, 'main/contactQCS.html')

# def table_in(request):
#     return render(request, 'main/table_inQCS.html')

def table_out(request):
    return render(request, 'main/table_outQCS.html')

# def user_info(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     return render(request, 'main/user_infoQCS.html', {'user': user})


def custom_404(request, exception):
    return HttpResponse(f'Ой-ёй-ёй! Какая жалость!:{exception}')