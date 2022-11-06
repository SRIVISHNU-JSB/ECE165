#Identify number of vowels in the string

vowels = 'aeiou'

string = "Why is the media here so negative? Why are we in India so embarrassed to recognize our own strengths, our achievements? We are such a great nation. We have so many amazing success stories but we refuse to acknowledge them. Why?” President Abdul Kalam had said in one of his best speeches delivered at Indian Institute of Technology, Hyderabad."

def Check_Vowel(string, vowels):
    string = string.casefold()

    a = e = i = o = u = 0

    for char in string:
        if char in vowels:
            if char=='a':
                a += 1
            elif char=='e':
                e += 1
            elif char=='i':
                i += 1
            elif char=='o':
                o += 1
            elif char=='u':
                u += 1
                
    print('Number of vowels in the given string:',a+e+i+o+u)
    print('Vowel figures found:','a:',a,'e:',e,'i:',i,'o:',o,'u:',u)
    maximum_citation=max(a,e,i,o,u)
    print('Vowel with highest citation:',maximum_citation)
    
    for value in [a,e,i,o,u]:
        if value==maximum_citation:
            print

Check_Vowel(string, vowels)

# user_string=input("Enter a string: ")
# Check_Vowel(user_string, vowels)