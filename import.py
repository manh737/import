import csv 
arr =[] 
count = 0
with open('image.csv', mode='r') as csv_file: 
    csv_reader = (csv.reader(csv_file))
    line_count = 0 
    wtr = csv.writer(open ('image-3.csv', 'w'), lineterminator='\n') 
    for row in (csv_reader): 
        if count == 0:
            wtr.writerow(row)
            count +=1
        else:
            tmp = (row[1].replace('jpg,','jpg').replace('jpg','jpg,').replace('(','').replace(')','').replace("&",'_').replace(' ','-').replace("'",'_'))[:-1].split(',')
            tmpCount = 0
            for image in tmp:
                if tmpCount == 0:
                    row[1] = image
                    row[7] = image
                    row[3] = row[3].replace('(','').replace(')','').replace(' ','-').replace("'",'_').replace("&",'_')
                    row[5] = row[5].replace('(','').replace(')','').replace(' ','-').replace("'",'_').replace("&",'_')
                    wtr.writerow(row)
                    tmpCount+=1
                else:
                    row[1] = ''
                    row[2] = ''
                    row[3] = ''
                    row[4] = ''
                    row[5] = ''
                    row[6] = ''
                    row[7] = image
                    wtr.writerow(row)
    wtr.writerows(arr)