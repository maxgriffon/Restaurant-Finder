import lab05_util
restaurants=lab05_util.read_yelp('yelp.txt')
ID=int(input('Enter restaurant ID from (1 to{}):'.format(len(restaurants))))
ID-=1
def print_info(rest):
    print('{} ({}))'.format(rest[0],rest[3]))
    add1=rest[3].split('+')
    print('\t{}\n\t{}'.format(add1[0],add1[1]))
    if (len(rest[6])>2):
        ave=(sum(rest[6])-(max(rest[6])+min(rest[6])))/len(rest[6])
        if (ave>=0 and ave<2):
            print(' This restaurant is rated bad, based on {} reviews.'.format(len(rest[6])))
        elif (ave>=2 and ave<3):
            print('This restaurant is rated average, based on {} reviews.'.format(len(rest[6])))
        elif (ave>=3 and ave<4):
            print('This restaurant is rated above average, based on {} reviews.'.format(len(rest[6])))
        elif (ave>=4 and ave<5):
            print('This restaurant is rated very good, based on {} reviews.'.format(len(rest[6])))
    else:
        ave=sum(rest[6])/len(rest[6])
        if (ave>=0) and (ave<2):
            print(' This restaurant is rated bad, based on {} reviews.'.format(len(rest[6])))
        elif (ave>=2 and ave<3):
            print('This restaurant is rated average, based on {} reviews.'.format(len(rest[6])))
        elif (ave>=3 and ave<4):
            print('This restaurant is rated above average, based on {} reviews.'.format(len(rest[6])))
        elif (ave>=4 and ave<5):
            print('This restaurant is rated very good, based on {} reviews.'.format(len(rest[6])))        
        
if ID<0 or ID>=156:
    print('error')
else:
    print_info(restaurants[ID])