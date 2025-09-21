# file1 = open("C:\\Users\\Aadiladmani\\Downloads \\ict.txt")
# print(file1)

# f1 = open(r"C:\Users\Aadiladmani\OneDrive\Desktop\\ict.txt")
# # This will print every line one by one in the file
# for each in f1:
#     print (each)

# # Python code to illustrate read() mode
# f1 = open(r"C:\Users\Aadiladmani\OneDrive\Desktop\\ict.txt")
# print (f1.read())

# with open(r"C:\Users\Aadiladmani\OneDrive\Desktop\\ict.txt",'r') as f1:  
#     data = f1.read() 
# print(data)

# f1 = open(r"C:\Users\Aadiladmani\OneDrive\Desktop\\ict.txt")
# print (f1.read(5))

# with open(r"C:\Users\Aadiladmani\OneDrive\Desktop\\ict.txt",'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)

# file = open("ict1.txt",'w')
# file.write("ICT ICT ICT \n")
# file.write("ICT ICT ICT ICT ICT")
# file.close()

# with open("file.txt", "w") as f: 
#     f.write("Hello World!!!") 
#     f.close()

# file = open("ict1.txt",'a')
# file.write("\n Department Department")
# file.close()

# with open(r'C:\Users\Aadiladmani\OneDrive\Desktop\a.tif', 'rb') as file:
#     binary_data = file.read()

# import csv
# # Reading from a CSV file
# with open('data-1.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# Writing to a CSV file
import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Aansh', 'PWP', 9])
    writer.writerow(['Ashutosh', 'PWP', 10])
    file.close()
