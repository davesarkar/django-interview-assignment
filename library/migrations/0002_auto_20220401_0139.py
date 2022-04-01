# Generated by Django 3.2.12 on 2022-03-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='record_type',
            field=models.CharField(choices=[('BORROW', 'BORROW'), ('RETURN', 'RETURN')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(choices=[(False, 'BORROWED'), (True, 'AVAILABLE')], default=False),
        ),
    ]