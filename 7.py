try:
    file1 = open('sample.txt', 'r+')
    print("Reading Text File:")
    rd=file1.readline()
    print("Line 1:",rd)
    rd2=file1.readline()
    print("Line 2:",rd2)
    file1.close()
except FileNotFoundError:
    print("Error: the file 'sample.txt' doesn't exist!")



