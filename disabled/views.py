from django.shortcuts import render,redirect,get_object_or_404
from .models import Detail,Disabled
from user import models as usermodel

# Create your views here



# def create_detail(request,disabled_id):
#     if request.method == 'POST':
#         detail = Detail(volunteer=request.user)
#         detail_form = Detail_Form(request.POST, instance = detail)
#         #current_user = get_object_or_404(usermodel.User,pk=request.user.id)
#         #disabled = get_object_or_404(Disabled,pk = disabled_id)
#         if detail_form.is_valid():
#             #detail_form.volunteer = current_user
#             detail_form.save()
#             #disabled.details.add(Detail,pk=detail_form.id)
#             #connect_detail_disable(disabled_id,detail_form.id)
#             return redirect('#')
#     else: 
#         detail_form = Detail_Form()
#     return render(request,'create_detail.html',{'detail_form':detail_form})

def create_detail(request,disabled_id):
    my_disabled = get_object_or_404(Disabled,pk = disabled_id)
    current_user = get_object_or_404(usermodel.User,pk = request.user.id)
    if request.method == 'POST':
        new_detail = Detail(
            about = request.POST['about'],
            volunteer_name = request.POST['volunteer_name'],
            disabled = my_disabled,
        )
        new_detail.save()
        return redirect('home')
    else:
        return render(request,'disabled_detail.html',{'disabled':my_disabled})
    # pass

    

def create_disabled(request):
    if request.method == 'POST':
        new_disabled = Disabled(
            name=request.POST['name'],
            gender=request.POST['gender'], 
            age=request.POST['age'], 
            handicap_type=request.POST['handicap_type'], 
        )
        new_disabled.save()
        return render(request, '#')
    else:
        return render(request, 'disabled.html')

