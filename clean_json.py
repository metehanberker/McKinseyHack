import json
import time

# Grab Currrent Time Before Running the Code
start = time.time()

data = []
with open('./prelim_data_set_1.json', encoding="utf8") as f:
    for line in f:
        data.append(json.loads(line))

all_data = []
new_data_file = open("myfile.json", "w")
counter = 0

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


for obj in data:

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
        count = 0
        for image in obj['_source']['multimedia']:
            if image['type']['type'] == 'image':
                count+=1
            else:
                continue
        length_of_images = count

    except:
        length_of_images = 0

    try:
        labels = [{'name': one_label['value'], 'confidence':one_label['details']['confidence']} for one_label in obj['_source']['multimedia'][0]['enhancement']['rekognition'][0]['labels'] ]
    
    except:
        labels = []

    new_obj = {'id': id, 'total_views': total_views, 'description': description, 'image_count': length_of_images, 'labels': labels}
    all_data.append(new_obj)
    # json.dump(new_obj, new_data_file)

    print(counter)
    counter += 1


json.dump(all_data, new_data_file)
new_data_file.close()

end = time.time()

#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))