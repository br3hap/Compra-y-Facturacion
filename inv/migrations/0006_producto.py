# Generated by Django 2.2 on 2022-12-03 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0005_unidadmedida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('codigo_barra', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0)),
                ('existencia', models.IntegerField(default=0)),
                ('ultima_compra', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripcion del Producto', max_length=100, unique=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Marca')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.SubCategoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.UnidadMedida')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'unique_together': {('codigo', 'codigo_barra')},
            },
        ),
    ]