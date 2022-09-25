import json
file = open('./labels_data.json')
data = json.load(file)

proper_labels = []

for label in data:
    avg_view = label['total_views']/label['num_of_artefacts_tagged_in']
    new_label = {'name': label['name'], 'total_views': label['total_views'], 'num_of_artefacts_tagged_in': label['num_of_artefacts_tagged_in'], 'avg_view_per_artefact': avg_view}
    if new_label['num_of_artefacts_tagged_in'] >=5:
        proper_labels.append(new_label)
new_data_file = open("total_tagged_in_label_data.json", "w")

def sort_func(param):
    return param['num_of_artefacts_tagged_in']

proper_labels.sort(reverse=True, key=sort_func)


json.dump(proper_labels, new_data_file)
new_data_file.close()