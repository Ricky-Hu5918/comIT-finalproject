from django.shortcuts import render, resolve_url
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView

# Create your views here.

def run_code(code):
    try:
        code = 'print(' + code + ')'
        output = subprocess.check_output(
            ['python', '-c', code], universal_newlines=True, stderr=subprocess.STDOUT, timeout=30)
    except subprocess.CalledProcessError as e:
        output = 'Input Error!'

    return output


# @csrf_exempt
# @require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result': result})



