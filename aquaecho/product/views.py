from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request=request, template_name='product/default.html')
