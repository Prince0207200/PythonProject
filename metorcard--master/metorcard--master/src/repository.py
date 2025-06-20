from src.model import Station

metroCard = dict()
ADULT_FARE = 200
SENIOR_CITIZEN_FARE = 100
KID_FARE = 50
RECHARGE_FEE_PERCENT = 2

rates = {
    "ADULT": ADULT_FARE,
    "SENIOR_CITIZEN": SENIOR_CITIZEN_FARE,
    "KID": KID_FARE
}




stations = {
    "CENTRAL": Station("CENTRAL"),
    "AIRPORT": Station("AIRPORT")
}
