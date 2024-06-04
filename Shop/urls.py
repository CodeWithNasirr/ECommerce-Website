from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("shopall/",views.shop,name="ShopAll"),
    path('productview/<int:myid>',views.product_view, name='ProductItems'),
    path("about/",views.about, name="About Us"),
    path("contact/",views.contact,name="Contact Us"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("checkout",views.checkout,name="CheckOut")

]
