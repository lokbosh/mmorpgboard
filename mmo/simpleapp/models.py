from ckeditor.fields import RichTextField
from django.db import models     
from django.contrib.auth.models import User
from django.urls import reverse

    
    
    
class Post(models.Model):
    tanks = 'TK'
    heals = 'HL'
    damage_dealers = 'DD'
    vendors = 'VD'
    guildmasters = 'GM'
    quest_giver = 'QG'
    smiths = 'SM'
    skinners = 'SK'
    potion_masters = 'PM'
    enchanters = 'EH'
    
    CATEGORY_CHOICES = (
        (tanks,'Танки'),(heals,'Хилы'),(damage_dealers,'Дамагеры'),(vendors,'Торговцы'),(guildmasters,'Гильдмастера'),
        (quest_giver,'Квестгиверы'),(smiths,'Кузнецы'),(skinners,'Кожевники'),(potion_masters,'Зельевары'),(enchanters,'Мастера заклинаний')
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = RichTextField()
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=tanks)
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    
    
    
    def __str__(self):
        return f'{self.title[:]}:'
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
class Response(models.Model):
    
    STATUS = (
        ('undefined', 'Неопределенный'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=128,)
    status = models.CharField(max_length=10, choices=STATUS, default='undefined')

    

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.post_id})
    
    




    

