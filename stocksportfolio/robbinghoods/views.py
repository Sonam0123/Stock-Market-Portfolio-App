from django.shortcuts import render

def home(request):

	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_d91740a399c34554bda6f3ba376d9202")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "error..."
		return render(request, 'home.html', {'api': api})
	else :
		return render(request, 'home.html', {'ticker': 'Enter a Ticker symbol above'})


def about(request):
	return render(request, 'about.html', {})