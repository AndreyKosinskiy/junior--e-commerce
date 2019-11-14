# Generated by Django 2.2.7 on 2019-11-14 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120)),
                ('is_subcategory', models.BooleanField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('discont', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ItemAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_str', models.CharField(blank=True, max_length=120)),
                ('value_num', models.CharField(blank=True, max_length=120)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Attribute')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Item')),
                ('unit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ManyToManyField(to='product.Attribute')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
    ]