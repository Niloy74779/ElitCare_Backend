# Generated by Django 4.2.7 on 2024-06-21 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_alter_review_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]
