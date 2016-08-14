import requests

def get_probbilty():
	apikey = "31b4901e-a1cb-4ffc-b6f8-74d14fb66e9d"
	model_name = "poolprobJSON"
	fields = {"fields":[{"name":"time","type":"STRING"},{"name":"holiday","type":"STRING"},{"name":"offer","type":"STRING"},{"name":"probability","type":"NUMERIC"},{"name":"area","type":"STRING"}]}
	data = {"dataset":[{"time":"12:30pm","area":"svnit surat","holiday":"yes","offer":"yes"}]}
	r = requests.post("https://api.havenondemand.com/1/api/sync/predict/v2", fields = fields ,json =data ,apikey = apikey ,model_name = model_name)
	print r.json
get_probbilty()