def get_quarterly(annual_quota, annual_incentive_quota):
    return [annual_quota / 4, annual_incentive_quota / 4]

def no_incentive():
    return [0, 0]

def full_incentive(annual_q, annual_i, money):
    q = get_quarterly(annual_q, annual_i)
    percent = money / q[0]
    incentive_percentage_earned = .25 + ((percent - .5)*100) * .015
    incentive_earned = q[1] * incentive_percentage_earned
    return [incentive_percentage_earned, incentive_earned]

def two_five_incentive(annual_q, annual_i, money):
    q = get_quarterly(annual_q, annual_i)
    percent = money / q[0]
    incentive_percentage_earned = 1 + ((percent-1)*100) * .025
    incentive_earned = q[1] * incentive_percentage_earned
    return [incentive_percentage_earned, incentive_earned]

def ascending_incentive(annual_q, annual_i, money):
    q = get_quarterly(annual_q, annual_i)
    percent = money / q[0]
    incentive_percentage_earned = 1.625 + ((percent - 1.25)*100) * .015
    incentive_earned = q[1] * incentive_percentage_earned
    return [incentive_percentage_earned, incentive_earned]


def main():
    run_app = True
    while(run_app):
        # user_annual_quota
        usr_q = int(input("Enter the annual quota for the agent: "))
        # user annaul incentive
        usr_i = int(input("Enter the annual incentive for the agent: "))
        # user quarterly cash attainment
        usr_money = int(input("Enter the QUARTERLY ammount of money earned: "))

        usr = get_quarterly(usr_q, usr_i)
        usr_percent = usr_money / usr[0]

        if usr_percent < .5:
            pp = no_incentive()
        elif usr_percent <= 1:
            pp = full_incentive(usr_q, usr_i, usr_money)
        elif usr_percent <= 1.25:
            pp = two_five_incentive(usr_q, usr_i, usr_money)
        else:
            pp = ascending_incentive(usr_q, usr_i, usr_money)

        print("The Agent earned " + str(pp[0]*100) + "% of there quarterly quota.")
        print("Earning them: $" + str(pp[1]))

        let = input("Press q to quit, or enter to continue: ")
        if let == "q":
            run_app = False

if __name__=="__main__":
    main()
