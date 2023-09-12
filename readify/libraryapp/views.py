from urllib import request
from django.shortcuts import redirect, render
from .models import AddBook,Book,Wishlist

# Create your views here.
def books_view(request):
    bookdata = AddBook.objects.all()
    return render(request,'books.html',{'bookdata': bookdata})
    
def add_cart(request, bookid2):
    userid=request.user.id
    book = Book(
        user_id=userid,
        book_id=bookid2        
    )
    book.save()
    return redirect('cart')
    
def cart(request):
    # Assuming you have the user object for the currently logged-in user
    user_id = request.user.id  # Replace with your user retrieval logic if needed
# Retrieve books in the user's cart
    books_in_cart = Book.objects.filter(user_id=user_id)
# Retrieve book details for the books in the cart
    book_details = AddBook.objects.filter(id__in=books_in_cart.values_list('book_id', flat=True))

    return render(request,"cart.html",{'books':book_details})

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

def delete_record(request, bye):
    remove=Wishlist.objects.filter(book_id=bye)
    print(remove)
    remove.delete()
    return redirect('wishlist')