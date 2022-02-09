
from django.db import router
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('stream',views.SteamPlatformVS,basename="streaml")
urlpatterns=[
# path('Steamlist',views.SteamPlatformAV.as_view(),name='Stramelist'),
# path('Steamlist/<int:pk>',views.SteamPlatformDetailsAV.as_view(),name='Streamdetails'),
path('',include(router.urls)),
path('list',views.WatchlistAv.as_view(),name="movielist")
,path('list/<int:pk>',views.WatchDeatilsAv.as_view(),name="moviedetails"),
path("stream/review",views.ReviewList.as_view(),name="revlist"),
path("stream/<int:pk>/review-create",views.ReviewCreate.as_view(),name="revcreate"),
path("stream/review/<int:pk>",views.ReviewDetails.as_view(),name="revdetails"),



]