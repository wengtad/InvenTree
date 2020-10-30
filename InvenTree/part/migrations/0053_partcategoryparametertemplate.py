# Generated by Django 3.0.7 on 2020-10-30 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0052_auto_20201027_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartCategoryParameterTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_value', models.CharField(blank=True, help_text='Default Parameter Value', max_length=500)),
                ('category', models.ForeignKey(help_text='Part Category', on_delete=django.db.models.deletion.CASCADE, related_name='parameter_templates', to='part.PartCategory')),
                ('parameter_template', models.ForeignKey(help_text='Parameter Template', on_delete=django.db.models.deletion.CASCADE, related_name='part_categories', to='part.PartParameterTemplate')),
            ],
        ),
        migrations.AddConstraint(
            model_name='partcategoryparametertemplate',
            constraint=models.UniqueConstraint(fields=('category', 'parameter_template'), name='unique_category_parameter_template_pair'),
        ),
    ]
