# Generated by Django 3.2.7 on 2021-10-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CollectorAPI', '0005_remove_honeypotinfo_raw_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoneypotAgregate24hIps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=45)),
                ('country_iso', models.CharField(max_length=4, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HoneypotAgregate30DIps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=45)),
                ('country_iso', models.CharField(max_length=4, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HoneypotAgregate7DIps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=45)),
                ('country_iso', models.CharField(max_length=4, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
