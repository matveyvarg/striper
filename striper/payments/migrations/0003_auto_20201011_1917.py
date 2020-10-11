# Generated by Django 3.0.10 on 2020-10-11 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20201010_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=0, verbose_name='H, o, w,  , b, i, g,  , i, s,  , d, i, s, c, o, u, n or t')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=0, verbose_name='H, o, w,  , b, i, g,  , i, s,  , t, a or x')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(verbose_name="I, t, e, m, ', s,  , d, e, s, c, r, i, p, t, i, o or n"),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name="I, t, e, m, ', s,  , n, a, m or e"),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=50, verbose_name="I, t, e, m, ', s,  , p, r, i, c or e"),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', to='payments.Item', verbose_name='I, t, e, m, s,  , t, o,  , p, u, r, c, h, a, s or e'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.Discount', verbose_name=' , D, i, s, c, o, u, n, t,  , a, p, p, l, i, e, d,  , f, o, r,  , o, r, d, e or r'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.Tax', verbose_name='T, a, x,  , a, p, p, l, i, e, d,  , f, o, r,  , o, r, d, e or r'),
        ),
    ]
