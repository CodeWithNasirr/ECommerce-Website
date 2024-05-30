from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/",views.about, name="About Us"),
    path("contact/",views.contact,name="Contact Us"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("checkout",views.checkout,name="CheckOut")

]
