#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
  a.append(s)
  s = raw_input()
i = input()
p = a[i]
j = a[i]
while j < len(a):
  if int(a[j]) < int(a[p]):
    p = j
  j = j + 1
print p
