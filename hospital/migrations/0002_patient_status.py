# Generated by Django 5.1.5 on 2025-01-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
