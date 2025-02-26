def individual_data(renterData):
    return {
        'name': renterData['name'],
        'room_No': renterData['room_No'],
        'room_Rent': renterData['room_Rent'],
        'rent_Paid': renterData['rent_Paid'],
        'amount_Paid': renterData['amount_Paid'],
        'balance_Amount': renterData['balance_Amount'],
        'curr_Electric_Unit': renterData['curr_Electric_Unit'],
        'prev_Electric_Unit': renterData['prev_Electric_Unit'],
        'per_Unit': renterData['per_Unit'],
        'electric_Bill': renterData['electric_Bill'],
        'status': renterData['status'],
        'month': renterData['month'],
        'paid_On': renterData['paid_On']
    }

def all_task(items):
    return [individual_data(renterData) for renterData in items]
