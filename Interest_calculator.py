#code for simple interest and compound interest calculation
#Interest calculator

p = float(input("Enter the principal amount of the loan in ₹ :")); #Taking user input regarding the principal amount of the loan taken
r = float(input("Enter the interest rate in percentage (within 0-100%) :")); #Taking user input regarding the interest rate of the loan taken
t = float(input("Enter the time period of the loan in years :")); #Taking user input regarding the time period for which the loan was taken
i = float(input("Enter the yearly fixed interest amount in ₹ :"));#Taking user input regarding the fixed interest amount charged.

print("The Principal amount of the loan in ₹ is : ₹ ", p);
print("The Interest rate in percentage {%} is : ",r);
print("The Time Period of the loan in years is : ",t);
print("********************************************************");

#Code block inorder to compute simple interest

SI = (p*r*t)/100;
PA = p + SI;
print("The Simple Interest in ₹ is : ₹", SI);
print("The total Amount to payback so that the loan is cleared in ₹ is : ₹", PA);
print("********************************************************");

#Code block inorder to compute compound interest

b =  1 + (r/100);
x= pow(b,t);
CI = p*x - p;
CPA = CI + p;
print("The Compound Interest in ₹ is : ₹", CI);
print("The total Amount to payback so that the loan is cleared in ₹ is : ₹", CPA);
print("********************************************************");

#Code block inoder to compute accrued interest

AI = p*(i/365)*t;
APA = AI + p;
print("The Accrued Interest in ₹ is : ₹", AI);
print("The total Amount to payback so that the loan is cleared in ₹ is : ₹", APA);
print("********************************************************");

print("Thank You");
print("********************************************************");


