from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=120, blank=True, null=False)
    is_subcategory = models.BooleanField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=120, blank=True, null=False)
    description = models.TextField()
    price = models.FloatField()
    discont = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    is_delete =models.BooleanField()

    category = models.ForeignKey("Category", on_delete=models.CASCADE,null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
        cat_attr = CategoryAttribute.objects.filter(category = self.category).first()
        attrs = cat_attr.attribute.all()
        for attr in cat_attr.attribute.all():
            ItemAttributeValue.objects.create(attribute = attr, item = self)
        

    def __str__(self):
        return self.title

class Attribute(models.Model):
    title = models.CharField(max_length=120, blank=True, null=False)
    def __str__(self):
        return self.title

class CategoryAttribute(models.Model):
    category = models.ForeignKey("Category",on_delete = models.CASCADE)
    attribute = models.ManyToManyField("Attribute")
    def __str__(self):
        return self.category.title+"| "+ " ".join([i.title for i in self.attribute.all() ])
        
class ItemAttributeValue(models.Model):
    #если значение число, например "12 размер" или "12 сантиметров"
    value_str = models.CharField(max_length=120, blank=True, null=False)
    #если значение строка, например белый, левый
    value_num = models.CharField(max_length=120, blank=True, null=False)
    #поле единици измерения, например см, м , кг, г
    unit =  models.ForeignKey("Unit", on_delete = models.CASCADE, blank=True, null=True)
    attribute = models.ForeignKey("Attribute", on_delete = models.CASCADE)
    item = models.ForeignKey("Item", on_delete = models.CASCADE)
    def __str__(self):
            return self.item.title + " " + self.attribute.title

class Unit(models.Model):
    unit = models.CharField(max_length = 120)