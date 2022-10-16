from django.shortcuts import render
from .forms import UploadForm
from .models import Upload
from django.http import JsonResponse
from django.shortcuts import HttpResponse
import json
from django.core import serializers



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
    form = UploadForm(request.POST or None, request.FILES or None)

    if is_ajax(request=request):
        pic_id = json.loads(request.POST.get('id'))
        action = request.POST.get('action')


        if pic_id is None:
            if form.is_valid():
                obj = form.save(commit=False)
        else:
            obj = Upload.objects.get(id=pic_id)

        obj.action = action 
        obj.save()
        
        data = serializers.serialize('json', [obj])

        return JsonResponse({'data':data})

            
    context = {
        'form': form,
    }

    return render(request,'opencv_site/main.html',context)
