# Generated by Django 4.2 on 2023-10-08 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DohoronName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('fatherName', models.CharField(blank=True, max_length=255, null=True)),
                ('motherName', models.CharField(blank=True, max_length=255, null=True)),
                ('nid', models.CharField(blank=True, max_length=255, null=True)),
                ('tinNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PodokName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doron', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, max_length=255, null=True, upload_to='report/%Y/%m/%d/')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_report', to='backend.report')),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('income', models.CharField(blank=True, max_length=255, null=True)),
                ('business', models.TextField(blank=True, null=True)),
                ('contribution', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
        ),
        migrations.CreateModel(
            name='Political',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politicalInfo', models.TextField(blank=True, null=True)),
                ('electionInfo', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
        ),
        migrations.CreateModel(
            name='PodokChildName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('podokname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.podokname')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parmentAdd', models.TextField(blank=True, null=True)),
                ('presentAdd', models.TextField(blank=True, null=True)),
                ('birthPlace', models.CharField(blank=True, max_length=255, null=True)),
                ('dateOfBirth', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('bodyColor', models.CharField(blank=True, max_length=255, null=True)),
                ('clue', models.CharField(blank=True, max_length=255, null=True)),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('passport', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('family', models.TextField(blank=True, null=True)),
                ('wealth', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Podok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('podokdate', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
                ('podok', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.podokname')),
            ],
        ),
        migrations.CreateModel(
            name='Mamla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mamlaInfo', models.TextField(blank=True, null=True)),
                ('sabotageInfo', models.TextField(blank=True, null=True)),
                ('arrestOrder', models.TextField(blank=True, null=True)),
                ('arrestInfo', models.TextField(blank=True, null=True)),
                ('corruptionInfo', models.TextField(blank=True, null=True)),
                ('thanaRecord', models.TextField(blank=True, null=True)),
                ('influential', models.CharField(blank=True, max_length=255, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]