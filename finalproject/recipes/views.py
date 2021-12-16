from django.shortcuts import render, redirect
import random
from django.http import HttpResponse
from .models import Recipe, SavedRecipes
from .forms import RecipeForm
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import RecipeSerializer
# Create your views here.

def home(request):
    savedRecipes = SavedRecipes.objects.all()
    personalRecipes = []
    for i in savedRecipes:
        if int(i.item_user) == request.user.id:
            try:
                personalRecipes.append(Recipe.objects.get(id=i.item_recipeid))
            except Recipe.DoesNotExist:
                print("failed")

    rec = Recipe.objects.order_by('?')[:3]

    context = {
        'personalRecipes': personalRecipes,
        'reccommended': rec
    }
    return render(request, 'recipes/home.html', context)

def browse(request):
    recipe_list = Recipe.objects.all()
    recipe = request.GET.get('name')
    if recipe != '' and recipe is not None:
        recipe_list = Recipe.objects.filter(item_name__contains=request.GET.get('name',''))
    paginator = Paginator(recipe_list, 5)
    page = request.GET.get('page')
    recipe_list = paginator.get_page(page)
    context = {
        'recipe_list': recipe_list
    }
    return render(request, 'recipes/browse.html', context)

def recipedetail(request, item_id):
    item = Recipe.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'recipes/recipedetail.html', context)

def createRecipe(request):
    form = RecipeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('recipes:browse')
    return render(request, 'recipes/recipeform.html', {'form':form})

def recipeedit(request, id):
    item = Recipe.objects.get(id=id)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('recipes:browse')

    return render(request, 'recipes/recipeform.html', {'form': form,'item':item})

def recipedelete(request, id):
    item = Recipe.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('recipes:browse')

    return render(request, 'recipes/recipe-delete.html',{'item':item})

def recipesave(request, id):
    recipe_item = Recipe.objects.get(id=id)
    print("recipeid: ", recipe_item.id, " userid: ", request.user.id)
    rec = SavedRecipes(item_recipeid=recipe_item.id,item_user=request.user.id)
    rec.save()
    return redirect('recipes:browse')


def profile(request):
    context = {}
    return render(request, 'recipes/profile.html', context)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all();
    serializer_class = RecipeSerializer

class ChineseViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(item_category="Chinese")
    serializer_class = RecipeSerializer

class IndianViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(item_category="Indian")
    serializer_class = RecipeSerializer

class MexicanViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(item_category="Mexican")
    serializer_class = RecipeSerializer

class AmericanViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(item_category="American")
    serializer_class = RecipeSerializer

