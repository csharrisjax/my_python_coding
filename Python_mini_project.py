# AWS Services Inventory Python Mini Project


# Create an empty list

my_list = []
print (my_list)

# Populate the list using append or insert

my_list.append('DynamoDB')
my_list.append('S3')
my_list.append('Lambda')
my_list.append('CloudFormation')
my_list.append('EC2')

#Print the list and the length of the list

print(my_list)
print (len(my_list))

# Remove two specific services from the list by name or by index

del my_list[1:3]


# Print the new list and the new length of the list

print (my_list)
print (len(my_list))
