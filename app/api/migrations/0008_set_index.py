# Generated by Django 2.1.11 on 2019-12-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_set_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='doi',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='journal',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pmc',
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='pmid',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.TextField(db_index=True),
        ),
    ]
