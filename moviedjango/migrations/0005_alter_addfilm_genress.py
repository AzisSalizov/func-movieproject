# Generated by Django 4.1.3 on 2022-11-30 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('moviedjango', '0004_delete_category_delete_genress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfilm',
            name='genress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genres.genress'),
        ),
    ]
