from django.urls import path
from .views import ListEntryView, DetailEntryView, CreateEntryView, UserView

app_name = 'entryapp'
urlpatterns = [
    # path('', views.hello_world, name='index'),
    path('entries/', ListEntryView.as_view(), name='entry_list'),
    path('entry/<int:pk>/detail/', DetailEntryView.as_view(), name='detail_entry'),
    path('entry/create/', CreateEntryView.as_view(), name='create_entry'),
    path('user/<int:user>/entries/', UserView.as_view(), name='user_list'),
]
