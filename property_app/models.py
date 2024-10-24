from django.db import models

property_type =(
    ('apartment', 'Apartment'),
    ('commercial', 'Commercial'),
    ('house', 'House'),
)
# property modules
class Property(models.Model):
    name = models.CharField(max_length=110)
    address = models.CharField(max_length=110)
    property_type = models.CharField(max_length=110, choices=property_type)
    description = models.TextField()
    number_of_units = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
# units modules
class Units(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    rents = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.property.name
    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
    # tenant modules
class Renter(models.Model):
    Name_renter= models.CharField(max_length=110)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.Name_renter
    class Meta:
        verbose_name = 'Renter'
        verbose_name_plural = 'Renters'
    # lesase mudoles
class Agreement(models.Model):
        renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
        unit = models.ForeignKey(Units, on_delete=models.CASCADE)
        start_date = models.DateField()
        end_date = models.DateField()
        def __str__(self):
            return self.renter.Name_renter
        class Meta:
            verbose_name = 'Agreement'
            verbose_name_plural = 'Agreements'


