#Q4
Age= input('Q4\nWhat is your age?')
print('My age is', Age)
print('My','age','is',Age)# Here comma gives a single space after each listed element.
print('My','age','is',Age,sep='*',end='!\n') 
print('My','age','is',Age,sep='^',end='!') 
# Here Any element listed in SEP separates all the listed elements by the element in SEP. 
# END in the list displays the character at the end of the list, as ! here.
# \n adds new line after the current.
