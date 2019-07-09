import lab05_util
restaurants=lab05_util.read_yelp('yelp.txt')

def print_info(rest):
    print('{} ({}))'.format(rest[0],rest[3]))
    add1=rest[3].split('+')
    print('\t{}\n\t{}'.format(add1[0],add1[1]))
    ave=sum(rest[6])/len(rest[6])
    print('Average Score: {:.2f}'.format(ave))
print(restaurants[0])
print(print_info(restaurants[0]))
print(print_info(restaurants[4]))