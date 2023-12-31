# Generated by Django 3.2.6 on 2024-01-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emploi', '0002_emploi_etudiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emploi',
            name='annee_date_debut',
            field=models.CharField(choices=[('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031')], max_length=40),
        ),
        migrations.AlterField(
            model_name='emploi',
            name='annee_date_fin',
            field=models.CharField(blank=True, choices=[('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031')], max_length=40, null=True),
        ),
    ]
