from django.shortcuts import render
from predict_client.prod_client import ProdClient

# Create your views here.

def test(request):
    client = ProdClient('localhost:9000', 'simple',2)
    req_data = [{'in_tensor_name': 'inputs', 'in_tensor_dtype': 'DT_INT32', 'data': 5}]
    value = client.predict(req_data)
    print(value)
    return render(request, 'tf_model_test/test.html',{'value':value})

