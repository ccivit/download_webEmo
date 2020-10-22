import csv
import os
import wget

files_to_download = ['test25.txt','train25.txt']

train = files_to_download[1]
test = files_to_download[0]

for file in files_to_download:
    if file == train:
        split = 'train'
    else:
        split = 'test'
    if not os.path.isdir(split):
        os.mkdir(split)

    print(split)

    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            # print(len(spamreader))
            i += 1
            # if i > 10:
            #     break
            print(row)
            url = row[0]
            category = row[1]
            file_name = url.split('/')[-1]
            print(file_name)
            if not os.path.isdir(os.path.join(split,category)):
                os.mkdir(os.path.join(split,category))
            destination = os.path.join(split,category,file_name)


            print(destination)
            wget.download(url,out = destination)
