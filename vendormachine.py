print("Welcome...")
print("Available Items :\n","1.Milk(Rs.30/L)\n","2.Curd(Rs.35/L)\n","3.Both")
choice=input("Please Enter your choice :")
choice=choice.lower()

def quantity_calculation(choice):
    packet_choice=input("Do you need packets.Available packets are 0.5L,1L and 2L ")
    packet_choice=packet_choice.lower()
    if packet_choice=='yes':
        halflitre_packet=int(input("Enter number of packets of 0.5L :"))
        fulllitre_packet=int(input("Enter number of packets of 1L :"))
        twolitre_packet=int(input("Enter number of packets of 2L :"))
        quantity=halflitre_packet*0.5+fulllitre_packet+twolitre_packet*2
        user_cost=int(input("Enter your input cost : "))
        cost=cost_calculation(quantity,choice)
        balance_cost=user_cost-cost
        if balance_cost==0:
            print("Thank you..Please collect your item")
        else:
            print("Please collect your item and balance of",balance_cost)   

    else:
        quantity=int(input("Enter the quantity you needed :"))
        user_cost=int(input("Enter your input cost :"))
        cost=cost_calculation(quantity,choice)
        balance_cost=user_cost-cost
        if balance_cost==0:
            print("Thank you..Please collect your item")
        else:
            print("Balance :",balance_cost)
            print("Please collect your balance and item")  

def cost_calculation(quantity,choice_selection):
    if choice_selection=='milk':
        return quantity*30

    elif choice_selection=='curd':
        return quantity*35

if choice=='milk':
    quantity_calculation('milk')
    
elif choice=='curd':
    quantity_calculation('curd') 
elif choice=='both':
    packet_choice=input("Do you need packets.Available packets are 0.5L,1L and 2L ")
    packet_choice=packet_choice.lower()
    if packet_choice=='yes':
        print("Milk :")
        print("--------------------")
        halflitre_packet=int(input("Enter number of packets of 0.5L :"))
        fulllitre_packet=int(input("Enter number of packets of 1L :"))
        twolitre_packet=int(input("Enter number of packets of 2L :"))
        quantity=halflitre_packet*0.5+fulllitre_packet+twolitre_packet*2
        costof_milk=cost_calculation(quantity,'milk')
        print("Curd :")
        print("--------------------")
        halflitre_packet=int(input("Enter number of packets of 0.5L :"))
        fulllitre_packet=int(input("Enter number of packets of 1L :"))
        twolitre_packet=int(input("Enter number of packets of 2L :"))
        quantity=halflitre_packet*0.5+fulllitre_packet+twolitre_packet*2
        costof_curd=cost_calculation(quantity,'curd')
        user_cost=int(input("Enter your input cost :"))
        total_cost=costof_milk+costof_curd
        balance_cost=user_cost-total_cost
        if balance_cost==0:
            print("Thank you..Please collect your item")
        else:
            print("Balance :",balance_cost)
            print("Please collect your balance and item") 
          
    else:
        quantity_milk=int(input("Enter the quantity of milk you needed :"))
        quantity_curd=int(input("Enter the quantity of curd you needed: "))
        milk_cost=cost_calculation(quantity_milk,'milk')
        curd_Cost=cost_calculation(quantity_curd,'curd')
        cost=milk_cost+curd_Cost
        userinput_cost=int(input("Enter input cost : "))
        balance=userinput_cost-cost
        print("balance is",balance)   
        
else:
    print("Please enter a valid option")       