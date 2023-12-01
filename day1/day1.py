
#
#
import os
total=0
data=open('input','r')
for line in data:
    print(line)
    line=line.replace('one','o1e')
    line=line.replace('two','t2o')
    line=line.replace('three','t3e')
    line=line.replace('four','f4r')
    line=line.replace('five','f5e')
    line=line.replace('six','s6x')
    line=line.replace('seven','s7n')
    line=line.replace('eight','e8t')
    line=line.replace('nine','n9e')
    print(line)
    num_list=[]
    line_num='0'
    for char in line:
      if char.isdigit() :
         num_list.append(char)
    line_num=num_list[0] + num_list[-1]
    total+=int(line_num)
    print(line_num)
    print(total)

print(total) 