# Generated by Django 4.1.1 on 2022-09-13 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appeal',
            options={'ordering': ('date', 'number')},
        ),
        migrations.AlterModelOptions(
            name='applicant',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='emergency',
            options={'ordering': ('code',)},
        ),
        migrations.RenameField(
            model_name='appeal',
            old_name='telephone',
            new_name='number',
        ),
    ]