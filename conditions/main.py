# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, cow_milking_status, location_of_the_cows,
                season, slurry_tank, grass_status):
    result = ""
    if weather == "rainy":
        if time_of_day == "day":
            if location_of_the_cows == "cowshed":
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
            # location = pasture
            else:
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    ""
        # time of day is night
        else:
            if location_of_the_cows == "cowshed":
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                result = result + "fertilize pasture"
                            else:
                                ""
                        else:
                            if grass_status:
                                result = result + "wait"

                            else:
                                ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
            # location = pasture
            else:
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    ""
    elif weather == "sunny":
        if time_of_day == "day":
            if location_of_the_cows == "cowshed":
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
            # location = pasture
            else:
                result = result + "take cows to cowshed\n"
                if cow_milking_status:
                    result = result + "milk cows\n"
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            if grass_status:
                                ""
                            else:
                                ""
                            result = result + "take cows back to pasture"
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    ""
        # time of day is night
        else:
            if location_of_the_cows == "cowshed":
                if cow_milking_status:
                    result = result + 'milk cows'
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                result = result + "milk cows"
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
            # location = pasture
            else:
                result = result + 'take cows to cowshed \n'
                if cow_milking_status:
                    result = result + 'milk cows'
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    ""
    elif weather == "windy":
        if time_of_day == "day":
            if location_of_the_cows == "cowshed":
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
            # location = pasture
            else:
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    ""
        # time of day is night
        else:
            if location_of_the_cows == "cowshed":
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                result = result + "milk cows"
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
            # location = pasture
            else:
                if cow_milking_status:
                    if season == "winter":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "spring":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    elif season == "summer":
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                    #season = fall
                    else:
                        if slurry_tank:
                            if grass_status:
                                ""
                            else:
                                ""
                        else:
                            ""
                #milkstatus = False
                else:
                    ""
    else:
        result = result + "wait"

    return result


if __name__ == '__main__':
    x = farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
    print(x)
    #'fertilize pasture'
    x = farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
    print(x)
    #'wait'
    x = farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
    print(x)
    #'milk cows'
    x = farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
    print(x)
#"""take cows to cowshed
#milk cows
