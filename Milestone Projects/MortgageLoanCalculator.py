# Author: Joe Do
# March 26, 2018
# Monthly payment and loan balance

months = int(input("Enter mortgage term (in months): "))
rate = float(input("Enter interest rate: "))
loan = float(input("Enter loan value: "))

# [If the quoted rate is 6%, for example, monthly_rate is .06/12 or .005].
monthly_rate = rate / 100 / 12

# The following formula is used to calculate the fixed monthly payment (P)
# required to fully amortize a loan of L dollars over a term of n months
# at a monthly interest rate of c.
# P = L[c(1 + c)n]/[(1 + c)n - 1]
payment = loan * (monthly_rate*(1 + monthly_rate)**months)/((1 + monthly_rate)**months - 1)

print ('Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f' % (loan, (months / 12), rate, payment))

p = int(input("How many months did you make payments? "))
# The next formula is used to calculate the remaining loan balance (B)
# of a fixed payment loan after p months.
# B = L[(1 + c)^n - (1 + c)^p]/[(1 + c)^n - 1]
B = loan * (((1 + monthly_rate)**months - (1 + monthly_rate)**p) / ((1 + monthly_rate)**months - 1))
print('The remaining loan balance is $%.2f' %(B))
