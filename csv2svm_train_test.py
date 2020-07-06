```
#!/usr/bin/env python
"""
    csv file to svm format
    each 10 samples fetch 3 samples for test and the rest for train
    csv format:
        label, fea1, fea2, ...
    svm format:
        label 0:fea1 1:fea2 ...
    --- 
    parameters: 
        infile(csv format with no head and index)
    --- 
    example:
        python trans2svm_train_test.py test.csv
        out: test.csv.trainSvm, test.csv.testSvm
"""
import os
import sys

if len(sys.argv) != 1:
    print("USAGE: " + sys.argv[0] + "infile")
    sys.exit(1)

infile = sys.argv[1]
trainSvm = infile + ".trainSvm"
testSvm = infile + ".testSvm"
rate = 0.3

# if svm file exists, delete it
if os.path.exists(trainSvm):
    os.remove(trainSvm)
if os.path.exists(testSvm):
    os.remove(testSvm)

count = 0
with open(infile, 'r') as fin:
    with open(trainSvm, 'w+') as ftrain:
        with open(testSvm, 'w+') as ftest:
            for line in fin:
                line = line.strip().split(',')
                if (count % 10) < (rate * 10):
                    newline = str(line[0])
                    for i in range(1, len(line)):
                        newline += (" " + str(i-1) + ":" + str(line[i]))
                    ftest.write(newline + "\n")
                else:
                    newline = str(line[0])
                    for i in range(1, len(line)):
                        newline += (" " + str(i-1) + ":" + str(line[i]))
                    ftrain.write(newline + "\n")
                count += 1
```
