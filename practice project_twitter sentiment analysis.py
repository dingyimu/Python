#Project name: Twitter data sentiment analysis practive
#project brief description:Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(x):
    for i in punctuation_chars:
        x=x.replace(i,'')
    return x
def get_pos(w):
    w=w.split()
    newlist=[]
    for i in w:
        z=strip_punctuation(i)
        z=z.lower()
        newlist.append(z)
    time=0
    for i in newlist:
        if i in positive_words:
            time+=1
    return time


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
         

def get_neg(n):
    n=n.split()
    newlist=[]
    for i in n:
        z=strip_punctuation(i)
        z=z.lower()
        newlist.append(z)
    timeneg=0
    for i in newlist:
        if i in negative_words:
            timeneg+=1
    return timeneg

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
file= open("project_twitter_data.csv") 
export = open("resulting_data.csv", "w")
export.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')

Lines = file.readlines() 

for lin in Lines[1:]:
    #print(lin)
    lin=lin.replace("\n","")
    linnum=lin.split(',')
    export.write('{}, {}, {}, {}, {} \n'.format(linnum[-2],linnum[-1],get_pos(lin), get_neg(lin), get_pos(lin)-get_neg(lin)))
export.close    