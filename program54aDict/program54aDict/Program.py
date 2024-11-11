car = {
    "1970 VW Bug":   [186,  9],
    "1979 Firebird": [412, 40],
    "1980 Subaru":   [361, 18],
    "1975 Cutlass":  [161, 11]
}

Print("Choose a car from the following:", car.keys())
mycar = input()
mile, gallons = car[mycar]
mpg = float(mile) / gallons
print("miles:", mile)
print("gallons:", gallons)
print("MPG:", round(mpg, 1))

input()