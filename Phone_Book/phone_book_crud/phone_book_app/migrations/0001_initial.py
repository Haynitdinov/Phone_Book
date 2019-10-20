# Generated by Django 2.2.5 on 2019-10-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfirst_name', models.CharField(max_length=50)),
                ('plast_name', models.CharField(max_length=50)),
                ('pphone_number', models.CharField(max_length=50)),
                ('pemail', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
