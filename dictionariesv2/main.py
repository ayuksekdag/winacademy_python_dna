# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    my_dict = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return my_dict


def add_stamp(passport, country):
    passport["stamps"] = country
    return passport


def add_biometric_data(passport, name, biometric_data, date_of_biometric_data):

    if "biometric" not in passport.keys():
        passport["biometric"] = {
            name: {"date": date_of_biometric_data, "value": biometric_data},
        }
    else:
        passport["biometric"][name] = {
            "date": date_of_biometric_data,
            "value": biometric_data,
        }
    return passport


if __name__ == "__main__":
    # m = create_passport("pinguin", "01012023", "antartica", "70", "none")
    # print(f"passport create for \n {m}")
    # t = add_stamp(m, "north pole")
    # print(f"travelled \n {t}")

    omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
    omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
    omari = add_biometric_data(omari, "eye_color_right", "blue", "2021-05-05")
    print("\n"), print(omari)
    omari = add_biometric_data(omari, "eye_color_right", "brown", "2022-05-05")
    print("\n"), print(omari)
