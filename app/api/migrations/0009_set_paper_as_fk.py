# Generated by Django 2.1.11 on 2020-01-02 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_set_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='paper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Paper'),
        ),
    ]
