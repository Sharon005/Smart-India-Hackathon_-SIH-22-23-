# Generated by Django 3.2.7 on 2022-03-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groundnut_Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=300, null=True)),
                ('rem', models.CharField(max_length=300, null=True)),
                ('slug', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Potato_Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=300, null=True)),
                ('rem', models.CharField(max_length=300, null=True)),
                ('slug', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Pulses_Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=300, null=True)),
                ('rem', models.CharField(max_length=300, null=True)),
                ('slug', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Rice_Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=300, null=True)),
                ('rem', models.CharField(max_length=300, null=True)),
                ('slug', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Tomato_Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=300, null=True)),
                ('rem', models.CharField(max_length=300, null=True)),
                ('slug', models.CharField(max_length=48)),
            ],
        ),
    ]
