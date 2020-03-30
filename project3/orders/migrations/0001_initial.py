# Generated by Django 2.0.3 on 2020-03-21 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaname', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('useremail', models.CharField(max_length=64)),
                ('userpassword', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizzaid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User'),
        ),
    ]