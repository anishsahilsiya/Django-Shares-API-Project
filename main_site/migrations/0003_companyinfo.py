# Generated by Django 3.1.2 on 2022-05-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_site', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('sector', models.CharField(default='N/A', max_length=255)),
                ('industry', models.CharField(default='N/A', max_length=255)),
            ],
        ),
    ]
