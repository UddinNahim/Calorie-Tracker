from django.shortcuts import render , redirect
from .models import Food ,Consume

# Create your views here.
def index(request):
    foods = Food.objects.all()  # always fetch foods

    if request.method == "POST":
        food_consumed_name = request.POST.get('food_consumed')  # safer
        if food_consumed_name:  # check if user selected a food
            food_obj = Food.objects.get(name=food_consumed_name)
            user = request.user
            consume = Consume(user=user, food_consumed=food_obj)
            consume.save()
        return redirect('index')  # redirect after POST

    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {
        "foods": foods,
        "consumed_food": consumed_food
    })

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('index')
    
    return render(request, 'myapp/delete.html', {'food': consumed_food})

def add_food(request):
    if request.method == "POST":
        name = request.POST.get('name')
        carbs = request.POST.get('carbs')
        protein = request.POST.get('protein')
        fats = request.POST.get('fats')
        calories = request.POST.get('calories')

        Food.objects.create(
            name=name,
            carbs=float(carbs),
            protein = float(protein),
            fats= float(fats),
            calories= int(calories)

        )
        return redirect('index')
    return render(request,'myapp/add_food.html')
    
