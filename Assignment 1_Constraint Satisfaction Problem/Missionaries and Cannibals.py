print("\tGame Start\nNow the task is to move all of them to right side of the river") 
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board") 
left_M = 3		  
left_C = 3		  
right_M=0		  
right_C=0		  
userM = 0	 
userC = 0	 
k = 0
print("\nM M M C C C |	 --- | \n") 
try: 
	while(True): 
		while(True): 
			print("Left side -> right side river travel") 
			uM = int(input("Enter number of Missionaries travel => "))	 
			uC = int(input("Enter number of Cannibals travel => ")) 

			if((uM==0)and(uC==0)): 
				print("Empty travel not possible") 
				print("Re-enter : ") 
			elif(((uM+uC) <= 2)and((left_M-uM)>=0)and((left_C-uC)>=0)): 
				break
			else: 
				print("Wrong input re-enter : ") 
		left_M = (left_M-uM) 
		left_C = (left_C-uC) 
		right_M += uM 
		right_C += uC 

		print("\n") 
		for i in range(0,left_M): 
			print("M ",end="") 
		for i in range(0,left_C): 
			print("C ",end="") 
		print("| --> | ",end="") 
		for i in range(0,right_M): 
			print("M ",end="") 
		for i in range(0,right_C): 
			print("C ",end="") 
		print("\n") 

		k +=1

		if(((left_C==3)and (left_M == 1))or((left_C==3)and(left_M==2))or((left_C==2)and(left_M==1))or((right_C==3)and (right_M == 1))or((right_C==3)and(right_M==2))or((right_C==2)and(right_M==1))): 
			print("Cannibals eat missionaries:\nYou lost the game") 

			break

		if((right_M+right_C) == 6): 
			print("You won the game : \n\tCongrats") 
			print("Total attempt") 
			print(k) 
			break
		while(True): 
			print("Right side -> Left side river travel") 
			userM = int(input("Enter number of Missionaries travel => ")) 
			userC = int(input("Enter number of Cannibals travel => ")) 
			
			if((userM==0)and(userC==0)): 
					print("Empty travel not possible") 
					print("Re-enter : ") 
			elif(((userM+userC) <= 2)and((right_M-userM)>=0)and((right_C-userC)>=0)): 
				break
			else: 
				print("Wrong input re-enter : ") 
		left_M += userM 
		left_C += userC 
		right_M -= userM 
		right_C -= userC 

		k +=1
		print("\n") 
		for i in range(0,left_M): 
			print("M ",end="") 
		for i in range(0,left_C): 
			print("C ",end="") 
		print("| <-- | ",end="") 
		for i in range(0,right_M): 
			print("M ",end="") 
		for i in range(0,right_C): 
			print("C ",end="") 
		print("\n") 

	

		if(((left_C==3)and (left_M == 1))or((left_C==3)and(left_M==2))or((left_C==2)and(left_M==1))or((right_C==3)and (right_M == 1))or((right_C==3)and(right_M==2))or((right_C==2)and(right_M==1))): 
			print("Cannibals eat missionaries:\nYou lost the game") 
			break
except EOFError as e: 
	print("\nInvalid input please retry !!")
