from django.db import models

CATEGORY_CHOICE =  (
    ('CLASSES 1-4', 'CLASSES 1-4'),
    ('CLASSES 5-8', 'CLASSES 5-8'),
    ('CLASSES 9-12', 'CLASSES 9-12'),
)

class Coding(models.Model):
    name = models.CharField(max_length=50)
    whatsapp_no = models.IntegerField()
    contact_no = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=50)
    class_name = models.CharField(max_length=20)
    school = models.CharField(max_length=100)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICE, default='CLASSES 1-4')
    payment_id = models.CharField(max_length=50, null=False, blank=False)
    paid = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.category

