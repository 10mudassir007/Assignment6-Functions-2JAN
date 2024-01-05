def transport_(transportation):
    if transportation == 'bus':
        return 2000
    elif transportation == 'train':
        return 4500
    elif transportation == 'flight':
        return 6500
    else:
        return 0

def accomodation_(accomodation):
    if accomodation == 'guest house':
        return 3000
    elif accomodation == 'hotel':
        return 5000
    elif accomodation == 'villa':
        return 8000

def activities_(activity):
    if activity == 'opera':
        return 2500
    elif activity == 'sights':
        return 4500
    elif activity == 'theme park':
        return 5000

def travel_cost(destination, transport, accomodation, activities, travel, duration):
    budget_daily = 10000
    luxury_daily = 25000

    transport_cost = transport_(transport)
    accomodation_cost = accomodation_(accomodation)

    activity_cost = 0
    for activity in activities:
        activity_cost += activities_(activity)

    total_cost = 0

    if travel == 'budget':
        total_cost += (budget_daily + accomodation_cost + transport_cost + activity_cost) * duration
    elif travel == 'luxury':
        total_cost += (luxury_daily + accomodation_cost + transport_cost + activity_cost) * duration
    else:
        return 'Invalid travel style'

    return total_cost

print(travel_cost('Paris', 'bus', 'hotel', ['opera'], 'budget', 4))
