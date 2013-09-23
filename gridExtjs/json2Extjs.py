from django.core.serializers.json import Serializer
from django.utils.encoding import smart_unicode
import datetime

from django.db.models.fields import DateTimeField, DateField, TimeField

DATE_FORMAT_FIELD = '%d/%m/%Y'
DATE_TIME_FORMAT_FIELD = '%d/%m/%Y %H:%M:%S'
TIME_FORMAT_FIELD = '%H:%M'

class ExtJSONSerialiser(Serializer):
    """
    Serializes a QuerySet to basic Python objects.
    """

    def __init__(self, *args, **kwargs):
        self.extraFields = {}
        Serializer.__init__(self, *args, **kwargs)
        
    def get_dump_object(self, obj):
        '''
        Por cause desse metodo, essa aplicacao requer agora o django 1.5 ou posterior
        '''
        options_2_extjs = getattr(obj, 'Options2GridExtjs', None)
        if options_2_extjs:
            self.extraFields = getattr(options_2_extjs, 'extra_fields', {})
        self._current.update({"pk": smart_unicode(obj._get_pk_val(), strings_only = True), })
        self._current.update({"pk": smart_unicode(obj._get_pk_val(), strings_only = True), })
        ATTR_INDEX = 1
        for field, attribute in self.extraFields.items():
            self._current.update({field:getattr(obj, attribute[ATTR_INDEX])})
        return self._current

    def handle_field(self, obj, field):
        if isinstance(field, DateTimeField):
            self._current[field.name] = ''
            datetime = getattr(obj, field.name)
            if datetime:
                datetimeStr = datetime.strftime(DATE_TIME_FORMAT_FIELD)
                self._current[field.name] = datetimeStr
        elif isinstance(field, DateField):
            self._current[field.name] = ''
            date = getattr(obj, field.name)
            if date:
                dateStr = date.strftime(DATE_FORMAT_FIELD)
                self._current[field.name] = dateStr
        elif isinstance(field, TimeField):
            self._current[field.name] = ''
            time = getattr(obj, field.name)
            if time:
                timeStr = time.strftime(TIME_FORMAT_FIELD)
                self._current[field.name] = timeStr
        else:
            super(ExtJSONSerialiser, self).handle_field(obj, field)
