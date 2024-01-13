# Object Oriented Programming Assignment
# Calculation of Rental Income

class ROICalculator():

    def __init__(self, income, expenses, cash_flow, cash_on_cash_ROI):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.cash_on_cash_ROI = cash_on_cash_ROI

    # method to determine our total monthly income
    def determine_income(self):
            try:
                rent = float(input('How much income from rent do you recieve each month? $'))
                self.income.append(rent)
                laundry = float(input('How much income from laundry costs do you recieve each month? $'))
                self.income.append(laundry)
                storage = float(input('How much income from storage costs do you recieve each month? $'))
                self.income.append(storage)
                misc = float(input('If you recieve income from anything else each month, enter the total of that here. $'))
                self.income.append(misc)

            except ValueError:
                print('Please enter a number as your given response.')

            print('Your monthly income has been determined.')
        
        # the sum of the income will be calculated in the cash_flow function

    # method to determine our total monthly expenses
    def determine_expenses(self):
            try:
                tax = float(input('How much do you spend on tax costs each month? $'))
                self.expenses.append(tax)
                insurance = float(input('How much do you spend on insurance costs each month? $'))
                self.expenses.append(insurance)
                print("Lets go over some utilities now.")
                electric = float(input('How much do you spend on electric costs each month? $'))
                self.expenses.append(electric)
                water = float(input('How much do you spend on water costs each month? $'))
                self.expenses.append(water)
                sewer = float(input('How much do you spend on sewer costs each month? $'))
                self.expenses.append(sewer)
                garbage = float(input('How much do you spend on garbage costs each month? $'))
                self.expenses.append(garbage)
                gas = float(input('How much do you spend on gas costs each month? $'))
                self.expenses.append(gas)
                print("Now we can finish up with the rest of your expenses.")
                hoa = float(input('How much do you spend on hoa costs each month? $'))
                self.expenses.append(hoa)
                lawn = float(input('How much do you spend on lawn costs each month? $'))
                self.expenses.append(lawn)
                vacancy = float(input('How much do you put aside for possible vacancies each month? $'))
                self.expenses.append(vacancy)
                repairs = float(input('How much do you put aside for possible minor repairs each month? $'))
                self.expenses.append(repairs)
                CAPX = float(input('How much do you put aside for possible high cost large repairs each month? $'))
                self.expenses.append(CAPX)
                property_management = float(input('How much money goes to property management each month? $'))
                self.expenses.append(property_management)
                mortgage = float(input('How much money goes to the mortgage each month? $'))
                self.expenses.append(mortgage)
            
            except ValueError:
                print('Please enter a number as your given response.')

            print('Your monthly expenses have been determined.')

        # the sum of the expenses will be calculated in the cash_flow function

    # method to calculate monthly cash flow
    def calc_cash_flow(self):
        self.cash_flow = sum(self.income) - sum(self.expenses)

        print(f'Your monthly cash flow is {self.cash_flow}')

    # method to determine cash on cash return of investment
    def determine_cash_on_cash(self):
            try:
                down_payment = float(input('How much money did the down payment on the property cost? $'))
                self.cash_on_cash_ROI.append(down_payment)
                closing_costs = float(input('How much money did the closing costs on the property cost? $'))
                self.cash_on_cash_ROI.append(closing_costs)
                rehab_budget = float(input('How much money did repairs on the property cost? $'))
                self.cash_on_cash_ROI.append(rehab_budget)
                misc = float(input('If there were any other investment costs, enter that amount here. $'))
                self.cash_on_cash_ROI.append(misc)
            
            except ValueError:
                print('Please enter a number as your given response.')

            print('Your investment expenses have been determined.')

    # finally, we can calculate the ROI
    def calc_roi(self):
        annual_cash_flow = self.cash_flow * 12
        raw_roi = annual_cash_flow / sum(self.cash_on_cash_ROI)
        roi = raw_roi * 100
        print(f'The ROI on your property is: {roi}%')

    
# now to create the function to make the class run
        
ROI = ROICalculator([], [], [], [])

def run():
    while True:
        print("Let's start calculating the ROI on your property")
        start = input('Would you like to get started? ')

        if start.lower() == 'yes':
            ROI.determine_income()
            ROI.determine_expenses()
            ROI.calc_cash_flow()
            ROI.determine_cash_on_cash()
            ROI.calc_roi()
            break;
        elif start.lower() == 'no':
            print('No problem, come back soon!')
            break;
        else:
            print("Please enter 'yes' or 'no' to continue.")

run()

# this may be overkill, but it calculates the same as the man in the video so i hope it's alright!