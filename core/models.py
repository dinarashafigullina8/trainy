from email.policy import default
from django.db import models


class Applicant(models.Model):
    man = 'М'
    women = 'Ж'
    sex_choices = [
        (man, 'Мужчина'),
        (women, 'Женщина')
    ]
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1,choices=sex_choices, default='M')
    birth = models.DateField()
    telephone = models.IntegerField(blank=True, default=0)
    health = models.CharField(max_length=100, blank=True, default='практически здоров', help_text='аллергоанамнез, хронические заболевания и т.д.')
    image = models.ImageField(default='-')

    def __str__(self):
        return self.concept
    
    class Meta:
        ordering = ('name',)

    


class Appeal(models.Model):
    work = 'В работе'
    done = 'Завершено'
    status_choices = [
        (work, 'В работе'),
        (done, 'Завершено')
    ]

    application = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='application')
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(db_index=True,editable=False, unique=True)
    status = models.CharField(max_length=30,choices=status_choices, default='В работе')
    number_of_victims = models.IntegerField(default=0)
    dont_call = models.CharField(max_length=20,default='-')

    class Meta:
        ordering = ('date', 'number')

    def __str__(self):
        return self.concept


class Emergency(models.Model):
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE, related_name='appeal')
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    telephone = models.IntegerField() 

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.concept
