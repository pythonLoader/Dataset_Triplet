import numpy as np
import subprocess

def all_triplet_generator(taxa_list):
    l=len(taxa_list)
    no_of_triplets=(l*(l-1)*(l-2))/6
    no_of_triplets.is_integer()
    print(no_of_triplets)
    used = 0
    list3=[]

    for i in range(0,l-2):

        # print(taxa_list[i])
        pointer1=i
        elem = taxon_list[pointer1]
        for j in range(1,l-used-1):
            pointer2 = pointer1+j
            elem += taxa_list[pointer2]
            # print("Upto 2nd elem-> " + elem)
            # list3.append(taxa_list[pointer2])
            for k in range (1, l-pointer2):
                pointer3 = pointer2+k
                elem += taxa_list[pointer3]
                print(elem)
                list3.append(elem)
                elem = elem[0:2]

            elem = elem[0]
        elem = ""
        used = used + 1

    print(len(list3))
    return list3


def triplet_maker(str):
    triplet = []
    str1 = '(' + str[0] + ',' + '(' + str[1] + ',' + str[2] + ')' + ')'
    str2 = '(' + str[1] + ',' + '(' + str[0] + ',' + str[2] + ')' + ')'
    str3 = '(' + str[2] + ',' + '(' + str[0] + ',' + str[1] + ')' + ')'
    triplet.append(str1)
    triplet.append(str2)
    triplet.append(str3)
    #print(triplet)
    return


def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def 

fl = open("input.txt","r+")

tokenized = read_by_tokens(fl)

n = next(tokenized)
n = int(n)
print(f'The number of tokens is: {n}')
taxon_list = []

for i in range(1,n+1):
    taxon_list.append(next(tokenized))

l = len(taxon_list)

trip_list = all_triplet_generator(taxon_list)
for x in trip_list:
    triplet_maker(x)

no_of_three_taxa_seq=(l*(l-1)*(l-2))/6
no_of_three_taxa_seq=int(no_of_three_taxa_seq)
no_of_gene_trees = int(next(tokenized))
no_of_triplets_in_each_taxa_seq = 3

print(taxon_list)

gene_trees = []
for i in range(0,no_of_gene_trees):
    gene_trees.append(next(tokenized))

mat = np.zeros((no_of_gene_trees,no_of_three_taxa_seq,no_of_triplets_in_each_taxa_seq))

gene_tree_triplets = []
gene_trees_map = {}


for gene_tree in gene_trees:
    print("Working with the tree " + gene_tree)
    with open("Tree_Input.tree", "w+") as f:
        f.write(gene_tree)
    subprocess.call(['./triplet-encoding-controller.sh','Tree_Input.tree','output.trip'])
    with open("output.trip", "r") as f2:
        data = f2.read()
    print(data)
    # data = f.read()
    # f.seek(0)
    # f.write(output)
    # f.truncate()

#subprocess.call(['./triplet-encoding-controller.sh','Tree_Input.tree','output.trip'])

'''

'''



#print(mat)
