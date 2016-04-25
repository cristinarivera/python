#!/usr/bin/env python
#-*- coding: utf-8 -*-
print 'Programa para saber quién es más joven'

a= float(raw_input('Edad de una: '))
b= float(raw_input('Edad de la otra: '))

if a==b:
    print 'Ambas personas tienen la misma edad'
if a>b:
    print 'La primera persona es mayor'
if b>a:
    print 'La segunda persona es mayor.'