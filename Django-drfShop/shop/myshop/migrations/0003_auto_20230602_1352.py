# Generated by Django 3.2 on 2023-06-02 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_category_real_estate'),
    ]

    operations = [
        migrations.AddField(
            model_name='real_estate',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='real_estate',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realestate_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.real_estate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='real_estate',
            name='LikeUser',
            field=models.ManyToManyField(blank=True, related_name='LikeUser', through='myshop.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
