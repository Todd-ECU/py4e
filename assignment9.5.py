'''
9.4 Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of
those lines as the person who sent the mail. The program creates
a Python dictionary that maps the sender's mail address to a count
of the number of times they appear in the file.
After the dictionary is produced, the program reads through
the dictionary using a maximum loop to find the most prolific committer.
Desired Output
--cwen@iupui.edu 5--
'''


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
freq = {}
mosfreq = 0
moskey = None

for line in fh:
   line = line.split()
   if "From" in line:    
       emails = line[1]
       freq[emails] = freq.get(emails, 0) + 1
       #print (emails) 

for key in freq:
    if freq[key] > mosfreq:
        moskey = key
        mosfreq = freq[key]

      
print(moskey,mosfreq) 

        
       
