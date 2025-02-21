# Generated by Django 5.0.6 on 2024-06-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0003_alter_insight_end_year_alter_insight_start_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='added',
            field=models.DateTimeField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='end_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='insight',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='intensity',
            field=models.IntegerField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='likelihood',
            field=models.IntegerField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='published',
            field=models.DateTimeField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='relevance',
            field=models.IntegerField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='start_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='url',
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
    ]
