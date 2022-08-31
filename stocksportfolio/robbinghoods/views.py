from django.shortcuts import render, redirect
from .models import Stock
from django.contrib	import messages
from .forms import StockForm


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
		return render(request, 'home.html', {'ticker': 'Enter a Ticker symbol above in the search field'})


def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added!"))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		return render(request, 'add_stock.html', {'ticker': ticker})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ('Stock has been deleted'))
	return redirect(add_stock)




















