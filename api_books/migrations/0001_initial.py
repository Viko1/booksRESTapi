from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('language', models.BooleanField(max_length=20)),
                ('categories', models.CharField(max_length=300)),
                ('number_isbm', models.BooleanField(max_length=5)),
                ('page_count', models.BooleanField(max_length=5)),
                ('thumbnail', models.CharField(max_length=200)),
            ],
        ),
    ]
