import math
import random


def height(dist=5,hits=1):
    l0=math.sqrt(25+dist**2)
    l=l0+10*hits
    ysq=(l**2)*(25/(25+dist**2))
    return math.sqrt(ysq)


# for dist in range(5,121,5):
#     f.write("For *{}* feet starting range and for \n1hit    |   2hits     |     3hits   |     4hits     the height is: ".format(dist))
#     f.write("{:05.2F}ft |   {:05.2F}ft   |     {:05.2F}ft |     {:05.2F}ft   for :".format(height(dist,1),height(dist,2),height(dist,3),height(dist,4)))
#     f.write("{}d6     |   {}d6       |     {}d6     |     {}d6       Fall Damage".format(int(round(height(dist,1)/10,0)),int(round(height(dist,2)/10,0)),int(round(height(dist,3)/10,0)),int(round(height(dist,4)/10,0))))
#     f.write()

# Run once to create file if not exists:
# f=open("output.txt","x")
# f.close()


# Output in file:
# f=open("output.txt","a")
#
# for dist in range(5,121,5):
#     f.write("For *{}* feet starting range and for \n1hit      |  2hits  |  3hits  |  4hits  |  5hits  |  6hits  |  7hits  |  8hits  |  9hits  |  10hits |  11hits |  12hits     the height is: \n".format(dist))
#     for hits in range(1,13):
#         f.write("{:05.2F}ft ".format(height(dist,hits)))
#         if(hits<12):
#             f.write("|")
#         else:
#             f.write("    For:\n")
#     for hits in range(1,13):
#         f.write("{}d6     ".format(int(round(height(dist,hits)/10,0))))
#         if(hits<12):
#             f.write(" |")
#         else:
#             f.write("    dice of Damage\n")
#
# f.close()



#Output in console:
for dist in range(5,121,5):
    print("For *{}* feet starting range and for \n1hit    |  2hits  |  3hits  |  4hits  |  5hits  |  6hits  |  7hits  |  8hits  |  9hits  |  10hits |  11hits |  12hits     the height is: ".format(dist))
    for hits in range(1,13):
        print("{:05.2F}ft ".format(height(dist,hits)),end="")
        if(hits<12):
            print("|",end=" ")
        else:
            print("    For:")
    for hits in range(1,13):
        print("{}d6     ".format(int(round(height(dist,hits)/10,0))),end="")
        if(hits<12):
            print("|",end=" ")
        else:
            print("    dice of Damage")
