# Generated by Django 2.1.3 on 2018-11-17 01:38

import disasterinfosite.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedsnugget',
            name='snugget_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.Snugget'),
        ),
        migrations.AlterField(
            model_name='eq_fault_buffer',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.EQ_Fault_Buffer.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='eq_fault_shaking',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.EQ_Fault_Shaking.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='eq_fault_worst',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.EQ_Fault_Worst.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='eq_historic_distance',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.EQ_Historic_Distance.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='fire_burn_probability2',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Fire_Burn_Probability2.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='fire_hist_bound',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Fire_Hist_Bound.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='fire_worst_case_ph2',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Fire_Worst_Case_ph2.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='flood_channel_migration_zones',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Flood_Channel_Migration_Zones.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='flood_fema_dfrim_2015',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Flood_FEMA_DFRIM_2015.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='flood_worst_case',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Flood_Worst_Case.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='landslide_placeholder2',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.Landslide_placeholder2.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='snugget',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='summerstorm',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.summerstorm.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
        migrations.AlterField(
            model_name='textsnugget',
            name='snugget_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disasterinfosite.Snugget'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='winterstorm',
            name='group',
            field=models.ForeignKey(default=disasterinfosite.models.winterstorm.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.ShapefileGroup'),
        ),
    ]