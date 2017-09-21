#!/bin/bash

#==============imports================

import io
import os
import sys
import base64


def main():
	print "Encrypt__&&__Decrypt"
	print "1 : Encrypt"
	print "2 : Decrypt"
	test=raw_input("Select The Option :~$ ")
	type(test)
	if(test=="1"):
		#getValues=raw_input("Enter value : \n")
		#type(getValues)
		#print "\n\t Result : "+getValues+" \n\t Loading...."
		#strs=len(getValues)
		
		#print "\t Length:",strs
	
		#lst=list(getValues)
		#print "\t List vale ",lst

		#for x in lst:
		#	print "\t \t",x
		#print "\t process complete !..."


		encrypt=raw_input("Enter Value fro  encryption :")
		type(encrypt)

		enprnt=base64.b64encode(encrypt)

		print "encryption code is :",enprnt
		print "\n"
		os.system('pause')


		#====================================else condition===================
	elif(test=="2"):
			
			print "Decrypt"

			decrypt=raw_input("Enter Value For decryption : ")
			type(decrypt)

			deprnt=base64.b64decode(decrypt)

			print "decryption code is",deprnt
			print "\n"
			os.system('pause')

	else:
		#os.system('T')
		
		print"Your Terminated !"
		sys.exit()



	
if __name__ == '__main__':
	main()