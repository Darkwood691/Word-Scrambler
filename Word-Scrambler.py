from tkinter.filedialog import askopenfilename
import random
filename = askopenfilename(filetypes=[("Text files","*.txt")])
array=[]
if filename != None:
    with open(filename,"r") as file:
        content=file.read()
        lines = content.split("\n")
        for line in lines:
            words=line.split(" ")
            for word in words:
                length=len(word)
                nWord=[]
                blackList=[]
                letCount=0
                punctuation=None
                for letter in word:
                    if letter=="," or letter=="." or letter=="!" or letter=="?" or letter==";":
                        length-=1
                        word=word[:-1]
                        punctuation=letter
                
                for n in range(length):
                    nWord.append("_")
                    
                for letter in word:
                    unique=False
                    flag=0
                    if letCount==0:
                        nWord[0]=letter
                    elif letCount==(length-1):
                        nWord[length-1]=letter
                    else:
                        while unique==False:
                            x=random.randint(1,(length-2))
                            flag = 0
                            for number in blackList:
                                if x==number:
                                    flag+=1
                            if flag>0:
                                unique=False
                            else:
                                unique=True
                                blackList.append(x)
                                nWord[x]=letter
                    letCount+=1
                if punctuation != None:
                    nWord.append(punctuation)
                    
                nWord=''.join(nWord)
                array.append(nWord)
array=' '.join(array)

with open("Scrambled.txt","w") as file:
    file.write(array)           
                            
                            