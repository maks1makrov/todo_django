from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from todo_app.models import Todo
from todo_app.utils import get_todo_for_user, find_next_display_priority_for_user


class TodoView(View):
    def get(self, request, priority=None):
        data = get_todo_for_user(request.user.id, priority)
        return render(request, 'index.html', {'data': data})

    def post(self, request):
        display_priority = find_next_display_priority_for_user()
        user = request.user if request.user.is_authenticated else None
        Todo.objects.create(text=request.POST.get('text'),
                            priority=request.POST.get('priority'),
                            display_priority=display_priority,
                            date_create=datetime.now(),
                            user=user)
        return redirect('read_todo')


class TodoDelete(View):
    def post(self, request, id):
        Todo.objects.get(id=id).delete()
        return redirect("read_todo")