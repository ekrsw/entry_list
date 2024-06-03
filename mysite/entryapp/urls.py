from django.urls import path
from .views import ListEntryView, DetailEntryView


urlpatterns = [
    # path('', views.hello_world, name='index'),
    path('entries/', ListEntryView.as_view(), name='entry_list'),
    path('entry/<int:pk>/detail/', DetailEntryView.as_view(), name='detail_entry'),
]