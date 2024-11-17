from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
   
    user_type=models.CharField(max_length=100,null=True)
   
    
    
    def __str__(self):   
        
        return f"{self.username}"
    
#addcash
class AddCash(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.source} - {self.amount}"


#expensemodel
class ExpenseModel(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.description}"

