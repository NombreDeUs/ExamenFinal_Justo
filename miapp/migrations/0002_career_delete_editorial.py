# Generated by Django 4.2.3 on 2023-07-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('idcareer', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('shortname', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='careers/')),
                ('state', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='editorial',
        ),
    ]