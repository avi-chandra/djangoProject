# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.db import connections
from django.db.models import Count
from . forms import RegistrationForm
import datetime

from . models import Question, Person_details, States, Cities
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    return render(request,'polls/index.html',{'latest_questions':latest_questions})

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request,'polls/detail.html',{'question':question,'error_message':'please select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def viewData(request):
    pdata = Person_details.objects.all()
    return render(request,'polls/show.html',{'pdata':pdata})

class SignUpView(CreateView):
    template_name = 'polls/signup.html'
    form_class = UserCreationForm

def ValidateUser(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exist'
    #user = User.objects.all()
    #return HttpResponse(user)
    return JsonResponse(data)

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        icard = request.POST.get('icard')
        age = request.POST.get('age')
        education = request.POST.get('edu')
        statename = request.POST.get('states')
        city = request.POST.get('city')
        cityname = Cities.objects.get(pk=city)
        current_date = datetime.datetime.now()

        details = Person_details(fullName=fname, idcardNum=icard, age=age, education=education, city=cityname,state=statename,added_date=current_date)
        details.save()
        return HttpResponseRedirect('/polls/thanks/')
    else :
        stateList = States.objects.all()
        return render(request,'polls/publicdata.html',{'statelist':stateList})

def ValidateId(request):
    idcard = request.GET.get('icard', None)
    statename = request.GET.get('states')
    elementId = request.GET.get('eid')
    if elementId == "id_icard":
        data = {
            'is_taken': Person_details.objects.filter(idcardNum__iexact=idcard).exists()
        }
    else:
        stateid = States.objects.get(state=statename)
        data = Cities.objects.all().filter(state_id=stateid)
        citylist = serializers.serialize('json',data)

    if 'is_taken' in data:
        data['error_message'] = 'A user with this Idcard already exist'
        return JsonResponse(data)
    else:
        return HttpResponse(citylist, content_type="application/json")

def thanks(request):
    return render(request,'polls/thankyou.html')

def play_count_by_month(request):
    data = Person_details.objects.values('age').annotate(dcount=Count('state'))
    return JsonResponse(list(data), safe=False)