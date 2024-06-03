from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import MessageForm


# Create your views here.
@login_required
def chat(request):
    chat_group = ChatGroup.objects.get(name='Myclass')
    chat_messages = chat_group.chat_messages.all().order_by('created')[:30]
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            return redirect('chat-app')

    return render(request, 'chat.html', {'chat_messages': chat_messages, 'user': request.user, 'form': form})
