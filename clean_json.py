import json
import time

# Grab Currrent Time Before Running the Code
start = time.time()

with open('./prelim_data_set_1.json', 'r') as f:
  data = json.load(f)


all_data = []
new_data_file = open("myfile.json", "w")


def find_primary_description(objects):

    for object in objects:  
        
        try:
            is_primary = object['primary']
        except:
            continue
        
        if is_primary == True:
            return object['value']
        else:
            continue
    
    return ''


for obj in data['data']:

    try:
        id = obj['_id']
    except:
        continue
    
    try:
        total_views = obj['_source']['admin']['analytics']['count']['total']
    except:
        total_views = 0

    try:
        description = find_primary_description(obj['_source']['description'])
    except:
        description = ''

    try:
        type_of_object = obj['_type']
    except:
        continue

    try:
        count = 0
        for image in obj['_source']['multimedia']:
            if image['type']['type'] == 'image':
                count+=1
            else:
                continue
        length_of_images = count

    except:
        length_of_images = 0



    new_obj = {'id': id, 'total_views': total_views, 'description': description, 'type': type_of_object, 'image_count': length_of_images}
    # json.dump(new_obj, new_data_file)
    all_data.append(new_obj)


json.dump(all_data, new_data_file)
new_data_file.close()

end = time.time()

#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))