#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 22:41:58 2017

@author: yadhu_krishnan
"""
#python program  to check existance of inverse (for every element) and identity element for a set Zn with addtion operation (modulo n) 
n=input("Enter a number") #Reads a number 'n'
print "Group elements are:"
for i in range (0,n):
    print(i),
for a in range (0,n):
    for b in range (0,n):
        c=a*b #Here operation is '*' in which the sign represent regular multiplication
        if(c%n==1):
            print '\ninverse of',a,'is',b
            flag=True
        else:
            flag=False
if(flag==True):
    print "Inverse exist and identity element is 1"
else:
    print "Inverse doesn't  exist"
        