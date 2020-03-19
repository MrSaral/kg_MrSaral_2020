import sys

def mapper(s1,s2):

	# Function to check for one-to-one mapping between
	# two strings.	
	#  	
	# Takes 2 strings as input and boolean output 

	if(not s1 or len(s1)<=1):
		# Boundary cases
		return True;

	d={}	# Dictionary
	for i in range(len(s1)):
		
		# Looping over all characters of first string

		c1=s1[i]
		c2=s2[i]

		if(d.has_key(c1)):
			if(d[c1]==c2):
				continue;
			else:
				return False;
		else:
			if (c2 not in d.values()):
				d[c1]=c2
	return True;




def main():
	# Driver function
	print (mapper(str(sys.argv[1]),str(sys.argv[2])))



if __name__ == "__main__":
    main()