from django.shortcuts import render

def home(request):

	import request
	import json

	# token: pk_d91740a399c34554bda6f3ba376d9202
	api_request = request.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_d91740a399c34554bda6f3ba376d9202")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "error..."

	return render(request, 'home.html', {})


def about(request):
	return render(request, 'about.html', {})