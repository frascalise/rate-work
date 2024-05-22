# Generated by Django 5.0.6 on 2024-05-22 15:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utente', '0002_utente_citta'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnuncioLavoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200, verbose_name='titolo')),
                ('descrizione', models.TextField(verbose_name='descrizione')),
                ('data_pubblicazione', models.DateTimeField(auto_now_add=True, verbose_name='data di pubblicazione')),
                ('is_distanza', models.BooleanField(default=False, verbose_name='id_distanza')),
                ('range_stipendio', models.CharField(choices=[('1000-1200', '1000-1200'), ('1200-1500', '1200-1500'), ('1500-2000', '1500-2000'), ('2000-2500', '2000-2500'), ('2500+', '2500+')], max_length=50, verbose_name='range_stipendio')),
                ('azienda', models.ForeignKey(limit_choices_to={'is_azienda': True}, on_delete=django.db.models.deletion.CASCADE, related_name='annunci', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
