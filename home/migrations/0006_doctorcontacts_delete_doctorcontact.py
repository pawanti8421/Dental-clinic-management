# Generated by Django 5.0.3 on 2024-03-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_usercontacts_delete_usercontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='DoctorContact',
        ),
    ]
