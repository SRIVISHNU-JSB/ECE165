# a. Given a circuit in Figure 1, write a Python program to solve it to find out 
# the circuit current 𝑰𝟏, 𝑰𝟐, 𝑰3 and node voltages 𝑽𝒂, 𝑽𝒃

R1 = 10 #10 Ohms
R2 = 40 #40 Ohms
R3 = 20 #20 Ohms

Vs = 10 #10 Volts

# Ohms law - V(Voltage)=I(current) x R(Resistance) => I=V/R

# Serial Resistance
Rs = R1
# Parallel Resistance
Rp = ((R2*R3)/(R2+R3))
# Total Resistance
Rt = Rp+Rs
# Total Current
It = Vs/Rt

Va = It*R1

Vb = Vs-Va

I1 = Va/R1
I2 = Vb/R3; I2=-I2 # For the circuit's current flow is reversed in direction
I3 = Vb/R2

print(Va+Vb)
print(It,I1,(-I2+I3)) # Hence Kirchhoff's law preserved
print(I1,I2,I3,Va,Vb) # Hence Kirchhoff's law preserved

# b. Modify the above code to use function. The function should accept the resister values 𝑹𝟏, 𝑹𝟐 and 𝑹𝟑, 
# as well, the supply voltage 𝑽𝒔 as input parameters passed user.Pass the parameter voltage 𝑽𝒔 using 
# the default value of 10 V. The function should return branch currents 𝑰𝟏, 𝑰𝟐 and node voltages 𝑽𝒂, 𝑽𝒃.

def Circuit_Analysis(R1, R2, R3, Vs=10):
    
    # Ohms law - V(Voltage)=I(current) x R(Resistance) => I=V/R

    # Serial Resistance
    Rs = R1
    # Parallel Resistance
    Rp = ((R2*R3)/(R2+R3))
    # Total Resistance
    Rt = Rp+Rs
    # Total Current
    It = Vs/Rt

    Va = It*R1

    Vb = Vs-Va

    I1 = Va/R1
    I2 = Vb/R3; I2=-I2 # For the circuit's current flow is reversed in direction
    I3 = Vb/R2

#     print(Va+Vb)
#     print(It,I1,(-I2+I3)) # Hence Kirchhoff's law preserved
    
    return I1,I2,Va,Vb

# Note: The input separated by spaces. In case we wish to take input separated by comma (, ) 
# we can use it as required.
R1,R2,R3,Vs=[int(i) for i in input('Enter the R1,R2,Rs and Vs: ').split(' ')]

print(Circuit_Analysis(R1,R2,R3,Vs))