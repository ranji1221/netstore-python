from django.shortcuts import redirect,render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
	#return HttpResponse('<html><title>To-Do lists</title></html>')
	#if request.method == 'POST':
	#	return HttpResponse(request.POST['item_text'])
	#return render(request,'home.html')
	'''
	return render(request,'home.html',{
		'new_item_text' : request.POST.get('item_text',''),
	})'''
	'''
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text = new_item_text)
	else:
		new_item_text = ''
	return render(request,'home.html',{
		'new_item_text' : new_item_text,
	})'''
	#再次优化代码
	'''
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
	return render(request,'home.html')'''
	#再再优化代码
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
	items = Item.objects.all()
	return render(request,'home.html',{'items' : items})