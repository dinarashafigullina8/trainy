from django.db import models


class Applicant(models.Model):
    man = 'М'
    women = 'Ж'
    sex_choices = [
        (man, 'Мужчина'),
        (women, 'Женщина')
    ]
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255,choices=sex_choices, default='M')
    birth = models.DateField()
    telephone = models.IntegerField(blank=True, default=0)
    health = models.CharField(max_length=255, blank=True, default='практически здоров', help_text='аллергоанамнез, хронические заболевания и т.д.')
    image = models.ImageField(default='-')

    def __str__(self):
        return self.concept
    
    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ('name',)

    


class Appeal(models.Model):
    work = 'В работе'
    done = 'Завершено'
    status_choices = [
        (work, 'В работе'),
        (done, 'Завершено')
    ]

    application = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='Appeal')
    emergency = models.ManyToManyField('name', related_name='Appeal')
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(db_index=True,editable=False, unique=True)
    status = models.CharField(max_length=255,choices=status_choices, default='В работе')
    number_of_victims = models.IntegerField(default=0)
    dont_call = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Appeal'
        verbose_name_plural = 'Appeals'
        ordering = ('date', 'number')

    def __str__(self):
        return self.concept


class Emergency(models.Model):
    police = 'Полиция'
    ambulance = 'Скорая'
    fire = 'Пожарная'
    name_choices = [
        (police, 'Полиция'),
        (ambulance, 'Скорая'),
        (fire, 'Пожарная')
    ]
    name = models.CharField(max_length=255, choices=name_choices)
    code = models.IntegerField()
    telephone = models.IntegerField() 

    class Meta:
        verbose_name = 'Emergency'
        verbose_name_plural = 'Emergencies'
        ordering = ('code',)

    def __str__(self):
        return self.concept
