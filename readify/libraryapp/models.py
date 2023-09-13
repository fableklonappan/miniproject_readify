from django.db import models
from userapp.models import CustomUser
# Create your models here.
class AddBook(models.Model):
    picture = models.ImageField(upload_to='books')
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    summary = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    
    
class BookCart(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(AddBook,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        # return self.book.title
        return f"cart details {self.user.email}: {self.book.title}"
    
class Wishlist(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(AddBook,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.book.title
    