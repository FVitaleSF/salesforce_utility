class fields_describe:


    def get_field_names(fields):
        field_names = []
        for i in fields:
            field_names.append(i.get('name'))
        return field_names

    def get_fields_properties(fields):
        data_type = []
        for d in fields:
            data_type.append(d.get('referenceTo'))
        
        picklist_values = []
        if data_type == 'Picklist':
            for p in fields.get('picklistValues'):
                picklist_values.add(p)
        return data_type

    