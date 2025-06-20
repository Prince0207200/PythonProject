from .repository import *
from .model import MetroCard

# Constants
RECHARGE_FEE_PERCENT = 2
DISCOUNT_PERCENT_ON_RETURN = 50

def balance(mid, balance):
    metroCard[mid] = MetroCard(mid, int(balance))

def recharge_card(card, amount, station_name):
    card.add_balance(amount)
    station = stations[station_name]
    recharge_fee = (amount * RECHARGE_FEE_PERCENT) / 100
    station.add_amount(recharge_fee)

def check_in(mid, passenger_type, src):
    card = metroCard[mid]
    original_fare = rates[passenger_type]
    fare = original_fare
    station = stations[src]

    # ✅ Apply discount only once for return journey
    is_return_trip = (
        (card.src == "AIRPORT" and src == "CENTRAL") or
        (card.src == "CENTRAL" and src == "AIRPORT")
    )

    if is_return_trip and not card.used_discount:
        discount = (original_fare * DISCOUNT_PERCENT_ON_RETURN) / 100
        fare -= discount
        station.add_discount(discount)
        card.used_discount = True

    # Recharge if needed
    if card.balance < fare:
        recharge_card(card, fare - card.balance, src)

    card.add_balance(-fare)
    card.update_src(src)

    station.add_amount(fare)
    station.add_passenger(passenger_type)

def summary():
    for station_name in ['CENTRAL', 'AIRPORT']:
        station = stations[station_name]
        print(f"TOTAL_COLLECTION {station_name} {int(station.total_amount)} {int(station.discount)}")
        print("PASSENGER_TYPE_SUMMARY")
        for p_type in sorted(station.passenger_history.keys()):
            print(p_type, station.passenger_history[p_type])
