# Generated by Django 2.2.2 on 2019-06-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('test_date', models.DateTimeField()),
                ('answers', models.CharField(max_length=200)),
                ('result', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
