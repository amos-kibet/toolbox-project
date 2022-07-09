# Generated by Django 2.0.8 on 2022-07-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('adanger', 'Priority High'), ('bwarning', 'Priority Medium'), ('csuccess', 'Priority Low')], default='adanger', max_length=30)),
                ('complete', models.IntegerField(default=0)),
            ],
        ),
    ]
