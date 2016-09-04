from django.shortcuts import redirect, render
from lists.models import Item
# from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)  # .objects.create is a neat shorthand for creating a new Item, without needing to call .save()
        return redirect('/')
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})  # , {
    # 'new_item_text': new_item_text
    # })
