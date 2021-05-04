from django.core.serializers import serialize
import json

class SerializeMixin(object):
    def Serialize(self,qs):
        y=serialize('json',qs)
        p_data = json.loads(y)
        finallist = []
        for obj in p_data:
            emp_data = obj['fields']
            finallist.append(emp_data)
        y = json.dumps(finallist)
        return y


