x=int(input("Enter Internal Marks: "))
y=int(input("Enter External Marks: "))
if x>100:
	print("Invalid Value")
elif y>100:
	print("Invalid Value")
elif x<0:
	print("Invalid Value")
elif y<0:
	print("Invalid Value")
else:		
	ass=x*60/100
	ext=y*40/100
	total=ass+ext
	total=round(total)
	if y<40:
		print("Your mark is "+str(total)+" You are FAIL!")
	else:	
		if total>=75:
			print("Your mark is "+str(total)+" You got DISTINTION!")
		elif total>=65:
			print("Your mark is "+str(total)+" You got MERIT!")
		elif total>=50:
			print("Your mark is "+str(total)+" You got PASS!")
		else:
			print("Your mark is "+str(total)+" You are FAIL!")		