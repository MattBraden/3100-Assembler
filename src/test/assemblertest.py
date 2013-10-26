'''
Created on Oct 22, 2013

@author: Matt
'''
import unittest
from main.assembler import Assembler

class AssemblerTest(unittest.TestCase):
    
    def testConvertToBinary(self):
        assembler = Assembler

        binary = assembler.convertToBinary(self, number=10, digits=5)
        self.assertEqual(binary, "01010", "Convert to Binary")

    def testProcessLine(self):
        assembler = Assembler

        # This is sort of an integration test
        line = "and r0, r1, r1"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00000000001000010000000000000000", "Convert to AND Instruction") 

        line = "or r5, r2, r3"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00000000010000110010100000000001", "Convert to OR Instruction") 

        line = "add r1, r1, r1"  
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00000000001000010000100000000010", "Convert to ADD Instruction")
        
        line = "sub r0, r1, r2"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00000000001000100000000000000100", "Convert to SUB Instruction")
       
        line = "lw r3, r1(2)"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00000100001000110000000000000010", "Convert to LW Instruction")
        
        line = "sw r2, r1(2)"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00001000001000100000000000000010", "Convert to SW Instruction")
        
        line = "beq r3, r1, 2"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "00001100011000010000000000000010", "Convert to BEQ Instruction")
        
        line = "// This is a comment"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "// This is a comment", "Comments are allowed")
        
        line = "This would be an error"
        newLine = assembler.processLine(self, line=line)
        self.assertEqual(newLine, "error", "Random text is an error")
        
    def testAssembler(self):
        assembler = Assembler
       
        # This is more of an intergration test 
        # How to pass in file?
         
        