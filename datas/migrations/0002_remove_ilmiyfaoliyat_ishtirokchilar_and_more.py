# Generated by Django 5.0.6 on 2025-04-27 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ilmiyfaoliyat',
            name='ishtirokchilar',
        ),
        migrations.AddField(
            model_name='ilmiyfaoliyat',
            name='ishtirokchilar',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='datas.talaba'),
            preserve_default=False,
        ),
    ]
