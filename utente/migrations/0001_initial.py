# Generated by Django 5.0.6 on 2024-05-27 16:41

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('citta', models.CharField(max_length=100, verbose_name='citta')),
                ('is_azienda', models.BooleanField(default=False, verbose_name='is_azienda')),
                ('tag', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='tag')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Utente',
                'verbose_name_plural': 'Utenti',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AnnuncioLavoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200, verbose_name='titolo')),
                ('descrizione', models.TextField(verbose_name='descrizione')),
                ('data_pubblicazione', models.DateTimeField(auto_now_add=True, verbose_name='data di pubblicazione')),
                ('is_distanza', models.BooleanField(default=False, verbose_name='id_distanza')),
                ('tag', models.CharField(default=None, max_length=200, null=True, verbose_name='tag')),
                ('range_stipendio', models.CharField(choices=[('1000-1200', '1000-1200'), ('1200-1500', '1200-1500'), ('1500-2000', '1500-2000'), ('2000-2500', '2000-2500'), ('2500+', '2500+')], max_length=50, verbose_name='range_stipendio')),
                ('is_available', models.BooleanField(default=True, verbose_name='is_available')),
                ('azienda', models.ForeignKey(limit_choices_to={'is_azienda': True}, on_delete=django.db.models.deletion.CASCADE, related_name='annunci', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Annuncio di Lavoro',
                'verbose_name_plural': 'Annunci di Lavoro',
            },
        ),
        migrations.CreateModel(
            name='Lavoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stato', models.CharField(choices=[('In attesa', 'In attesa'), ('Accettato', 'Accettato'), ('Rifiutato', 'Rifiutato')], default='In attesa', max_length=200, verbose_name='stato')),
                ('annuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lavori', to='utente.annunciolavoro')),
                ('lavoratore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lavori', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lavoro',
                'verbose_name_plural': 'Lavori',
            },
        ),
        migrations.CreateModel(
            name='Recensione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valutazione', models.IntegerField(choices=[(1, 'Positivo'), (0, 'Neutro'), (-1, 'Negativo')], verbose_name='valutazione')),
                ('titolo', models.CharField(max_length=200, verbose_name='titolo')),
                ('commento', models.TextField(verbose_name='commento')),
                ('destinatario', models.ForeignKey(limit_choices_to={'is_azienda': False}, on_delete=django.db.models.deletion.CASCADE, related_name='recensione_destinatario', to=settings.AUTH_USER_MODEL)),
                ('lavoro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recensioni', to='utente.lavoro')),
                ('mittente', models.ForeignKey(limit_choices_to={'is_azienda': True}, on_delete=django.db.models.deletion.CASCADE, related_name='recensione_mittente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recensione',
                'verbose_name_plural': 'Recensioni',
            },
        ),
    ]
