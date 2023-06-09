# Generated by Django 4.1.3 on 2023-03-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('financial', 'Financial'), ('operational', 'Operational'), ('strategic', 'Strategic'), ('compliance', 'Compliance'), ('cybersecurity', 'Cybersecurity'), ('reputational', 'Reputational'), ('legal', 'Legal'), ('environmental', 'Environmental'), ('health_safety', 'Health and Safety'), ('technology', 'Technology'), ('supply_chain', 'Supply Chain'), ('market', 'Market'), ('political', 'Political'), ('social', 'Social'), ('human_resource', 'Human Resource')], max_length=50)),
                ('owner', models.CharField(max_length=255)),
                ('likelihood', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=50)),
                ('impact', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=50)),
                ('overall_score', models.IntegerField(default=50)),
                ('status', models.CharField(choices=[('active', 'Active'), ('resolved', 'Resolved'), ('mitigated', 'Mitigated')], max_length=50)),
                ('mitigation_plan', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('review_date', models.DateField()),
            ],
        ),
    ]
