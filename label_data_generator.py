import json
  
# Opening JSON file
file = open('./output_clean_data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(file)

labels = []

count = 0

for artefact in data:
    print(count)
    all_labels = artefact['labels']

    for label in all_labels:

        logged_previosuly = False

        for added_label in labels:

            if added_label['name'] == label['name']:
                logged_previosuly = True
                added_label['total_views'] += artefact['total_views']
                added_label['num_of_artefacts_tagged_in'] += 1
        
        if not logged_previosuly:
            labels.append({'name': label['name'], 'total_views': artefact['total_views'], 'num_of_artefacts_tagged_in': 1})

    count+=1

new_data_file = open("labels_data.json", "w")
json.dump(labels, new_data_file)
new_data_file.close()
        
            
