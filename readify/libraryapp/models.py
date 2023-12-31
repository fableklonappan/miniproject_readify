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
    
class AudioBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    narrator = models.CharField(max_length=100)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='audiobook_covers/')
    audio_file = models.FileField(upload_to='audiobooks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class BookCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    
class PdfBook(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    page_number = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='pdf_covers/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='book_pdfs/', blank=True, null=True)
    
    def __str__(self):
        return self.book_name