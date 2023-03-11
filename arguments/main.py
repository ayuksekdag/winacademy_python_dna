# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, template="Hello, <name>!"):
    x = template.replace("<name>", name)
    return x


def force(mass, body="earth"):
    dict = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }
    gravity = dict.get(body)
    gravity = round(gravity, 1)
    force = gravity * mass
    return force


def pull(m1, m2, d1):

    G = 6.673 * (10**-11)
    F = G * ((m1 * m2) / d1**2)
    F = round(F, 10)
    print(f"F is {F}")
    return F


if __name__ == "__main__":
    print(greet(name="ali"))
    print(greet("Bob", "What's up, <name>!"))
    print("\n")
    print(force(1))
    print(pull(m1=800, m2=1500, d1=3))
