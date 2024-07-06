from django.shortcuts import render
from django.http import HttpResponseRedirect
from search_user.models import Information

CREATE_USER_PATH = 'search_user/create_user.html'
SERCH_USER_PATH = 'search_user/index.html'
SEARCH_RESULT_PATH = 'search_user/search_result.html'
USER_INFORMATION_PATH = 'search_user/user_information.html'
FILLED_FORM_ERROR = 'Заполните все поля в форме'

def index(request):
    if request.method == 'GET':
        return render(request, SERCH_USER_PATH)
    
    if request.method == 'POST':
        result_search = result_search_db(request)
        return render(request, SEARCH_RESULT_PATH, context={'result': result_search})

def user_info(request, id):
    if request.method == 'GET':
        info_user = Information.objects.get(id=id)
        return render(request, USER_INFORMATION_PATH, context={'info_user': info_user, 'auth': request.user.is_authenticated})

def create_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                return render(request, CREATE_USER_PATH)

            if request.method == 'POST':
                for i in request.POST: # Проверка заполнения полей в форме.
                    if request.POST[i]:
                        continue
                    else:
                        return render(request, CREATE_USER_PATH, context={'error': FILLED_FORM_ERROR}) 

                user_information = Information.objects.create(fio=request.POST['fio'], country=request.POST['country'], address=request.POST['address'], telephone=request.POST['telephone'], description=request.POST['description'])
            
    return HttpResponseRedirect('/')

def delete_user(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                Information.objects.get(id=id).delete()
                
    return HttpResponseRedirect('/')
            
def result_search_db(request):
    result_search = Information.objects
    for i in request.POST:
        if i == 'fio':
            result_search = result_search.filter(fio__icontains=request.POST[i])
        if i == 'country':
            result_search = result_search.filter(country__icontains=request.POST[i])
        if i == 'address':
            result_search = result_search.filter(address__icontains=request.POST[i])
        if i == 'telephone':
            result_search = result_search.filter(telephone__icontains=request.POST[i])
        if i == 'description':
            result_search = result_search.filter(description__icontains=request.POST[i])

    return result_search