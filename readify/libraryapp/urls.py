
from django.urls import path,include    
from django.conf import settings 
from django.conf.urls.static import static
from libraryapp import views
urlpatterns = [
     path('books_view/', views.books_view, name='books_view'),
     path('add_cart/<int:bookid2>/', views.add_cart, name='add_cart'),
     path('cart',views.cart,name="cart"),
     path('delete_cart/<int:cbye>/', views.delete_cart, name='delete_cart'),
     path('add_wishlist/<int:bookid3>/', views.add_wishlist, name='add_wishlist'),
     path('wishlist',views.wishlist,name="wishlist"),
     path('delete_wishlist/<int:bye>/', views.delete_wishlist, name='delete_wishlist'),
     path('audio_view/', views.audio_view, name='audio_view'),
     path('pdf_view/', views.pdf_view, name='pdf_view'),
]