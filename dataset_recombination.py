import shutil
import random

random.seed(0)
def recombination(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        random.shuffle(lines)
        test_sa = random.sample(lines,len(lines)//10)
        train_sa = list(set(lines)-set(test_sa))
    with open('./train.txt','w') as f1:
        f1.writelines(train_sa)
    with open('./test.txt','w') as f2:
        f2.writelines(test_sa)
        # pass
        
def copy_files(file1,source_dir,dest_dir):
    with open(file1,'r+') as f1:
        names = f1.readlines()

    for i  in names:
        path1 = source_dir + i[:-1]+'.jpg'
        dest_path = source_dir + i[:-1]+'.jpg'
        shutil.copy(path1,dest_path)



if __name__=="__main__":
    # recombination(file_path)
    file1 = 