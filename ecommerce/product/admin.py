from django.contrib import admin
from .models import Item, Attribute, Category, CategoryAttribute, ItemAttributeValue, Unit
# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Attribute)
admin.site.register(Unit)
admin.site.register(CategoryAttribute)
admin.site.register(ItemAttributeValue)