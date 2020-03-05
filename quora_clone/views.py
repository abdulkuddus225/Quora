from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.sessions.models import Session
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_welcome'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "index.html", context)
    else:
        return render(request, "index.html", context)



def user_logout(request):
    
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


def resgister(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request,"index.html")
    else:
        form=UserCreationForm()
        arg={'form':form}
        return render(request,"register.html",arg)


def welcome(request):
        context = {}
        context['user'] = request.user
        return render(request, "welcome.html", context)
        


def index(request):
    if request.method=="POST":
        form=request.POST
        created_by=request.user
        messages.success(request,"Question Added")
        Questions.objects.create(question=form['question'],created_by=created_by)
        return render(request,'welcome.html')
    else:
        all_questions=Questions.objects.all()
        return render(request,'questions.html',{'all_questions':all_questions})
    

@login_required
def details(request,id=None):
    if 'add_answer':
        if request.method=="POST":
            form=request.POST
            answer_id=Questions.objects.get(id=id)
            answers_by=request.user
            messages.success(request,"Answer Added")
            Answers.objects.create(answer_id=answer_id,answers=form['answer'],answers_by=answers_by)
            return HttpResponse("Answer Added")
        else:
            all_questions=Questions.objects.get(id=id)
            return render(request,'details.html',{'all_questions':all_questions})
    elif 'like_id':
        return HttpResponse("Liked")
        
   

def likes(request):
    post=get_object_or_404(Answers,id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())
