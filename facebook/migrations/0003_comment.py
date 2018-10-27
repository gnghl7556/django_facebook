# Generated by Django 2.1.1 on 2018-10-27 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_auto_20181027_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('password', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='facebook.Article')),
            ],
        ),
    ]
