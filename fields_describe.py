class fields_describe:

    @staticmethod
    def get_field_names(fields):
        field_names = []
        for i in fields:
            field_names.append(i.get('name'))
        return field_names
    
    @staticmethod
    def get_fields_properties(fields):
        data_type = {}
        for d in fields:
            data_type[d.get('name')] = d.get('type')
        return data_type
    
    def get_picklist_values():
        picklist_values = []
        for p in fields.get('picklistValues'):
            picklist_values.add(p)
        return picklist_values
            
        

    