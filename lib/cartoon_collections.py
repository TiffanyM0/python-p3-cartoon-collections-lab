def roll_call_dwarves(list_dwarves):
    pass
    for name in list_dwarves:
        num = list_dwarves.index(name) +1
        print (f"{num}. {name}")


def summon_captain_planet(planeteer_calls):
    pass
    caps_planeteer_calls = [f"{call.title()}!"for call in planeteer_calls]
    print (caps_planeteer_calls)
    return caps_planeteer_calls

def long_planeteer_calls(planeteer_calls):
    pass
    true_calls = [call for call in planeteer_calls if len(call) > 4]
    if len(true_calls) > 0:
        return True
    return False           


def find_the_cheese(snacks):
    pass
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks :
        for cheese in cheeses:
            if cheese in snack:
                return cheese
    return None