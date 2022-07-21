# Generated by Django 4.0.2 on 2022-07-21 10:48

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ትግርኛ', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ልጣፍ',
            options={'ordering': ['-ዕለት']},
        ),
        migrations.AddField(
            model_name='ልጣፍ',
            name='መጠቓለሊ',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ልጣፍ',
            name='ምስሊ',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='ልጣፍ',
            name='ምድብ',
            field=models.IntegerField(choices=[(0, 'ረቒቕ'), (1, 'ሕታም')], default=0),
        ),
        migrations.AddField(
            model_name='ልጣፍ',
            name='ስለግ',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ልጣፍ',
            name='ፈተውቲ',
            field=models.ManyToManyField(blank=True, related_name='tigpost_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ልጣፍ',
            name='ኣርእስቲ',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ልጣፍ',
            name='ዕለት',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ልጣፍ',
            name='ደራሲ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tigblog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ርእይቶ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ኢመይል', models.EmailField(max_length=254)),
                ('ትሕዝቶ', models.TextField(max_length=200)),
                ('ዕለት', models.DateTimeField(auto_now_add=True)),
                ('ፀዲቑ', models.BooleanField(default=False)),
                ('ልጣፍ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tigcomments', to='ትግርኛ.ልጣፍ')),
                ('ሽም', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tigpost_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['ዕለት'],
            },
        ),
    ]
