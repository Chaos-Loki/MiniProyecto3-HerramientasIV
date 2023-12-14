from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import cache_control
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from main.models import (
        UserProfile,
    )
from chat.models import(
    Conversation,
    UserMessage,
)
from chat.forms import MessageForm
from django.contrib import messages
from django.db.models import Q
User = UserProfile

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def redactChat(request, user_id):
    recipient =  User.objects.get(id=user_id)
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        
        if not room_name:
            messages.error(request, 'Introduce un nombre al asunto del chat')
        else:
            conversation = Conversation.objects.create(
                user1 = request.user.userprofile,
                user2 = recipient,
                room_name = room_name  
            ) 
            messages.success(request, 'Se creo el chat!')
            return redirect('chat:conversation-detail', pk=conversation.pk)

    return render(request, 'chat/redact_chat.html', {'recipient': recipient})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def inbox(request):
    conversations = Conversation.objects.filter(Q(user1=request.user.userprofile) | Q(user2=request.user.userprofile))  
    context = {'conversations': conversations}
    return render(request, 'chat/inbox.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def conversation_detail(request, pk):
    conversation = Conversation.objects.get(pk=pk)
    if not (conversation.user1 == request.user.userprofile or conversation.user2 == request.user.userprofile):
        # user not authorized for this conversation
        return redirect('chat:inbox')
    
    messages = conversation.messages.order_by('created_at') 
    context = {'conversation': conversation, 'messages': messages}
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid(): 
            message = form.save(commit=False)
            message.conversation = conversation
            message.from_user = request.user.userprofile
            message.save() 
            return redirect('chat:conversation-detail', pk=pk)
    else:
        form = MessageForm()
        
    context['form'] = form
        
    return render(request, 'chat/conversation-detail.html', context)