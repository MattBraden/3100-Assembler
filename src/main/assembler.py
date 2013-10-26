'''
Created on Oct 21, 2013

@author: Matt Braden
'''
import re
class Assembler:

    outputFile = ""
    def __init__(self):
        # I need to learn more about python
        pass
    
    def assembler(self, file):
        # Open File
        # NOTE: This should be a parameter on the command line?
        # FUCK THAT lets turn it into a webapp :)
        # But later...
        
        file = "" 
        #file = open('C:\Users\MattBeast\assembly.txt', 'r')

        # Check if it matches one of the forms
        #     INST R#, R#, R#        R Format
        #     INST R#, R#, IMMED     Store/Load
        #     INST R#, R#            Branch
        
        error = 0
        lineNumber = 0
        for instructionLine in file:
            # Check if last line
            lineNumber += 1
            newInstructionLine = self.processLine(instructionLine)
            # Append to new file
        # Always close file
        #file.close()
        
        # Output to new file

    def convertToBinary(self, number, digits):  
        # Thanks stackoverflow :)
        # Doesn't work for negatives
        # NOTE: Lambda is an anonymous function
        getBin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
        binary = getBin(number, digits) 
         
        return binary

    
    def processLine(self, line):
        # List of definitions
        # Operation Codes
        rformat = "000000"
        load    = "000001"
        store   = "000010"
        branch  = "000011"
        
        # Function Codes
        andCode = "000000"
        orCode  = "000001"
        add     = "000010"
        sub     = "000100"
        
        # Different sections of instruction
        opCode    = ""      # Bits 31-26
        regRs     = ""      # Bits 25-21
        regRt     = ""      # Bits 20-16
        regRd     = ""      # Bits 15-11
        immediate = ""      # Bits 15-0
        dontCare  = "00000" # Bits 10-6
        functCode = ""      # Bits 5-0

        # Matches R Format
        match = re.search(r'(?P<functCode>add|sub|and|or)\s*r(?P<regRd>\d+)\s*,\s*r(?P<regRs>\d+)\s*,\s*r(?P<regRt>\d+)', line, re.IGNORECASE)
        if match:
            opCode = rformat

            # I think this should be self .....
            # This isn't good for unit testing
            regRs = Assembler.convertToBinary(self, int(match.group('regRs')), 5)
            regRt = Assembler.convertToBinary(self, int(match.group('regRt')), 5)
            regRd = Assembler.convertToBinary(self, int(match.group('regRd')), 5)
            
            # Python doesn't have cases :(
            if (match.group('functCode').lower() == 'and'):
                functCode = andCode 
            elif (match.group('functCode').lower() == 'or'):
                functCode = orCode
            elif (match.group('functCode').lower() == 'add'):
                functCode = add
            elif (match.group('functCode').lower() == 'sub'):
                functCode = sub
       
        # Matches Load/Store 
        match = re.search(r'(?P<opCode>lw|sw)\s*r(?P<regRt>\d+)\s*,\s*r(?P<regRs>\d+)\s*\((?P<immediate>\d+)\)', line, re.IGNORECASE)
        if match:
            if (match.group('opCode').lower() == 'lw'):
                opCode = load
            elif (match.group('opCode').lower() == 'sw'):
                opCode = store

            regRs = Assembler.convertToBinary(self, int(match.group('regRs')), 5)
            regRt = Assembler.convertToBinary(self, int(match.group('regRt')), 5)
            immediate = Assembler.convertToBinary(self, int(match.group('immediate')), 16)

        # Matches Branch
        match = re.search(r'(?P<opCode>beq)\s*r(?P<regRs>\d+)\s*,\s*r(?P<regRt>\d+)\s*,\s*(?P<immediate>\d+)', line, re.IGNORECASE)
        if match:
            opCode = branch
            regRs = Assembler.convertToBinary(self, int(match.group('regRs')), 5)
            regRt = Assembler.convertToBinary(self, int(match.group('regRt')), 5)
            immediate = Assembler.convertToBinary(self, int(match.group('immediate')), 16)

        # Matches Comment
        # What happens when you put a comment at the end of an instruction?
        match = re.search(r'^//', line)
        if match:
            return line
        
        # Return the formatted instruction
        if (opCode == rformat):
            return opCode + regRs + regRt + regRd + dontCare + functCode
        elif (opCode == load or opCode == store or opCode == branch):
            return opCode + regRs + regRt + immediate
        else:
            return "error"
        '''
      
        # Blank line 
        match = re.match(r'^\s+$', line) 
        if match:
       
        # Comment 
        match = re.match(r'^//', line)
        if match:
        
        # Check if last line?
        # ERROR: Doesn't match
       ''' 