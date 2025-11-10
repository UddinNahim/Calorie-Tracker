from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Consume

def index(request):
    foods = Food.objects.all()  # everyone can see available foods

    if request.method == "POST":
        if request.user.is_authenticated:  # only logged-in users can add consumption
            food_consumed_name = request.POST.get('food_consumed')
            if food_consumed_name:
                food_obj = Food.objects.get(name=food_consumed_name)
                Consume.objects.create(user=request.user, food_consumed=food_obj)
        return redirect('index')  # redirect after POST

    # Only show consumed foods if the user is logged in
    consumed_food = Consume.objects.filter(user=request.user) if request.user.is_authenticated else []

    return render(request, 'myapp/index.html', {
        "foods": foods,
        "consumed_food": consumed_food
    })

@login_required
def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('index')
    return render(request, 'myapp/delete.html', {'food': consumed_food})

@login_required
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
            protein=float(protein),
            fats=float(fats),
            calories=int(calories)
        )
        return redirect('index')
    return render(request, 'myapp/add_food.html')
