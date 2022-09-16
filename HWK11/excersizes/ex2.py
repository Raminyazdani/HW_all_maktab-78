import argparse


parser = argparse.ArgumentParser(description="python script for calculating averages")
parser.add_argument("-g","--grades",type=float,nargs="+",required=True)
parser.add_argument("-f","--float",type=int,required=False,default=2)

args = vars(parser.parse_args())

result = round(sum(args["grades"])/len(args["grades"]),args["float"])

print(f"{result}")