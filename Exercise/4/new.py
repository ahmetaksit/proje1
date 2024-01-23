import sys,argparse
print("program adı:"+sys.argv[0])
print("tüm parametre:"+ str(sys.argv))
print("argparse pakalti"+str(argparse.ArgumentParser(prog="deneme",description="okey")))
parca = argparse.ArgumentParser()
parca.add_argument('-f',"--deneme",help="foo help")
parca.add_argument("-d","--delete",action="store_true")
arts = parca.parse_args()
print(arts)
