from django.db import models     
from django.contrib.auth.models import User



class Player(models.Model):
    mmo_player = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mmo_player.username
    
class Category(models.Model):
    name = models.CharField(max_length=30,unique=True,)
    subscribers = models.ManyToManyField(User,related_name='categories')
    
    def __str__(self):
        return self.name.title()
    
    
    
class Post(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
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
    
    categoryType = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=None)
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.title[:]}: {self.text[:20]}'
    
class Response(models.Model):
    dateCreation = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    res_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_user')
    res_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reply')
    status = models.BooleanField(default=False)
    
class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    def __str__(self):
        return f'{self.user}'    
    
    




    

