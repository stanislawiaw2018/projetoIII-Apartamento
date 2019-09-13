# Generated by Django 2.2.4 on 2019-09-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('qtdQuartos', models.IntegerField()),
                ('proprietario', models.CharField(max_length=50)),
                ('valor_Condominio', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
