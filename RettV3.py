import os, re
import matplotlib.pyplot as plt

TitleMotif = re.compile(r'(\w){1,}_1') #regular expression that can extract the gene titles from the sequence file
FOXO3Motif = re.compile(r'TGTTT')
MP = os.path.join('/','home','edward','canopy','scripts','Rett V2','MP.txt')
Text = open(MP) # opens the sequence file as a file object
Sequences = Text.read() # turns that file object into a readable script
Genes = Sequences.split('>') # splits the script at every '>', creating a list where each object is a full, individual gene sequence (a chunk)

for x in Genes: #gets rid of any newline characters that would confound future analysis
    x.replace('\n','')    
    
GH =  {}

for x in range(len(Genes)):
    Label = TitleMotif.search(Genes[x])
   # GeneHitDictionary = {} 
    if Label != None:
        Title = Label.group() #looks in each chunk for the Gene ID, and assings that ID to Title.
        MoMouse = FOXO3Motif.findall(Genes[x]) #searches each chunk for the motif and adds each hit to a tuple called MoMouse. len(MoMouse) = # of hits
       # GeneHitDictionary.setdefault(Title,len(MoMouse)) #Adds each Title - # of hits combo to a dictionary
        GH[Title] = len(MoMouse) # more efficient way, that preserves data even once the loop closes

ct_0 = 0
ct_1 = 0
ct_2 = 0
ct_3 = 0
ct_4 = 0
ct_5 = 0
ct_6 = 0
ct_7 = 0


'''for k,v in GH.items():
    if v == 0:
        ct_0 += 1
    if v == 1:
        ct_1 += 1
    if v == 2:
        ct_2 += 1
    if v == 3:
        ct_3 += 1
    if v == 4:
        ct_4 += 1
    if v == 5:
        ct_5 += 1
    if v == 6:
        ct_6 += 1
    if v ==7:
        ct_7 += 1'''

ct = {}

for k,v in GH.items():
   # ct.setdefault(v,1)
    #ct[v] += 1
    if v not in ct:
        ct[v] = 0
    if v in ct:
        ct[v] += 1
    if v == 22:
        print(k)

print(ct)
        
# investigate OG paper, see if everything matches up
# cat seqs | program name

'''print(ct_0)
print(ct_1)
print(ct_2)
print(ct_3)
print(ct_4)   
print(ct_5)    #print(k + ' ' + str(v))
print(ct_6)
print(ct_7)

#print('Gene Name: ' + Title + ' ' + 'Number of Hits: ' + str(len(MoMouse)))

#Try to get in order of frequency of hits.
#Try and graph it.
# numpy, matplotlib'''