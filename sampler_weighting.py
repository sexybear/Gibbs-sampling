from __future__ import division
import random

DNA_list = [] 
item_set = [] 
maxscore = 0 
motif = []
num = 0
st = 0
k = 0

def read_DNA(filename):
        global DNA_list 
        file_DNA = open(filename)
        stop = "\n"
        while 1:
                line = file_DNA.readline()
                if not line:
                        break
                DNA_list.append(line[:-1])

def count_math():
        global DNA_list
        global item_set
        global maxscore
        global motif
        global num
        global st
        global k
        global ci

        p_dic_count = {}

        h = 0
        for seq in DNA_list:
                p_dic_count[h] = {}
                h = h+1

        for h in range(0,12):
                for item in item_set:
                        p_dic_count[h][item] = []
        #print p_dic_count
        h = 0
        for seq in DNA_list:
                for item in seq:
                                p_dic_count[h][item].append(item)
                h = h + 1

        p_dic_tf = {}
        
        for key in p_dic_count.keys():
                p_dic_tf[key] = {}
                for item in p_dic_count[key].keys():
                        p_dic_tf[key][item] = float(len(p_dic_count[key][item])/len(DNA_list[0]))

        #print p_dic_tf
        if num > len(DNA_list[0]):
                l = random.randint(0,len(DNA_list)-1)
        else:
                while(1):
                        l = random.randint(0,len(DNA_list)-1)
                        if l != num:
                                break
                        else:
                                l = random.randint(0,len(DNA_list)-1)
        start_dic = {}
        start_dic[num] = st

        print "----------------"
        print ci
        print "num:  %d"%num
        print "position  %d"%st
        print "----------------"

        h = 0
        while h < len(DNA_list):
                if h != num:
                        start_dic[h] = random.randint(0,len(DNA_list[0])-k)
                h = h + 1

        profile = []

        h = 0
        for item in DNA_list:
                if h != l:
                        profile.append(item[start_dic[h]:(start_dic[h] + k)])
                h = h+1
        p_dic = {}
        for item in item_set:
                p_dic[item] = [float(0)] * k

        for seq in profile:
                h = 0
                for item in seq:
                        p_dic[item][h] = p_dic[item][h] + p_dic_tf[h][item]
                        h = h+1

        print p_dic
        p_dic_result = {}
        for item in item_set:
                p_dic_result[item] = []

        
        for i in p_dic.keys():
                for item in p_dic[i]:
                        item = float(item/(len(DNA_list)-1))
                        item_final = "%.3f"%item
                        p_dic_result[i].append(item_final)


        result_list = []
        for i in range(0,len(DNA_list[0])-k-1):
                list_back = DNA_list[l][i:i+k]

                o = 0
                result = 1.0
                for h in list_back:
                        result = result*float(p_dic_result[h][o])
                        o = o+1
                result_final = "%.6f"%result
                result_list.append(result_final)
        num = l
        h = max(result_list)
        st = result_list.index(h)
        mo = DNA_list[l][st:st+k]
        if h > maxscore:
                maxscore = h
                motif = mo

if __name__ == "__main__":

        filename = "DNA.txt"
        read_DNA(filename)
        print DNA_list
        item_set = set([item for DNA_seq in DNA_list for item in DNA_seq])
        print item_set

        k = 7
        ci = 0

        for i in range(0,100):
                count_math()
                ci = ci + 1
        print "maxscore:"
        print maxscore
        print "motif:"
        print motif
                
        
