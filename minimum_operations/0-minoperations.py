#!/usr/bin/python3

def minOperations(n):
	operations = 0
	result = "H"

	while len(result) < n:
		result += result
		operations += 1
	
	return result, operations

n = int(input("Enter the target length (n): "))

# Call the minOperations function with the user-provided value of 'n'
final_string, num_operations = minOperations(n)

# Check if the length of the final string is less than 'n' and return 0 if true
if len(final_string) < n:
    print("If n is impossible to achieve, return 0")
    print("Result is:", 0)
else:
    print("Final string: {}".format(final_string))
    print("Number of operations: {}".format(num_operations))
