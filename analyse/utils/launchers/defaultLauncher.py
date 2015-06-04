#!/usr/bin/env python
import os
import sys

fileProcesses = '$fileProcesses$'
nProcessors   = $nProcessors$
launcher      = '$launcher$'
interpretor   = '$interpretor$'

f             = open(fileProcesses, 'r')
lines         = f.readlines()
f.close()

header        = lines.pop(0).replace('\n','')
argsNames     = header.split('\t')

currentNTask  = 0
processesPID  = {}

print('$startString$')

for line in lines:

    if (currentNTask == nProcessors):
        (oldpid, exitStatus) = os.wait()

        for i in processesPID:
            if processesPID[i] == oldpid:
                processusNbr = i
                break

    else:
        currentNTask += 1
        processusNbr  = currentNTask
        
    pid = os.fork()
    if (pid > 0):
        processesPID[processusNbr] = pid
        
    if (pid == 0):
        args    = line.replace('\n','').split('\t')
        command = interpretor + ' ' + launcher
        for (argName, arg) in zip(argsNames, args):
            command += ' ' + argName + '=' + arg

        command += ' >> $logFile$'+str(processusNbr) 

        print command
        sys.exit(os.system(command))
        
for i in xrange(currentNTask):
    os.wait()

