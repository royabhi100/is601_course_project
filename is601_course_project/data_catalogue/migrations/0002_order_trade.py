# Generated by Django 4.0.3 on 2022-04-25 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField()),
                ('ticker', models.CharField(max_length=256)),
                ('environment_type', models.CharField(choices=[('DEV', 'Development'), ('PROD', 'Production'), ('UAT', 'Staging')], max_length=4)),
                ('price', models.FloatField()),
                ('size', models.IntegerField()),
                ('state', models.CharField(choices=[('O', 'Open'), ('E', 'Executed'), ('P', 'Partial'), ('C', 'Cancelled')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradeid', models.IntegerField()),
                ('orderid', models.IntegerField()),
                ('ticker', models.CharField(max_length=256)),
                ('environment_type', models.CharField(choices=[('DEV', 'Development'), ('PROD', 'Production'), ('UAT', 'Staging')], max_length=4)),
                ('price', models.FloatField()),
                ('size', models.IntegerField()),
            ],
        ),
    ]
