from django.shortcuts import render, HttpResponse, redirect
from .models import User, Queue

def index(request):
    context = {
        'all_users' : User.objects.all(),
    }
    print('*'*100)
    print('in the index page')
    return render(request, 'queue_app/index.html', context)

def queue_list(request):
    queue_list = Queue()
    context = {
        'queued_users' : queue_list.s1,
    }
    print('*'*100)
    print('users are being queued here')
    print(context['queued_users'])#Shows that user objects are not being queued
    return render(request, 'queue_app/queue_list.html', context)

def create_user(request):
    print('*'*100)
    print('creating new user')
    new_user = User.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        age = request.POST['age']
    )
    print(new_user)
    return redirect('/')

def nq_user(request, user_id):
    print('*'*100)
    print('enqueueing user...')
    nqing_user = User.objects.get(id = user_id)
    Queue().enqueue(nqing_user)
    print(nqing_user)
    return redirect('/queue_list')

def dq_user(request, user_id):
    print('*'*100)
    print('dequeueing user...')
    dqing_user = User.objects.get(id = user_id)
    dq = Queue()
    dq.dequeue(dqing_user)
    print(dqing_user)
    return redirect('/queue_list')



