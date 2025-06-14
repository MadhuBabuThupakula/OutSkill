import sys
for i in range(1,10):
    print('processing', i)
    #sys.stdout.write(f"{i} ")
    if i % 2 == 0:
        print('even number', i)
        #sys.stdout.write("\n")