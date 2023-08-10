from uuid import UUID
import json



def message_to_json(data:str):
    data_dict = {}
    for item in data.split():
        key, value = item.split('=')
        if value.startswith('UUID'):
            value = UUID(value[6:-2])
        elif value == 'True':
            value = True
        elif value == 'False':
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
        data_dict[key] = value

    json_data = json.dumps(data_dict, indent=4, default=str)
    return json.loads(json_data)