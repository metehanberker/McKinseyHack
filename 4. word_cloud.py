import json
file = open('./labels_data/labels_data.json')
data = json.load(file)

wordCloudText = ''

for dict in data:
    addText= (dict.get("name")+' ')*dict.get("num_of_artefacts_tagged_in")
    wordCloudText += addText

file = open('word_cloud.txt', 'w')
file.write(wordCloudText)
file.close()