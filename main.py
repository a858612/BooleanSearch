
import pandas as pd
import sys

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()

    # Please implement your algorithm below
df = pd.read_csv(args.source,header=None)
df2 = pd.read_csv(args.query,header=None)
#data = pd.read_csv('output_list.txt', sep=" ", header=None)
orig_stdout = sys.stdout
f = open(args.output, 'w')
sys.stdout = f
#encoding=utf-8

#words = df2.iloc[7,0].split(' ')
#y = 0
PREVIOUS = 0 ##for comma
iszero = 1
for z in range(0, len(df2.index),1):
    words = df2.iloc[z,0].split(' ')
    if (words[0] == None):
        break
    for x in range(0, len(df.index),1):
        if pd.isnull(df.iloc[x,1]):
            break
        else:
            if len(words) > 1:
                if words[1] == 'or': ##search
                    for y in range(0, len(words),2):
                        if words[y] in str(df.iloc[x,1]):
                            if PREVIOUS == 1:
                                print(',',x+1,end='',sep='')
                            else:
                                iszero = 0
                                print(x+1,end='',sep='')
                                PREVIOUS = 1
                            break
                elif words[1] == 'and':
                    for y in range(0, len(words),2):
                        if words[y] in str(df.iloc[x,1]):
                            if y != len(words)-1:
                                continue
                            else:
                                if PREVIOUS == 1:
                                    print(',',x+1,end='',sep='')
                                else:
                                    iszero = 0
                                    print(x+1,end='',sep='')
                                    PREVIOUS = 1
                        else:
                            break;
                elif words[1] == 'not':
                    if words[0] not in str(df.iloc[x,1]):
                        continue
                    for y in range(2, len(words),2):
                        if words[y] not in str(df.iloc[x,1]):
                            if y != len(words)-1:
                                continue
                            else:
                                if PREVIOUS == 1:
                                    print(',',x+1,end='',sep='')
                                else:
                                    iszero = 0
                                    print(x+1,end='',sep='')
                                    PREVIOUS = 1
                        else:
                            break;
            else:  ##FIND THIS ONLY'''
                if words[0] in str(df.iloc[x,1]):
                    if PREVIOUS == 1:
                        print(',',x+1,end='',sep='')
                    else:
                        iszero = 0
                        print(x+1,end='',sep='')
                        PREVIOUS = 1
    if(iszero==1):
        print(0,end='',sep='')
    if z == len(df2.index)-1:
        break
    else:
        print('\n',end='',sep='')
        PREVIOUS = 0
        iszero = 1

sys.stdout = orig_stdout
f.close()



#import jieba
#sentence = df.iloc[2,1]
#print ("Input：", sentence)
#words = jieba.cut(sentence, cut_all=False)
#print ("Output 精確模式 Full Mode：")
#for word in words:
#    print (word)
