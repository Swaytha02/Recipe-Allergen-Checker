# Generated by Django 5.0.7 on 2024-07-28 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='allergens',
            field=models.ManyToManyField(blank=True, to='checker.allergen'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='checker.ingredient'),
        ),
    ]