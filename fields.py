from django.db import models
from django.forms import DateField

class BSFormDateField(DateField):
    def widget_attrs(self, widget):
        attrs = super(BSFormDateField, self).widget_attrs(widget)
        attrs.update({'data-input-type': 'datepicker'})
        return attrs

class BSDateField(models.DateField):    
    def formfield(self, **kwargs):
        defaults = {'form_class': BSFormDateField}
        defaults.update(kwargs)
        return super(BSDateField, self).formfield(**defaults)