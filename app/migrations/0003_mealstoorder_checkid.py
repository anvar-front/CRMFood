# Generated by Django 3.2 on 2021-05-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_check_waiterid'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealstoorder',
            name='checkid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkid', to='app.check'),
        ),
    ]
