# Generated by Django 5.0.1 on 2024-01-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorpass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('contraseña', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='PasswordEntry',
        ),
    ]
