# Generated by Django 4.0.4 on 2022-06-06 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='silsite.project'),
        ),
    ]
