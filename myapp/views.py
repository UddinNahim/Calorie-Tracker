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
