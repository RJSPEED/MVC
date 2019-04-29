import bt_model
import bt_view


def run():
    bt_model.load()
    mainmenu()

def mainmenu():
    while True:
        bt_view.show_menu()
        selection = bt_view.get_input()        
        #Account Creation
        if selection == '1':
            account = None
            pin = None
            #Gather account details
            f_name = bt_view.get_input_new_account("First Name")
            l_name = bt_view.get_input_new_account("Last Name")
            pin = bt_view.get_input_new_account("PIN")
            con_pin = bt_view.get_input_new_account("Confirm PIN")
            #Check if pins match
            if pin != con_pin:
                bt_view.get_pins_unmatched()
            else:
                #Create account, ie. add to data dictionary
                account = bt_model.create_account(f_name, l_name, pin)
                bt_view.get_new_account_confirm(account)
        #Log In
        elif selection == '2':    
            #Gather account numer and pin
            account = None
            pin = None
            new_balance = None
            account = bt_view.get_account_details("Account Number")
            pin = bt_view.get_account_details("PIN")
            #Return greeting
            if bt_model.validate_account(account, pin) == "xxx":
                #Failed to find account
                bt_view.get_failed_validate_msg()
            else:
                #Welcome greeting
                details = bt_model.validate_account(account, pin)
                details = details + " (" + account + ")"
                bt_view.get_login_greeting(details)
                while True:
                    #New sub-menu
                    bt_view.show_op2_menu()
                    op2_selection = bt_view.get_input() 
                    if op2_selection == '1':
                        #Check Bal
                        balance = bt_model.get_bal(account)
                        bt_view.get_show_balance(balance)
                    elif op2_selection == '2':
                        #Withdraw
                        amount = bt_view.get_with_or_dep_amount("Withdrawal Amount:")
                        new_balance = bt_model.withdraw(account, amount)
                        if new_balance == "xxx":
                            #Insufficient funds
                            bt_view.get_post_withdrawal_reject_msg()
                        else:
                            bt_view.get_post_withdrawal_msg(amount,new_balance)
                    elif op2_selection == '3':
                        #Deposit
                        amount = bt_view.get_with_or_dep_amount("Deposit Amount:")
                        new_balance = bt_model.deposit(account, amount)
                        bt_view.get_post_deposit_msg(amount,new_balance)
                    else:
                        bt_model.save()
                        return
        else:
            bt_model.save()
            return

if __name__ == "__main__":
    run()
