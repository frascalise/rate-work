# Generated by Django 5.0.6 on 2024-05-26 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utente', '0003_annunciolavoro_is_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lavoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lavori', to='utente.annunciolavoro')),
                ('lavoratore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lavori', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lavoro',
                'verbose_name_plural': 'Lavori',
            },
        ),
    ]
