'''
	Using Tkinter InBuilt Library Developed a Calculator 
	
'''
# -*- coding:utf-8 -*-
from Tkinter import *
import math
import re

class Calculator:
	def __init__(self,master):
		self.master = master
		master.title("Calculator using Tkinter")
		master.configure(background='black')
		master.resizable(False, False)
		# Create a Screen Widget
		self.screen = Text(master, state='disable', width=30, height = 4, background = 'silver',foreground = 'black',font=10)
		
		# Position Screen in Window
		self.screen.grid(row=0,column=0,columnspan=4, padx=5,pady=5)
		self.screen.configure(state='normal')
		
		#initialize screen value as empty
		self.equation = ''
		
		# Using Method creating different Buttons
		b1 = self.createButton(7)
		b2 = self.createButton(8)
		b3 = self.createButton(9)
		b4 = self.createButton(u"\u232B",None)
		b5 = self.createButton(4)
		b6 = self.createButton(5)
		b7 = self.createButton(6)
		b8 = self.createButton(u"\u00F7")
		b9 = self.createButton(1)
		b10 = self.createButton(2)
		b11 = self.createButton(3)
		b12 = self.createButton('*')
		b13 = self.createButton('.')
		b14 = self.createButton(0)
		b15 = self.createButton('+')
		b16 = self.createButton('-')
		b17 = self.createButton('=',None)
		b18 = self.createButton('%')
		b19 = self.createButton('^')
		b20 = self.createButton(u"\u221A")

		
		# Store all buttons in List
		buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]
		
		count = 0
		# Arrange Button with Grid Manager
		for row in range(1,6):
			for column in range(4):
				buttons[count].grid(row=row,column=column)
				count += 1
		
	# Create a Button
	def createButton(self,val,write=True,width=7,borderwidth=5,relief="raised",padx=2,pady=2):
		return Button(self.master,text=val,command=lambda:self.click(val,write),width=width,padx=padx,pady=pady,borderwidth=5,relief="raised")

	# Click Function to Perform Operations according to User Selection
	def click(self,text,write):
		if write == None:
			if text == "=" and self.equation:
				if u"\u221A".encode('utf-8') in self.equation:
					pass # Need to Code for Square Root of Equation
				else:
					self.equation = re.sub(u"\u00F7".encode('utf-8'),"/",self.equation)
					self.equation = self.equation.replace('^','**')
					answer = str(eval(self.equation))
				self.clear_screen()
				self.insert_screen(answer,newline=True)	
			elif text == u"\u232B":
				self.clear_screen()
		else:
			self.insert_screen(text)
			
	def insert_screen(self,value,newline=False):
		self.screen.configure(state='normal')
		self.screen.insert(END,value)
		if value in [u"\u00F7",u"\u221A"]:
			value = value.encode('utf-8')		# Without Encoding throwing UnicodeEncodeError 
		self.equation += str(value)
		self.screen.configure(state ='disabled')
	
	def clear_screen(self):
		self.equation = ''
		self.screen.configure(state='normal')
		self.screen.delete('1.0', END)
					
root = Tk()
gui = Calculator(root)
root.mainloop()
