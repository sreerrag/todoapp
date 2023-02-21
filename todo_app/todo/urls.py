from django.urls import path
from.views import TaskList,TaskCreate,TaskUpdate,TaskDelete,TaskDetailView
from . import views

urlpatterns=[
    path('task-list',TaskList.as_view(),name = 'task'),
    path('task-create',TaskCreate.as_view(),name = 'task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name = 'task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name = 'task-delete'),
    path('task-detail/<int:pk>', TaskDetailView.as_view(), name = 'task-detail'),
    # path('user-login/',CustomLoginView.as_view(),name = 'user-login')
    path("login/", views.CustomLogin.as_view(),name = 'login'),
    path("register/",views.signup,name = 'register'),
    # path('',views.Home,name = 'home')

]
