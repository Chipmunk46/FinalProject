from django.urls import path
from recipes import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name="home"),
    path('browse/', views.browse, name="browse"),
    path('recipedetail/<int:item_id>', views.recipedetail, name="recipedetail"),
    path('createrecipe/', views.createRecipe, name="createrecipe"),
    path('edit/<int:id>', views.recipeedit, name="editrecipe"),
    path('delete/<int:id>', views.recipedelete, name="deleterecipe"),
    path('save/<int:id>', views.recipesave, name="saverecipe"),
    #path('deletesave/<int:id>', views.deletesave, name="deletesave")
]

urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)