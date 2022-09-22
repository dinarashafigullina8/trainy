from django.db import models


class Applicant(models.Model):
    man = 'М'
    women = 'Ж'
    gender_choices = [
        (man, 'Мужчина'),
        (women, 'Женщина')
    ]
    name = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.CharField(max_length=255,choices=gender_choices, default='M', verbose_name='Пол')
    birth = models.DateField(verbose_name='Дата рождения')
    telephone = models.IntegerField(blank=True, default=0, verbose_name='Номер телефона')
    health = models.CharField(max_length=255, blank=True,default='практически здоров',
                             help_text='аллергоанамнез, хронические заболевания и т.д.',
                             verbose_name='Состояние здоровья')
    image = models.ImageField(default='-', verbose_name='Фото')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('name',)


class Emergency(models.Model):
    police = 'Полиция'
    ambulance = 'Скорая'
    fire = 'Пожарная'
    name_choices = [
        (police, 'Полиция'),
        (ambulance, 'Скорая'),
        (fire, 'Пожарная')
    ]
    name = models.CharField(max_length=255, choices=name_choices, verbose_name='Название')
    code = models.CharField(max_length=255, verbose_name='Код')
    telephone = models.IntegerField(verbose_name='Номер телефона') 
    
    def __str__(self):
        return self.name 


    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ('code',)

      


class Appeal(models.Model):
    work = 'В работе'
    done = 'Завершено'
    status_choices = [
        (work, 'В работе'),
        (done, 'Завершено')
    ]

    application = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='Appeal', verbose_name='Обращение')
    emergency = models.ManyToManyField(Emergency, related_name='Appeal', verbose_name='Экстренная служба')
    date = models.DateField(auto_now_add=True, verbose_name='Дата обращения')
    number = models.IntegerField(db_index=True,editable=False, unique=True, verbose_name='Номер обращения')
    status = models.CharField(max_length=255,choices=status_choices, default='В работе', verbose_name='Статус')
    number_of_victims = models.IntegerField(default=0, verbose_name='Количество обращений')
    dont_call = models.BooleanField(default=False, verbose_name='Не звонить?')

    def __str__(self):
        return self.status

    
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('date', 'number')





