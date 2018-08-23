from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'tf_model_test/test.html')
