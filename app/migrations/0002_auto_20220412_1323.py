# Generated by Django 3.2.9 on 2022-04-12 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tache',
            old_name='personne',
            new_name='evaluateur',
        ),
        migrations.AddField(
            model_name='personne',
            name='taches',
            field=models.ManyToManyField(blank=True, null=True, to='app.Tache'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='libelle',
            field=models.CharField(default='Projet sans nom', max_length=250),
        ),
        migrations.AlterField(
            model_name='projet',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.personne'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='libelle',
            field=models.CharField(default='Tache sans nom', max_length=200),
        ),
        migrations.AlterField(
            model_name='tache',
            name='tacheParente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tache'),
        ),
    ]