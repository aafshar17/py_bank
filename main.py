

import csv      # need to import that csv module


csv_path = 'raw_data/budget_data_1.csv'     # set global file path which can be accessed by anyone

csv_file = open (csv_path, 'r')
csv_reader = csv.reader(csv_file, delimiter=',')

# with open (csv_path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

for line in csv_reader:
    print(line)

csv_file.seek(0)


def resetFileToBeginning():
    csv_file.seek(0)


def calculateTotalNumberOfMonths():
    resetFileToBeginning()
    next(csv_reader)           # skip the first line in the file, which is the header

    count_of_months = 0
    for row in csv_reader:
        if row[0] != " ":
            count_of_months = count_of_months + 1
        else:
            break
    return count_of_months


def calculateTotalRevenue():
    resetFileToBeginning()
    next(csv_reader)           # skip the first line in the file, which is the header

    total_revenue = 0
    number_of_months = 0

    for row in csv_reader:
        if row[0] != " ":
            revenue = row[1]
            total_revenue = total_revenue + int(revenue)
            number_of_months = number_of_months + 1
        else:
            break
    return total_revenue

def calculateAverageMonthlyRevChange():
    resetFileToBeginning()
    next(csv_reader)  # skip the first line in the file, which is the header

    previous_months_rev = 0
    total_change_in_rev = 0
    number_of_months_in_period = 0

    for row in csv_reader:
        if row[0] != " ":
            change_in_revenue = float(row[1]) - previous_months_rev
            total_change_in_rev = total_change_in_rev + float(change_in_revenue)
            previous_months_rev = float(row[1])
            number_of_months_in_period = number_of_months_in_period + 1
        else:
            break

    avg_rev_change_in_period = total_change_in_rev/number_of_months_in_period

    return int(avg_rev_change_in_period)


def calculateGreatestIncreaseInRevenue():

    resetFileToBeginning()
    next(csv_reader)  # skip the first line in the file, which is the header

    previous_month_revenue = 0
    change_in_rev = 0
    max_change_in_rev = 0
    number_of_months_in_period = 0
    date_max_change = 0

    for row in csv_reader:
        if row[0] != " ":
            change_in_rev = float(row[1]) - previous_month_revenue
            if max_change_in_rev < change_in_rev:
                max_change_in_rev = change_in_rev
                date_max_change = row[0]
                previous_month_revenue = float(row[1])
                number_of_months_in_period = number_of_months_in_period + 1
        else:
            break
        number_of_months_in_period = number_of_months_in_period + 1
    return date_max_change, int(max_change_in_rev)


def calculateGreatestDecreaseInRevenue():

    resetFileToBeginning()
    next(csv_reader)  # skip the first line in the file, which is the header

    previous_month_rev = 0
    change_in_revenue = 0
    maximum_negative_change_in_revenue = 0
    number_of_months_in_period = 0
    date_maximum_negative_change = 0

    for row in csv_reader:
        if row[0] != " ":
            change_in_revenue = float(row[1]) - previous_month_rev
            if maximum_negative_change_in_revenue > change_in_revenue:
                maximum_negative_change_in_revenue = change_in_revenue
                date_maximum_negative_change = row[0]
                previous_month_rev = float(row[1])
            number_of_months_in_period = number_of_months_in_period + 1
        else:
            break
    return date_maximum_negative_change, int(maximum_negative_change_in_revenue)


def print_financial_analysis(total_number_of_months, total_revenue_over_period, avg_change_in_rev_over_period,
                             date_greatest_increase_in_rev, greatest_increase_in_rev, date_greatest_decrease_revenue,
                             greatest_decrease_revenue):
    print('\n')
    print('Financial Analysis', )
    print('-------------------------', )
    print('Total Months: ' + str(total_number_of_months), )
    print('Total Revenue: ' + '$' + str(total_revenue_over_period), )
    print('Average Revenue Change: ' + '$' + str(avg_change_in_rev_over_period), )
    print('Greatest Increase in Revenue: ' + str(date_greatest_increase_in_rev) + ':' + '(' + '$' + str(greatest_increase_in_rev) + ')' ,)
    print('Greatest Decrease in Revenue: ' + str(date_greatest_decrease_revenue) + ':' + '(' + '$' + str(greatest_decrease_revenue) + ')' ,)
    print('------------------------- ', )



def write_output_resulting_file(total_number_of_months, total_revenue_over_period, avg_change_in_rev_over_period,
                                date_greatest_increase_in_rev, greatest_increase_in_rev,
                                date_greatest_decrease_revenue, greatest_decrease_revenue):




    with open('raw_data/output_result.txt', 'w') as outputFile:
        outputFile.write('\n')
        outputFile.write('Financial Analysis', )
        outputFile.write('\n')
        outputFile.write('-------------------------', )
        outputFile.write('\n')
        outputFile.write('Total Months: ' + str(total_number_of_months), )
        outputFile.write('\n')
        outputFile.write('Total Revenue: ' + '$' + str(total_revenue_over_period), )
        outputFile.write('\n')
        outputFile.write('Average Revenue Change: ' + '$' + str(avg_change_in_rev_over_period), )
        outputFile.write('\n')
        outputFile.write('Greatest Increase in Revenue: ' + str(date_greatest_increase_in_rev) + ':' + '(' + '$' + str(greatest_increase_in_rev) + ')' ,)
        outputFile.write('\n')
        outputFile.write('Greatest Decrease in Revenue: ' + str(date_greatest_decrease_revenue) + ':' + '(' + '$' + str(greatest_decrease_revenue) + ')' ,)

        # outputFile.write('The total number of months over period is ' + str(total_number_of_months))
        # outputFile.write('\n')

        # outputFile.write('The total revenue over period is $' + str(total_revenue_over_period))
        # outputFile.write('\n')

        # outputFile.write('The average change in revenue is $' + str(avg_change_in_rev_over_period))
        # outputFile.write('\n')

        # outputFile.write('Date is ' + date_greatest_increase_in_rev + ' The greatest increase in revenue is $ ' +
                        # str(greatest_increase_in_rev))
        # outputFile.write('\n')

        # outputFile.write('Date is ' + str(date_greatest_decrease_revenue) + ' The greatest decrease in revenue is $ ' +
                        # str(greatest_decrease_revenue))
        # outputFile.write('\n')



def startProcess():

    total_number_of_months = calculateTotalNumberOfMonths()

    # str_total_number_of_months = 'The total number of months over period is ' + str(total_number_of_months)

    # print(str_total_number_of_months)

    total_revenue_over_period = calculateTotalRevenue()

    # print('The total revenue over period is $' + str(total_revenue_over_period))

    avg_change_in_rev_over_period = calculateAverageMonthlyRevChange()

    # print('The average change in revenue is $' + str(avg_change_in_rev_over_period))

    date_greatest_increase_in_rev, greatest_increase_in_rev = calculateGreatestIncreaseInRevenue()

    # print('Date is ' + date_greatest_increase_in_rev + ' The greatest increase in revenue is $ ' +
          # str(greatest_increase_in_rev))

    date_greatest_decrease_revenue, greatest_decrease_revenue = calculateGreatestDecreaseInRevenue()

    # print('Date is ' + str(date_greatest_decrease_revenue) + ' The greatest decrease in revenue is $ ' +
          # str(greatest_decrease_revenue))


    print_financial_analysis(total_number_of_months, total_revenue_over_period, avg_change_in_rev_over_period, date_greatest_increase_in_rev,
                             greatest_increase_in_rev, date_greatest_decrease_revenue, greatest_decrease_revenue)

    write_output_resulting_file(total_number_of_months, total_revenue_over_period, avg_change_in_rev_over_period,
                                date_greatest_increase_in_rev, greatest_increase_in_rev,
                                date_greatest_decrease_revenue, greatest_decrease_revenue)

startProcess()