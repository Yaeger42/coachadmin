from django.urls import path
from restapi import views

urlpatterns = [
    path(
        route = '',
        view = views.get_all_coaches,
        name = 'get_all_coaches'
    ),
    path(
        route = '<int:id>/',
        view = views.get_one_coach,
        name = 'get_one_coach'
    ),
    
    path(
        route = 'create/',
        view = views.insert_coach,
        name = 'insert_coach'
    ),

    path(
        route = 'delete/<int:id>',
        view = views.delete_coach,
        name = 'delete_coach'
    ),

    path(
        route = 'update/',
        view = views.edit_coach,
        name = 'edit coach'
    )
]