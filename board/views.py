from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Item
from django.urls import reverse_lazy
# Create your views here.

class ItemLV(ListView):
    # model = Item
    # template_name = "board/Item_list.html"
    # context_object_name = "items"
    # # paginated_by = 1

    # def get_queryset(self):
    #     return Item.objects.all()

    model = Item
    # ListView는 기본 세팅
    # - template : 앱이름/모델명(소문자)_list.html
    # - context : object_list
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tiger'
        return context
    
class ItemCV(CreateView):
    model = Item
    success_url = reverse_lazy('index')
    fields = ['title', 'content','price']  

class ItemDV(DetailView):
    model = Item