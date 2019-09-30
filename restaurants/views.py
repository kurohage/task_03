from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list": [
    {
    "restaurant_name": "Le Notre",
    "food_type": "French"
    },
    {
    "restaurant_name": "La Piazza",
    "food_type": "Italian"
    },
    {
    "restaurant_name": "Johnny Rockets",
    "food_type": "American"
    },
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {
    "restaurant_name": "Le Notre",
    "food_type": "French"
    }
    }
    return render(request, 'detail.html', context)
