# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, cow_milking_status, location_of_the_cows,
                season, slurry_tank, grass_status):
    result = ""
    if weather == "rain" or time_of_day == "night":
        result = result + "take cows to cowshed\n"
        if cow_milking_status == True:
            result = result + "milk cows\n"
    if slurry_tank == True and time_of_day == "night" and weather != "sunny":
        result = result + "fertilize pasture\n"
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
