import numpy as np
import subprocess


def all_triplet_generator(taxa_list):
    l=len(taxa_list)
    no_of_triplets=(l*(l-1)*(l-2))/6
    #no_of_triplets.is_integer()
    #print(no_of_triplets)
    used = 0
    list3=[]

    for i in range(0,l-2):

        # print(taxa_list[i])
        pointer1=i
        elem = taxa_list[pointer1]
        for j in range(1,l-used-1):
            pointer2 = pointer1+j
            elem += taxa_list[pointer2]
            # print("Upto 2nd elem-> " + elem)
            # list3.append(taxa_list[pointer2])
            for k in range (1, l-pointer2):
                pointer3 = pointer2+k
                elem += taxa_list[pointer3]
                #print(elem)
                list3.append(elem)
                elem = elem[0:2]

            elem = elem[0]
        elem = ""
        used = used + 1

    #print(len(list3))
    return list3




taxa_map={}
genetree_list=[]
fl = open("input.txt","r+")
while True:
    line = fl.readline().strip()
    if line == '':
        break
    else:
    	genetree_list.append(line) 
    	length=len(line)
    	for i in range (0,length):
    		if(line[i]!='(' and line[i]!= ')' and line[i]!=',' and line[i]!=';'):
    			if(line[i] not in taxa_map.keys()):
    				print(line[i])
    				taxa_map[line[i]]=1

#print(genetree_list)
three_taxa_sequence=all_triplet_generator(taxa_map.keys())
print('three_taxa_sequence: ')
print(three_taxa_sequence)
print('\n')

column_determinator={}
val=1
type_1=1
type_2=2
type_3=3
for each_seq in three_taxa_sequence:
	t1=each_seq[0]
	t2=each_seq[1]
	t3=each_seq[2]
	s1=t1+t2+t3
	s2=t1+t3+t2
	s3=t2+t1+t3
	s4=t2+t3+t1
	s5=t3+t1+t2
	s6=t3+t2+t1
	column_determinator[s1]=str(val)+','+str(type_1)
	column_determinator[s2]=str(val)+','+str(type_1)
	column_determinator[s3]=str(val)+','+str(type_2)
	column_determinator[s4]=str(val)+','+str(type_2)
	column_determinator[s5]=str(val)+','+str(type_3)
	column_determinator[s6]=str(val)+','+str(type_3)
	val+=1

no_of_gene_trees = len(genetree_list)
no_of_three_taxa_seq = len(three_taxa_sequence)

table = np.zeros((no_of_gene_trees,no_of_three_taxa_seq,3))

for index,gene_tree in enumerate(genetree_list):
    print("Working with the tree " + gene_tree)
    with open("Tree_Input.tree", "w+") as f:
        f.write(gene_tree)
    subprocess.call(['./triplet-encoding-controller.sh','Tree_Input.tree','output.trip'])
    with open("output.trip", "r") as f2:
        data = f2.read()
        lines=data.split("\n")
        no_of_lines=len(lines)
        #print("line: ")
    	#print(lines)
    	for i in range(0,no_of_lines-1):
    		triplet=lines[i][1]+lines[i][4]+lines[i][6]
    		if triplet in column_determinator.keys():
    			#print (str(index) + " " + column_determinator[triplet])

    			res = [x.strip() for x in column_determinator[triplet].split(',')]
    			axis_y = int(res[0])
    			axis_z = int(res[1])

    			table[index][axis_y-1][axis_z-1] = 1
    			#print(column_determinator[triplet][2])
    			#axis_y=int(column_determinator[triplet])
    			#axis_z=int(column_determinator[triplet][2])
    			#print(axis_y+axis_z)


print(table)
