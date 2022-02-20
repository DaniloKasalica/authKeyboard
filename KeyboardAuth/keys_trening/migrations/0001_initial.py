# Generated by Django 4.0.2 on 2022-02-20 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('key', models.CharField(max_length=16, unique=True)),
                ('hold_time', models.IntegerField(blank=True, null=True)),
                ('presure_up', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('presure_down', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('finger_size_up', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('finger_size_down', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateX_up', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateY_up', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateX_down', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateY_down', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_edited', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_key_training_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'key_trining',
            },
        ),
        migrations.CreateModel(
            name='KeyPairsTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('keys', models.CharField(max_length=16, unique=True)),
                ('flight_time', models.IntegerField(blank=True, null=True)),
                ('hold_time1', models.IntegerField(blank=True, null=True)),
                ('presure_up1', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('presure_down2', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('presure_size_up1', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('presure_size_down2', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateX_up1', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateY_up1', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateX_down2', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('coordinateY_down2', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_edited', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_key_pairs_training_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'key_pairs_trining',
            },
        ),
    ]