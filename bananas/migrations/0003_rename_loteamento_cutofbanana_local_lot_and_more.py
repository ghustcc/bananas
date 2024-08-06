# Generated by Django 5.0.6 on 2024-08-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bananas', '0002_lots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cutofbanana',
            old_name='loteamento',
            new_name='local_lot',
        ),
        migrations.RenameField(
            model_name='cutofbanana',
            old_name='fisrt',
            new_name='numero_lot',
        ),
        migrations.RemoveField(
            model_name='cutofbanana',
            name='second',
        ),
        migrations.AddField(
            model_name='cutofbanana',
            name='primeira',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cutofbanana',
            name='segunda',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lots',
            name='numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lots',
            name='hectares',
            field=models.FloatField(default=0),
        ),
    ]
