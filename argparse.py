import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n")

args = parser.parse_args()

for _ in range( (args.n)):
    print("meow")