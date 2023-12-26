# Generated by Django 4.2.8 on 2023-12-22 10:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=20)),
                ('address', models.TextField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
                ('aadhar_card_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
