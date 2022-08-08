#!/usr/bin/env python3

'''Just a price calculator in Euros for the current energy price laws adopted in Spain'''

HEPH = 0.40739  # Highest Energy Price per hour
AEPH = 0.25861  # Average Energy Price per hour

def calc_en() -> str:
    '''E(kWh/day) = P(W) * t(h/day) / 1000(W/kW)
    Returns the consumption in Euros.'''
    # kWh
    potency = int(input("Cual es la potencia tu electrodoméstico? **Como pone en la etiqueta por favor (kWh/1000h)** \n"))
    
    # hours per day in use
    hours_per_day = int(input("Cuantas horas de uso diário? \n"))
    
    # potency/1000h = Wh
    kwh = potency / 1000
    print(kwh)
    
    # Wh * price per hour
    kwh_hour = kwh * HEPH
    kwh_day = kwh_hour * hours_per_day
    kwh_month = kwh_day * 30
    return f"Consumo de: {kwh_hour:.2f}€ por hora.\nConsumo de: {kwh_day:.2f}€ al dia.\nConsumo de: {kwh_month:.2f}€ al mes."



if __name__=="__main__":
    print(calc_en())
