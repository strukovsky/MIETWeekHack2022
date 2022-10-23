# Generated by Django 4.1.2 on 2022-10-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoIPConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sip_server_address', models.CharField(max_length=255)),
                ('sip_server_port', models.PositiveBigIntegerField(default=5060)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('sip_client_address', models.CharField(max_length=255)),
                ('sip_client_port', models.PositiveBigIntegerField(default=5060)),
            ],
        ),
    ]