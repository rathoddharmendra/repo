from django.shortcuts import render
#from django.http import HttpResponse



# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello Explorer! </h1>")
    class Treasure:
        def __init__(self, name, value, material, location):
            self.name = name
            self.value = value
            self.material = material
            self.location = location
    treasures = [
        Treasure('Gold Nugget', 1000.00, 'gold', "KGF, India"),
        Treasure('Fool\'s Gold', 0, 'pyrite', "California, US"),
        Treasure('Coffee Can', 20.00, 'tin', "London, Britain"),

    ]
    #return render(request, 'index.html', context)
    return render(request, 'index.html', {'treasures': treasures})
