from datasets import load_dataset
dataset_sem = load_dataset("sem_eval_2010_task_8", split = 'test')
print(dataset_sem)
print(dir(dataset_sem))
print(dataset_sem.data)
print(dir(dataset_sem.data))
print(len(dataset_sem.data))
print(dataset_sem.data[0])
print(dataset_sem.data[1])
print(dataset_sem.data[0][0])
import csv

with open('./data/test/dataset_csv.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = '|', lineterminator = '\n')
    for _ in range(len(dataset_sem.data[0])):
        csv_writer.writerow([dataset_sem.data[0][_], dataset_sem.data[1][_]])
