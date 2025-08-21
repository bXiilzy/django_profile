from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')

def for_view(request):
    context = {}
    context['message'] = "การวนซ้ำใน_Django"
    
    if request.method == 'POST' and request.POST.get('count') != '':
        number = int(request.POST.get('count'))
        context['count'] = list(range(1,number +1))
    else:
        context['count'] = list(range(1, 2))
        
    return render(request, 'for.html',context)

def multipli(request):
    context = {}
    context['message'] = "ตารางสูตรคูณ"
    
    if request.method == 'POST' and request.POST.get('number') != '':
        number = int(request.POST.get('number'))
        context['number'] = number
        context['table'] = [(i, number * i) for i in range(1, 13)]
    else:
        context['table'] = []
        context['number'] = None
        
    return render(request, 'table.html', context)