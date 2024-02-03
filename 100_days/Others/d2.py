while (True):
  bill=float(input('Enter the bill amount\n'))
  if (bill>=150):
    break
  else:
    continue

persons=int(input("Enter the no of persons sharing the bill\n"))
bill_tip=bill*1.12
bill_share=round(bill_tip/persons,2)
print(f"The share of each person is {bill_share}")