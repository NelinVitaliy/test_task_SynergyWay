# Generated by Django 3.0.5 on 2020-04-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='User Nickname')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('group', models.ManyToManyField(related_name='users_group', to='groups.Group', verbose_name='The User Group')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]