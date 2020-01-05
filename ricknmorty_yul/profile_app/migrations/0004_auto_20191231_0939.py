# Generated by Django 3.0.1 on 2019-12-31 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_auto_20191231_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_app.Gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='planet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_app.Planet'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_app.Species'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_app.Status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_app.Type'),
        ),
    ]