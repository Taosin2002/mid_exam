# Generated by Django 4.2.7 on 2023-12-24 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='author/media/')),
                ('name', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
