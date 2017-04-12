#!/usr/bin/env python
#coding=utf-8

import sys

class Combine:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.dic1 = {}
        self.dic2 = {}
        self.dic3 = {}

    def doCombine(self):
        f1 = open(self.file1, 'r')
        while True:
            line1 = f1.readline()
            if len(line1) == 0:
                break;
            else:
                pos = line1.find(':')
                user_ = line1[:pos]
                hash_ = line1[pos+1:]
                self.dic1[user_] = hash_
        #print str(self.table1)
        f1.close()
        
        f2 = open(self.file2, 'r')
        while True:
            line2 = f2.readline()
            
            if len(line2) == 0:
                break;
            else:
                pos2 = line2.find(':')
                user2_ = line2[:pos2]
                hash2_ = line2[pos2+1:]
                self.dic2[user2_] = hash2_
        #print str(self.table2)
        f2.close()
        
        for key, value in self.dic1.items():
            #print key, 'corresponds to', value
            if self.dic2.has_key(key):
                hash_combine = value.replace("\n", "") + ':' + self.dic2[key]
                self.dic3[key] = hash_combine
            else:
                self.dic3[key] = value
                
        for key, value in self.dic2.items():
            if not self.dic3.has_key(key):
                self.dic3[key] = value
        
        for key, value in self.dic3.items():
            if not value.endswith('\n'):
                self.dic3[key] =  value + "\n"
                
        #print str(self.dic3)
        f3 = open("combine.txt", 'w')
        for key, value in self.dic3.items():
            f3.write(key+':'+value)
            
        f3.close() 
        
        
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print "usage: combine.py lm.txt nt.txt"
    else:
        Combine(sys.argv[1], sys.argv[2]).doCombine();
        print "combine finished!"
