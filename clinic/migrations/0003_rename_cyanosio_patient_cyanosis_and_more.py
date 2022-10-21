# Generated by Django 4.1.2 on 2022-10-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_personalhistory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='cyanosio',
            new_name='cyanosis',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='edenro',
            new_name='edema',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='lcterus',
            new_name='icterus',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='lumph_adenopathy',
            new_name='lymphadenopathy',
        ),
        migrations.AddField(
            model_name='patient',
            name='investigation',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='provisional_diagnosis',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='bp',
            field=models.CharField(max_length=20, verbose_name='BP (mm of Hg)'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pulse_rate',
            field=models.CharField(max_length=20, verbose_name='Pulse Rate (BpM)'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='temperature',
            field=models.CharField(max_length=20, verbose_name='Temperature (°F)'),
        ),
    ]