def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    return total 
print("Total amount:" , round(total_calc(678,15),2))