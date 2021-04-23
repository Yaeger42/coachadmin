from django.urls import path 

from coach import views

urlpatterns = [
    path(
        route = 'new',
        view = views.CreateCoachView.as_view(),
        name = 'create'
    ),

    path(
        route = 'feed',
        view = views.CoachFeedView.as_view(),
        name = 'feed'
    ),

    path(
        route = 'edit/<pk>',
        view = views.EditCoachView.as_view(),
        name = 'edit'
    ),
    path(
        route = '<pk>/delete/',
        view = views.CoachDeleteView.as_view(),
        name = 'delete'
    )
]