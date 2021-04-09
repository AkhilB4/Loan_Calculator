import math
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()
arguments = args.__dict__

if 'type' not in arguments.keys() or (arguments['type'] not in ['annuity', 'diff']):
    print("Incorrect parameters")

elif args.type == "diff":
    if len(arguments.keys()) < 4 or arguments['payment'] is not None or arguments['interest'] is None:
        print("Incorrect parameters.")

    else:
        del arguments['type']
        flag = True
        if len(arguments.keys()) >= 4:
            if arguments['payment'] is not None:
                print("Incorrect parameters.")
            else:
                for i, arg in enumerate(arguments.keys()):
                    if arguments[arg] is not None and arguments[arg] < 0:
                        print("Incorrect parameters.")
                        flag = False
                        break

                if flag:
                    total = 0
                    for i in range(1, args.periods + 1):
                        factor = (args.interest / 1200) * (args.principal - ((args.principal * (i - 1)) / args.periods))
                        d = (args.principal / args.periods) + factor
                        print(f"Month {i}: payment is {math.ceil(d)}")
                        total += math.ceil(d)
                    print(f"\nOverpayment = {total - args.principal}")

else:
    if len(arguments.keys()) < 4 or arguments['interest'] is None:
        print("Incorrect parameters.")

    else:
        del arguments['type']
        flag = True
        if len(arguments.keys()) >= 4:
            for i, arg in enumerate(list(arguments.keys())):
                # print(i)
                if arguments[arg] is not None and arguments[arg] < 0:
                    print("Incorrect parameters.")
                    flag = False
                    break

            if flag:
                if args.interest is not None \
                        and args.payment is not None \
                        and args.periods is not None:
                    i = args.interest / 1200
                    factor = (i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)
                    p = args.payment / factor
                    print(f"Your loan principal = {int(p)}!")
                    print(f"Overpayment = {round(args.payment * args.periods - int(p))}")

                elif args.principal is not None \
                        and args.interest is not None \
                        and args.periods is not None:
                    i = args.interest / 1200
                    factor = (i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)
                    a = math.ceil(args.principal * factor)
                    print(f"Your annuity payment = {a}!")
                    print(f"Overpayment = {a * args.periods - args.principal}")

                elif args.principal is not None \
                        and args.payment is not None \
                        and args.interest is not None:
                    i = args.interest / 1200
                    payment = args.payment / (args.payment - (i * args.principal))
                    n = math.ceil(math.log(payment, 1 + i))
                    number_of_years = n // 12
                    number_of_months = n % 12
                    total_no_of_months = 0
                    if number_of_months != 0 and number_of_years != 0:
                        if number_of_years == 1:
                            years = str(number_of_years) + " year"
                        else:
                            years = str(number_of_years) + " years"
                        if number_of_months == 1:
                            months = str(number_of_months) + " month"
                        else:
                            months = str(number_of_months) + " months"
                        print(f"It will take {years} and {months} to repay this loan!")
                        total_no_of_months = number_of_years * 12 + number_of_months

                    elif number_of_years != 0 and number_of_months == 0:
                        if number_of_years == 1:
                            years = str(number_of_years) + " year"
                        else:
                            years = str(number_of_years) + " years"
                        print(f"It will take {years} to repay this loan!")
                        total_no_of_months = number_of_years * 12

                    elif number_of_years == 0 and number_of_months != 0:
                        if number_of_months == 1:
                            months = str(number_of_months) + " month"
                        else:
                            months = str(number_of_months) + " months"
                        print(f"It will take {months} to repay this loan!")
                        total_no_of_months = number_of_months
                    print(f"Overpayment = {args.payment * total_no_of_months - args.principal}")
