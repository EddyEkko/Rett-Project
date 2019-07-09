# Rett-Project
import re, os
HDAC3Motif = re.compile(r'TGT')
MouseFile = os.path.join('/','home','edward','canopy','scripts','Rett Project','MousePromoterFastq.txt')
MousePromoters = open(MouseFile)
HitCount = MousePromoters.read()
MoMouse = HDAC3Motif.findall(HitCount)
print('Number of Matches: ' + str(len(MoMouse)))

Promoters = []

def ExtractHit(x):
    for i in range(len(x)):
        text = x[i:i+609] #divides the documeent into chunks exactly one complete sequence long. 
        chunk = text.replace('\n','') #removes any newline characters in the chunks.
        if chunk.isalpha(): #eliminates chunks that contain anything other than base pairs.
            if HDAC3Motif.search(chunk): #searches remaining chunks for the motif.
                global Promoters 
                Promoters += [chunk] #if it matches, this adds that chunk to Promoter list.
        
ExtractHit(HitCount)
print(len(Promoters))
print(Promoters[1])
