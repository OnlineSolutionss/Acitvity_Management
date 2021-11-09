from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin

from django.views import View
from .models import History

class HistoryList(ListView):
    def get_queryset(self):
        user_history = History.objects.filter(user=self.request.user)
        return user_history

class MyHistroy(View):
    def get(self, request):
        return render(request, 'histroy.html')

    def post(self, request):
        print('Post Method is calling okk')
        return render(request, 'histroy.html')


class HistoryDelete(SingleObjectMixin, View):
    model = History
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
        return redirect('history')
