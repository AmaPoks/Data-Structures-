      #Ama Pokuaa Agyemang
      #Index Number = 6925321
#Question a
w = 10   #load intensity on beam 


L = 12   #length of beam


x = 0    #a distance on the beam


#M is bending moment 
M = (w * (-6*x**2 + 6*L*x - L**2))/12

#V is shear force 
V = w * ((L/2) - x)

print(f'a) Bending Moment when x = 0 is M = {M}KN/m') 
print() #Puts space between answers in console
print(f'Shear Force when x = 0 is V = {V}KN')
#Shear Force and Bending Moment when x = 0

x = 12 # x is the same as L
M = (w * (-6*x**2 + 6*L*x - L**2))/12
print()
print(f'Bending Moment when x = 12 is {M}KN/m')

V = w * ((L/2) - x) 
print()
print(f'Shear Force when x = 12 is {V}KN')

#Question b
a = -6
b = 72
c = -144

square_complete = b/(2*a)

cnstnt = -c/a + square_complete**2

contraflexure_1 = (cnstnt**0.5 - square_complete)
contraflexure_2 = (-cnstnt**0.5 - square_complete)
#point_of_contraflexure_1 and point_of_contraflexure_2 are roots of the quadratic equation.
print()
print('b)The distances at which the bending moment will be zero are x1 = ' + str({contraflexure_1}) + 'x2= ' + str({contraflexure_2})) 


#Question c
V = 0 #To find x,V = 0
x = V + (L/2)  #  make x the subject
 
print()
print('c) ' + str(x) + ' is the point at which the Shear Force is = 0')

#Question d
import numpy as np
beam_length = 12  #Length(mm),(Steps is mm so convert beam_length to mm)
steps = 0.01 #(mm), convert a step of 10mm to m because the beam_length is in m
w = 10
span_beam = np.arange (0, beam_length + steps, steps) # list to discretize the beam length
x = span_beam 
M = w * (-6*x**2 + 6*L*x - L**2)/12 
print()
print('e) The Moment for each step along the span is {0}'.format(M))


#Question e
begin = 0 #0 is the starting point of the range
step = 0.01 #(mm), convert a step of 10mm to m
A = L + step #L=12m, span of the beam
x = np.arange(begin,A,step)
V = w*(L/2 - x) #V is the shear force
print()
print('(e) The shear force for each step along the span is {}'.format(V))
#to provide the shear force(V) for each value of x within the beam_span

#Question f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(span_beam) #Find the values of x within the beam_span that are close to zero and take them to zero
m_AM = min(AM) #This operation is carried out because Bending Moment is minimum when x = 0(Absolute)
"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""

#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w
#Using the Almighty formula;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print(f'f)The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))     


#Question g
"""
Let the relative errors be re
"""
re1 = ((9.464101615137753-9.46)/9.464101615137753*100)
re2 = (( 2.539999999999999-2.5358983848622456)/2.539999999999999*100)
print()
print('(g) The relative errors are {0}% and {1}%'.format(re1,re2))



#Question h
import numpy as np
def calculate_M(w, L, x):
    return(w * (-6*x**2 + 6*L*x - L**2)/12) #store function in M

beam_length = 12

values_of_moment = [] 
for x in span_beam:
    M = calculate_M(w, L, x)
    values_of_moment.append(M) #Fill the empty list created above with the moment values
    
max_BM = max(values_of_moment) #maximum bending moment in the list of moment values
min_BM = min(values_of_moment) #minimum bending moment in the list of moment values

print()
print("h) Maximum bending moment:", max_BM) 


print()
print("Minimum bending moment:", min_BM) 

#Github username = AmaPoks

    