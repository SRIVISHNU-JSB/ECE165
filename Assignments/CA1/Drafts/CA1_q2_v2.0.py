##WAP to find out the vowels in the string and dig out 
def Check_Vow(string, vowels):
    
    # The term "casefold" has been used to refer to a method of ignoring cases.
    
#   string = string.casefold()
    string = string.casefold()
    
    count = {}.fromkeys(vowels, 0)
    
    # To count the vowels
    for character in string:
        
        if character in count:
            
            count[character] += 1
            
    return count

# Driver Code

vowels = 'aeiou'

string = "Why is the media here so negative? Why are we in India so embarrassed to recognize our own strengths, our achievements? We are such a great nation. We have so many amazing success stories but we refuse to acknowledge them. Why?” President Abdul Kalam had said in one of his best speeches delivered at Indian Institute of Technology, Hyderabad."

# print (Check_Vow(string, vowels))

for i in string:
    print(i)
    

# user_string=input("Enter a string: ")

# print(Check_Vow(user_string, vowels))