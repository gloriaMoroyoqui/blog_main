from django.db import models

# Create your models here.
class Category(models.mODE1):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title')
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.title
    
class Post(models.Mode1):

    ACTIVE ='active'
    DRAFT = 'draft'

    CHOICES_STATUS ={
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
        }
    
    category = models.Foreigkey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    intro = models.textField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, defauldt=ACTIVE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 