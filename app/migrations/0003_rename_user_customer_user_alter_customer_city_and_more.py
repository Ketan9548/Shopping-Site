# Generated by Django 4.2.3 on 2023-08-21 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_alter_product_category_alter_product_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='User',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Jammu & Kashmir', 'Jammu & Kashmir'), ('Rajisthan', 'Rajisthan'), ('Udisa', 'Udisa'), ('Goa', 'Goa'), ('Tamil Nadu', 'Tamil Nadu'), ('Udham Singh nagar', 'Udham Singh nagar'), ('Tripura', 'Tripura'), ('Greater Noida', 'Greater Noida'), ('Punjab', 'Punjab'), ('jaspur Udham Singh nagar', 'jaspur Udham Singh nagar'), ('Gujrat', 'Gujrat'), ('West Bengal', 'West Bengal'), ('Assam', 'Assam'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Mumbai', 'Mumbai'), ('Sikkim', 'Sikkim'), ('Hariyana', 'Hariyana'), ('Uttarakhan', 'Uttarakhan'), ('Bihar', 'Bihar'), ('Karnatak', 'Karnatak'), ('Noida', 'Noida'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Telangana', 'Telangana'), ('Delhi', 'Delhi'), ('Madhya Pradesh', 'Madhya Pradesh')], max_length=100),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]