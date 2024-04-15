#Import pathlib and shutil modules
import pathlib
import shutil 

#Create a path of cwd and print
path = pathlib.Path.cwd()
print(path)

#create a new path object named "folder_week11"
path2 = path/"folder_week11"
path2.mkdir(parents=True, exist_ok=True)

#create text file in that directory
file_path = path2/"week11.txt"
file_path.touch()

#write in that text file
file_path.write_text("Test: Writing to file.")

#open the text file and read it
week11 = path2/"week11.txt"
file = week11.open(mode='r', encoding='utf-8')
print(file.read())
file.close()

#Make a new path for the backups
path3 = path2/"file_backups"
path3.mkdir(parents=True, exist_ok=True)

#Using the shutil module, make copy of the week11.txt file
source_file = path2 / "week11.txt"
destination_file = path3 / "week11_backup.txt"
shutil.copy(source_file, destination_file)

#From the folder_week11 directory, use rglob() method to print out only the txt files
for txt_file in path2.rglob('*.txt'):
    print(txt_file)





