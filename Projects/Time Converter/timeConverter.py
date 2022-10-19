# ColumbiaTime = int(ArizonaTime) + 2
# FranceTime = int(ArizonaTime) + 9
# NetherlandsTime = int(ArizonaTime) + 9
# IndiaTime = int(ArizonaTime) + 12.50
# NewZealandTime = int(ArizonaTime) + 13



gmt_offset = {
    "Arizona": 2,
    "Columbia": 2,
    "France": 9,
    "Netherlands": 9,
    "India": 12.5,
    "NewZealand": 13
}

arizona_time = int(input("What time is it in Arizona rounded to next hour: "))

for time in (gmt_offset):
    local_time = gmt_offset[time] + (arizona_time)
    print(f" {local_time}")









# print(f"{ArizonaTime} Arizona Time")
# print(f"{ColumbiaTime} Columbia Time")
# print(f"{FranceTime} France Time")
# print(f"{IndiaTime} India Time")
# print(f"{NetherlandsTime} Netherlands Time")
# print(F"{NewZealandTime} NewZealand Time")