# Generated by Django 5.0.3 on 2024-03-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_delete_bookappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookappointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('useremail', models.EmailField(max_length=200)),
                ('doctorname', models.CharField(max_length=200)),
                ('doctoremail', models.EmailField(max_length=200)),
                ('clinicname', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('appdate', models.CharField(max_length=200)),
                ('apptime', models.CharField(max_length=100)),
                ('consultationfee', models.CharField(max_length=10)),
                ('payment', models.CharField(max_length=100)),
            ],
        ),
    ]
