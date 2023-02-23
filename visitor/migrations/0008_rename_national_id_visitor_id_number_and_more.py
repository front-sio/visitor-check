# Generated by Django 4.1.4 on 2022-12-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0007_visitor_national_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='national_id',
            new_name='id_number',
        ),
        migrations.AddField(
            model_name='visitor',
            name='on_behalf',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
