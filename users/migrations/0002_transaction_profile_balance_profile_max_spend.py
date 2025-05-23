# Generated by Django 5.2 on 2025-04-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_spend',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]
