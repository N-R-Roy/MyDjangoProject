# Generated by Django 4.1.5 on 2023-01-25 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="asst_manager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proj_asst_manager",
                to="myapp.person",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="manager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proj_manager",
                to="myapp.person",
            ),
        ),
    ]
