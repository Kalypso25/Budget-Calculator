#create a budget tracker
#monthly income
month_net = 7818
tenant_rent = 2256.45
total_income = month_net + tenant_rent
#insert school expenses
flt_seat = 69.98
sc_flt = 567
atl_shuttle = 116
sc_books = 9.99
#insert monthly expenses
mortgage_exp = 2590.88
rent_ins = 26
laundry = 26
hoa_fees = 817.58
cell_bill = 128.12
adobe = 10.46
apple_cons = 43.42
gym = 27.11
UMGC_bill = 473
gas = 60
power = 100
water = 40
cc_mo_payoff = 600
my_rent = 800
food = 400
#trying a dictionary
try:
    expense_dic = {'flt_seat': 69.98, 'sc_flt': 567.80,'atl_shuttle': 116, 'sc_books': 9.99, 'mortgage_exp': 2590.88,\
    '               rent_ins': 26, 'laundry': 26,'hoa_fees': 817.58,'cell_bill': 128.12, 'adobe': 10.46, \
                   'apple_cons': 43.42,'gym': 27.11, 'UMGC_bill': 473, 'gas': 60, 'power': 100, 'water ': 40, \
                   'cc_mo_payoff': 600,'my_rent': 800, 'food': 400}
except TypeError:
    print('TypeError')
except KeyError:
    print('KeyError')
except NameError:
    print('NameError')


total_sc_exp = flt_seat + sc_flt + atl_shuttle + sc_books
total_mis_exp = mortgage_exp + rent_ins + laundry + hoa_fees + cell_bill + adobe + apple_cons + gym + UMGC_bill + \
                gas + power + water + cc_mo_payoff + my_rent + food
debit_expenses = total_sc_exp + total_mis_exp
#create calc
print("Your total monthly school expenses are: ", round(total_sc_exp),"\nYour total monthly bill expenses are: ",
      round(total_mis_exp))
print("Your remaining balance after all expenses is: ", round(total_income) - round(debit_expenses))
play_money = round(total_income) - round(debit_expenses)
money_leftover = play_money * 12
print("You have ", money_leftover, "left over to invest or stack for the year ")

