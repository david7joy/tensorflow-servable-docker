from predict_client.prod_client import ProdClient

# Used by Docker 1
client = ProdClient('localhost:9001', 'simple', 1)
req_data = [{'in_tensor_name': 'inputs', 'in_tensor_dtype': 'DT_INT32', 'data': 4}]
client.predict(req_data)

# Used by Docker 2
client = ProdClient('localhost:9000', 'simple_1', 2)
req_data = [{'in_tensor_name': 'inputs', 'in_tensor_dtype': 'DT_INT32', 'data': 4}]
client.predict(req_data)

# Used by Docker 3
client = ProdClient('localhost:9002', 'subtract_model', 1)
req_data = [{'in_tensor_name': 'inputs', 'in_tensor_dtype': 'DT_INT32', 'data': 22}]
client.predict(req_data)