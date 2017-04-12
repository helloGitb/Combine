1#!/usr/bin/env python
#coding=utf-8

import sys

class Combine:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.dic1 = {}
        self.dic2 = {}

    def doCombine(self):
        f = open(self.file1, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break;
            else:
                pos = line.find(':')
                user_ = line[:pos]
                hash_ = line[pos+1:]
                self.dic1[user_] = hash_
        #print str(self.dic1)
        f.close()
        
        f = open(self.file2, 'r')
        while True:
            line = f.readline()
            
            if len(line) == 0:
                break;
            else:
                pos = line.find(':')
                user_ = line[:pos]
                hash_ = line[pos+1:]
                self.dic2[user_] = hash_
        #print str(self.dic2)
        f.close()
        
        for key, value in self.dic1.items():
            #print key, 'corresponds to', value
            if self.dic2.has_key(key):
                hash_combine = value.replace("\n", "") + ':' + self.dic2[key]
                self.dic1[key] = hash_combine
        
        for key, value in self.dic2.items():
            if not self.dic1.has_key(key):
                self.dic1[key] = value
        
        for key, value in self.dic1.items():
            if not value.endswith('\n'):
                self.dic1[key] =  value + "\n"
                
        #print str(self.dic3)
        f = open("combine.txt", 'w')
        for key, value in self.dic1.items():
            f.write(key+':'+value)
            
        f.close() 
        
        
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print "usage: combine.py lm.txt nt.txt"
    else:
        Combine(sys.argv[1], sys.argv[2]).doCombine();
        print "combine finished!"
