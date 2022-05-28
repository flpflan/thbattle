# Generated by Django 3.2.13 on 2022-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.SlugField(help_text='类型', max_length=20, verbose_name='类型')),
                ('count', models.PositiveIntegerField(help_text='数量', verbose_name='数量')),
            ],
            options={
                'verbose_name': '物品',
                'verbose_name_plural': '物品',
            },
        ),
        migrations.CreateModel(
            name='ItemActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.SlugField(help_text='动作', max_length=20, verbose_name='动作')),
                ('sku', models.SlugField(help_text='类型', max_length=20, verbose_name='类型')),
                ('count', models.IntegerField(help_text='数量', verbose_name='数量')),
                ('extra', models.CharField(help_text='额外数据', max_length=256, verbose_name='额外数据')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='日期', verbose_name='日期')),
            ],
            options={
                'verbose_name': '物品动作历史',
                'verbose_name_plural': '物品动作历史',
            },
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.SlugField(help_text='类型', max_length=20, verbose_name='类型')),
                ('count', models.IntegerField(help_text='数量', verbose_name='数量')),
                ('currency', models.SlugField(help_text='货币', max_length=20, verbose_name='货币')),
                ('price', models.IntegerField(help_text='售价', verbose_name='售价')),
            ],
            options={
                'verbose_name': '商店',
                'verbose_name_plural': '商店',
            },
        ),
    ]
