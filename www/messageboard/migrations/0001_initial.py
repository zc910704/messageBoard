# Generated by Django 2.0 on 2018-05-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_text', models.CharField(max_length=200)),
                ('msg_sender', models.CharField(max_length=64)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
