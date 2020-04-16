# Generated by Django 3.0.5 on 2020-04-16 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20200416_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='type',
            field=models.CharField(choices=[('binary', 'Binary'), ('digital', 'Digital')], default='digital', max_length=8),
        ),
    ]
