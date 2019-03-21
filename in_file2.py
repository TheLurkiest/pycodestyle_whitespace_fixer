"""
h2.py
practice with parsing and transforming str and list sequences
created by mihaela sabin
oct 2, 2018
"""

class problems:

    def keep_words(self, word_list):
        """
        parses word_list to create a list that have only alpha characters
        word_list: list of strings
        returns: list of strings that have only alpha characters

        test case 1:
            given: ['duck','fish','cat9','dog pig cow7','44']
            returns: ['duck','fish']

        test case 2:
            given: ['red','blue5','yellow 44']
            returns: ['red']

        test case 3:
            given: ['mouse4','mice3','3434','rat','mole']
            returns: ['rat','mole']

        """
        beehive=word_list
        honey_comb='drop'
        bad_honey=false
        output_hive=[]
        for bee in beehive:
            honey_comb=str(bee)
            print('current honey_comb is '+ str(honey_comb))
            for honey_drop in honey_comb:
                #print('honey drop is '+ str(honey_drop))
                if(honey_drop.isdigit()==true):
                    bad_honey=true
                    print('this word contains digits')
            if(bad_honey==false):
                print('this word did not contain digits')
                #print('adding current bee')
                output_hive.append(bee)
            else:
                bad_honey=false


        return output_hive

    def shorter_than_5(self, word_list):
        """
        parses word_list to create a list that has strings of length smaller
        than 5.
        word_list: list of words
        returns: list of strings of length smaller than 5

        test case 1:
            given: ['dog','catfish','snail','cow']
            returns: ['dog', 'cow']
        test case 2:
            given: ['cat','117','monkey']
            returns: ['cat','117']
        test case 3:
            given: ['zebra11','clam','bull','beaver']
            returns: ['clam', 'bull']

        """
        #snake_list=len(word_list)
        count_s=0
        length_blip=0
        output_list=[]
        for word_blips in word_list:
            length_blip=len(word_blips)
            if(length_blip < 5):
                output_list.append(word_blips)
        return output_list


    def gamble_calc(self, letter_list, selected_letter):
        """
        letters 'b' or 'r' will be at different indexes in a list, along with
        that there will be a string value of either one as the selection. you
        have to write code to return what are the odds it will land on the
        selected letter. round to the nearest whole number if a decimal
        value occurs.

        ex.
        gamble_calc(['b','b','r','b'], 'r')
        return = 25%
        gamble_calc(['b','b','r','b','r'], 'b')
        return = 60%

        test case 1)
        given:
            gamble_calc(['r','r','r','b'], 'r')
        returns:
            75% probability
        test case 2)
        given:
            gamble_calc(['r','r','r','b','b','r','r','r','r'], 'b')
        returns:
            22.22222 = 22%
        test case 2)
        given:
            gamble_calc(['r','r','r','b','r','r','r','r','r'], 'r')
        returns:
            88.89 = 89%
        """
        prob_win=0.0
        chipstack=letter_list
        r_tot=0
        b_tot=0

        for chip in chipstack:
            if (chip == 'r'):
                r_tot=r_tot+1
            else:
                b_tot=b_tot+1

        prob_r_win = int(100 * (r_tot / (r_tot + b_tot)) + 0.5)
        prob_b_win = int(100 * (b_tot / (r_tot + b_tot)) + 0.5)

        print('probability of b winning is '+ str(prob_b_win) +'%')
        print('probability of r winning is '+ str(prob_r_win) +'%')
        if(selected_letter == 'r'):
            return (str(prob_r_win) +'%')
        else:
            return (str(prob_b_win) +'%')

        # for param1 input we're getting a big list of single letter strings--
        # each either 'b' or 'r', along different indexes each time in the
        # list.
        # for param2 input we get a single string, one character long-- either
        # 'b' or 'r' again.  write code the will calculate the odds it will
        # land on param2's letter.
        # round to the nearest whole number if a decimal value occurs.

        # alright, rounding is simple-- just add 0.5 to our final calculation--
        # obviously, doing so if # is 2.5 or higher will result in 3.0 or
        # higher-- which means you can just truncate with int type casting
        # before returning i think.

    def time_left(self, start_time, end_time):
        """
        this will take two sperate times as string types and return how many
        hours and minutes in between as a string. in order to do math with the
        string values you will need to convert them into integers.

        then before
        you return they the final time will have to be converted back to string
        always assume that times are no more then 11:59 hours apart.

        ex.
        time_left('12:50', '5:00')
        return = '4:10'

        time_left('1:00', '12:59')
        return = '11:59'

        time_left('1:00', '1:05')
        return = '0:05'
        carful not to return 0:5 on this

        time_left('1:00', '1:00')
        return = '0:00'
        """


        # ok here's what we're doing: we're
        # given two 2 parameters showing time-- assuming that the two times
        # are < 12 hours apart, we need to determine-- and then return--
        # the difference in minutes and hours, between the first and 2nd
        # input paramters' times.

        # the 1st thing we're going to have to do, is grab the individual
        # values for the minutes, and hours, for each parameter.  the method
        # to do that is quite simple.
        t1_mid = start_time.find(':')
        t2_mid = end_time.find(':')#
        # now that we know where these are, we can simply use slicing like so:
        hour1 = start_time[:(t1_mid)]
        min1 = start_time[(t1_mid+1):]
        min2 = end_time[(t2_mid+1):]
        hour2 = end_time[:(t2_mid)]



        num_hr1=int(hour1)
        num_min1=int(min1)

        num_hr2=int(hour2)
        num_min2=int(min2)

        if(num_hr2 < num_hr1):
            num_hr2=12+num_hr2

        time_diff_hrs=num_hr2 - num_hr1
        time_diff_min=num_min2 - num_min1 # if num_min2 is > num_min1 then
        # it'll add more time to the total time spend-- toherwise it'll
        # subtract.


        print('number of hours at start are '+ str(hour1))
        print('number of minutes at start are '+ str(min1))

        print('number of hours at end are '+ str(hour2))
        print('number of minutes at end are '+ str(min2))


        output_hrs=time_diff_hrs
        if(time_diff_min >= 0 and time_diff_min < 60):# we add more time to elapsed time so far
            output_min=time_diff_min
            output_hrs=time_diff_hrs
        elif(time_diff_min > 60):
            output_hrs = output_hrs + 1
            output_min=time_diff_min
        elif(time_diff_min < 0):
            output_min=60 + time_diff_min
            output_hrs = output_hrs - 1

        output_min2=str(output_min)
        if(len(output_min2)==1):
            output_min2='0'+ str(output_min)


        # between 12 and 5 o'clock
        if (output_hrs>12):
            output_hrs=output_hrs-12
        final_full_time_output=(str(output_hrs)+':'+ str(output_min2))
        print('the amount of time that has passed so far is: '+ str(final_full_time_output))
        return (str(output_hrs)+':'+ str(output_min2))
