import os

def writeToFile(name_fileb,userSays1):
    with open('' + str(name_fileb), "w") as f:
            f.write(str(userSays1)+"\n")
    #file.write("My String\n")
    f.close()

def readFromFile(file_in):

    fin = open(file_in,"r")
    numLines = 0

    multi_line_list=[]

    numLines = 0
    lofs=[]

    for line in fin:

        numLines = numLines + 1
        if(numLines<25):
            print("line number "+str(numLines))
            print("original line: "+str(line))

        s3=str(line)
        s4=str(line)

        l1=["=","+","*","-"]
	breadcrumb1=0
	crumbtrails1=[]
	lastcrumb1=0
	crumb_seg=""
	crumb_count=0

	s5=""
	s7=""
	bread_out2=""
	bread_out=""

        for blips in l1:
	    print("current blip we use find to seek at start of for loop is "+str(blips))
	    print("the thing we are looking inside to find our blip is "+str(s3))
	    print("the other thing we COULD look inside is "+str(s4))
	    print( "length of s3 is " + str(len(s3)) )
	    if(len(s3)==0):
	        s3=s4
	    breadcrumb1=0
	    crumb_count=s3[breadcrumb1:].count(str(blips))
	    print("crumb_count is "+str(crumb_count))

	    while(crumb_count>=1):
		if(len(s5)>0):
		    s3=s4
       	        lastcrumb1=s3[(breadcrumb1+1):].find(str(blips)) + breadcrumb1
		print("index of next findblips is lastcrumb1 which is "+str(lastcrumb1))
		print("current blip we use find to seek is "+str(blips))

		print("s3 at lastcrumb1+1 index is "+str(s3[lastcrumb1+1]))
		print("...and s3 at lastcrumb1+2 index is "+str(s3[lastcrumb1+2]))

                if(s3[lastcrumb1+1] == s3[lastcrumb1+2] ):
                    print("debug statement double blip detected")
                    print("single blip being sliced out")
                    crumbtrails1.append(s3[breadcrumb1:lastcrumb1])

                    crumbtrails1.append(s4[lastcrumb1])

                    crumbtrails1.append(" ")

                    crumbtrails1.append(s4[lastcrumb1+1:lastcrumb1+2])

		    crumbtrails1.append(s4[lastcrumb1+1])

                    crumbtrails1.append(" ")


                    print("crumbtrails1 just after else7 is "+str(crumbtrails1))

                    bread_out2=bread_out + str("".join(crumbtrails1)) + "\n"
                    bread_out=bread_out2
                    breadcrumb1=lastcrumb1+4
                    s3=s7


                    crumb_count=crumb_count-1
                    crumb_count=s3[breadcrumb1:].count(str(blips))
                    if(crumb_count<=0 and len(s4)>=lastcrumb1+2):
                        crumbtrails1.append(s4[(lastcrumb1+3):] )
                    s4="".join(crumbtrails1)



		    #crumbtrails1.append(s4[lastcrumb1+1])


       	        else:
		    print("single blip being sliced out")
       	            crumbtrails1.append(s3[breadcrumb1:lastcrumb1])

       	            crumbtrails1.append(s4[lastcrumb1])
		    #if(str(crumbtrails1[-1]).isspace==False):
		    crumbtrails1.append(" ")
       	            crumbtrails1.append(s3[lastcrumb1+1])
		    #if(str(s4[(lastcrumb1+2)]).isspace==False):
		    crumbtrails1.append(" ")
		    print("crumbtrails1 just after else7 is "+str(crumbtrails1))
		    bread_out2=bread_out + str("".join(crumbtrails1)) + "\n"
		    bread_out=bread_out2
       	            breadcrumb1=lastcrumb1+2
		    s3=s7

		    crumb_count=crumb_count-1
	            crumb_count=s3[breadcrumb1:].count(str(blips))
		    if(crumb_count<=0 and len(s4)>=lastcrumb1+2):
		        crumbtrails1.append(s4[(lastcrumb1+2):] )
	            s4="".join(crumbtrails1)



	        crumbtrails1=[]

	    s5=s4+"\n"
	    print("s5 at this point is "+str(s5))
	    print("lofs at this point is "+str(lofs))
	    print("crumbtrails1 at this point is "+str(crumbtrails1))

        lofs.append(s5)

    # close fin object
    fin.close()

    s1= "".join(lofs)
    # s1= "\n".join(lofs)

    print("s1 just prior to output to out_file3 is "+str(s1))
    writeToFile("out_file3.txt",s1)

    multi_line_list=lofs

    # return result
    return multi_line_list


print("the function is about to be called")

fileContent=readFromFile("in_file2.py")

print("the function is complete")


