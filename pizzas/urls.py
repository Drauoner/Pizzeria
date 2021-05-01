from django.urls import path


from . import views


app_name = "pizzas"


urlpatterns = [

    path("", views.homepage, name="homepage"),
    path("menu", views.menu, name="menu"),
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
    #path("new_comment/", views.new_comment, name="new_comment"),

    #path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    #path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]