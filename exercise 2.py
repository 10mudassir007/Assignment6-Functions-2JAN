def resturant(people,items,prices,discount):
    discount_ = 0.1
    sales_tax = 0.05

    total_price = sum(prices)
    items = len(prices)

    s_total_price = total_price + (total_price*sales_tax)
    if discount == 'yes':
        dis_price = s_total_price - (s_total_price * discount_)
        split_price = dis_price/people
        return (f'No of items ordered:{items},\nTotal Price of all items:{s_total_price},\nDiscounted price:{dis_price},\nPrice per person:{split_price}')
    else:
        split_price = s_total_price/people
        return (f'No of items ordered:{items},\nTotal Price of all items:{s_total_price},\nPrice per person:{split_price}')
    
    

print(resturant(4,3,[600,400,300],'yes'))

    