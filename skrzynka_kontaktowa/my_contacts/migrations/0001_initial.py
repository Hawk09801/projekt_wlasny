# Generated by Django 2.1.3 on 2018-11-28 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64, null=True)),
                ('street', models.CharField(max_length=64, null=True)),
                ('house_number', models.SmallIntegerField(null=True)),
                ('apartment_number', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=64, null=True)),
                ('mail_type', models.IntegerField(choices=[(1, 'mail prywatny'), (2, 'mail służbowy'), (3, 'inny')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('description', models.TextField(null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_contacts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Telephon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('type_number', models.IntegerField(choices=[(1, 'numer domowy'), (2, 'numer służbowy'), (3, 'numer komórkowy'), (4, 'inny')], null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_contacts.Person')),
            ],
        ),
        migrations.AddField(
            model_name='mail',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_contacts.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='person',
            field=models.ManyToManyField(to='my_contacts.Person'),
        ),
    ]
