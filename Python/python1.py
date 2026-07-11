MAB=5000
cibil_score=750
ACC_balance=10000
if MAB>5000 and cibil_score>700 and ACC_balance>5000:
    print("Eligible for loan")  
else:
    print("Not eligible for loan,Because either MAB is less than or equal to 5000, cibil_score is less than or equal to 700, or ACC_balance is less than or equal to 5000.")