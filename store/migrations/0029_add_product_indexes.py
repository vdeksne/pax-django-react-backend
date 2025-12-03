# Generated manually for product indexes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_product_image'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['status', 'featured'], name='store_produ_status_featur_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['status', '-date'], name='store_produ_status_date_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['slug'], name='store_produ_slug_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category', 'status'], name='store_produ_categor_status_idx'),
        ),
    ]
