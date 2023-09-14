from urllib import request
from django.shortcuts import redirect, render
from .models import AddBook,BookCart,Wishlist,AudioBook

# Create your views here.
def books_view(request):
    bookdata = AddBook.objects.all()
    return render(request,'books.html',{'bookdata': bookdata})
    
def add_cart(request, bookid2):
    userid=request.user.id
    book = BookCart(
        user_id=userid,
        book_id=bookid2        
    )
    book.save()
    return redirect('cart')
    
def cart(request):
    # Assuming you have the user object for the currently logged-in user
    user_id = request.user.id  # Replace with your user retrieval logic if needed
# Retrieve books in the user's cart
    books_in_cart = BookCart.objects.filter(user_id=user_id)
# Retrieve book details for the books in the cart
    book_details = AddBook.objects.filter(id__in=books_in_cart.values_list('book_id', flat=True))

    return render(request,"cart.html",{'cart_books':book_details})

def delete_cart(request, cbye):
    remove=BookCart.objects.filter(book_id=cbye)
    remove.delete()
    return redirect('cart')

def add_wishlist(request, bookid3):
    userid=request.user.id
    book = Wishlist(
        user_id=userid,
        book_id=bookid3        
    )
    book.save()
    return redirect('books_view')

def wishlist(request):
    user_id = request.user.id
    books_in_cart = Wishlist.objects.filter(user_id=user_id)
    book_details = AddBook.objects.filter(id__in=books_in_cart.values_list('book_id', flat=True))

    return render(request,"wishlist.html",{'books':book_details})

def delete_wishlist(request, bye):
    remove=Wishlist.objects.filter(book_id=bye)
    remove.delete()
    return redirect('wishlist')

def audio_view(request):
    return render(request,'audiobooks.html')

def audio_view(request):
    audiobook = AudioBook.objects.all()
    return render(request,'audiobooks.html', {'audiobook':audiobook})