wordCloudText = ''
for dict in labels:
    addText= (dict.get('label_name')+' ')*dict.get('amount_of_images_tagged_in')
    wordCloudText += addText

file = open('word_cloud.txt', 'w')
file.write(wordCloudText)
file.close()