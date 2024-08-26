print("Let's practice everything.")
print("You\'d need to know \' bout escapes with \\ that do:")
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print('--------------')
print(poem)
print('-------------')


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
# ==> def secret_formula(10000):
    jelly_beans = started * 500
    # ==> jelly_beans = started(10000) * 500
    jars = jelly_beans / 1000
    # ==> jars = jelly_beans(5000000) / 1000
    crates = jars / 100
    # ==> crates = jars(50000.0) / 100
    return  jelly_beans,jars, crates
    # ==> return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
#beans, jars, crates = secret_formula(10000)

# Remeber that this is another way to format a string
print("With the starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have jelly_beans , {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))