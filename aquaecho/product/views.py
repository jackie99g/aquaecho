from json import dumps

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import AcessLog


# Create your views here.
class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        method = request.method
        host = request.get_host()
        full_path_info = request.get_full_path_info()
        scheme = request.scheme
        content_type = request.content_type
        meta_data = self._gte_meta_data(request.META)
        access_log = AcessLog(
            method=method,
            host=host,
            full_path_info=full_path_info,
            scheme=scheme,
            content_type=content_type,
            meta_data=meta_data,
        )
        access_log.save()
        return render(request=request, template_name='product/default.html')

    def _gte_meta_data(self, meta_data: dict) -> str:
        classinfo = str | bool | int | float | list | tuple
        remove_keys = []
        for key in meta_data.keys():
            if not isinstance(meta_data[key], classinfo):
                remove_keys.append(key)
        for key in remove_keys:
            meta_data.pop(key)
        meta_data_json = dumps(meta_data)
        return meta_data_json
