def ticket(people,ages,day):
    adult = 800
    teen = 650
    child = 500

    discount = 0.1
    total_price = 0
    for age in ages:
        if age>18:
            price = adult
        elif age>14:
            price = teen
        elif age<14:
            price = child
        
        if day in ['friday','saturday','sunday']:
            multiplier = 1.2
        else:
            multiplier = 1.0

        price = price * multiplier
        total_price += price

    people = len(ages)

    if people > 3:
        total_price -= (total_price*discount)

    return total_price

print(ticket(4,[10,24,21,27],'monday'))