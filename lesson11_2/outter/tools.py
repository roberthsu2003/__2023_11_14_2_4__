import csv

def saveToCSV(fileName:str,data:list[list],subject_nums:int) -> bool:
    fileName += ".csv"
    subjects = [f'科目{i+1}' for i in range(subject_nums)]
    fields = ['姓名']
    fields.extend(subjects)
    with open(fileName,mode='w',encoding='utf-8',newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(data)
        except:
            return False
        else:
            return True
