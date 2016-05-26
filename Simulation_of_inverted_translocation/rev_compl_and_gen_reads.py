#!/usr/bin/python2.7
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

file= open("test.tsv")

for seq in file:
    seq= seq.rstrip()
    seq_list=list(seq)
    
############### Taking inputs from user for i, j and k #################


start=input("Enter start postion or i: " )
stop=input("\nEnter stop postion or j: " )

if start>stop:
    '''
        Quiting the program if start location is greater than
        stop location. User will have to rerun the program
    '''
    print 'Start cannot be greater than stop location.. try again\n'
    quit()

insert_position=input("\nEnter insert postion or k: " )
print "\n"





################ Function to get DNA stretch ###########################
def get_sequence(start, stop):
    '''
        This function takes the start and stop locations from user
        and returs stretch of nucleotides
    '''
    DNA_stretch = seq_list[start-1:stop]
    return DNA_stretch


DNA_stretch= get_sequence(start, stop)    
print 'DNA_stretch: ', "".join(DNA_stretch), '\n\n'




######### Function to return reverse compliment of DNA strecth ##########
def reverse_complement(seq):
    '''
        This function takes the strech of DNA from 'get_sequence'
        function and returs reverse complimented stretc
    '''

    reverse_seq_list=seq[::-1]
    reverse_complemented=[]
    seq_dict = {'T':'A','A':'T','G':'C','C':'G'}
    reverse_complemented="".join(map(lambda x: seq_dict[x] , reverse_seq_list))
    return reverse_complemented

reverse_complemented = reverse_complement(DNA_stretch)

print 'reverse_complemented: ' ,"".join(reverse_complemented ), '\n\n'



## Printing the remaining sequence left after deleting the strech of DNA ###
remaining_sequence= "".join(seq_list[0:start-1]) + "".join(seq_list[stop:len(seq_list)])
print 'remaining_sequence: ' ,"".join(remaining_sequence), '\n\n'




##### Function to insert the reverse complimented DNA stretch #########

def insert_reverse_complement(string, index):
    '''
        This function inserts the reverse complimented DNA stretch
        at the given index by user
    '''
        
    return string[:index] + reverse_complemented  + string[index:]
    
final_sequence = insert_reverse_complement(remaining_sequence,insert_position)

print 'final_sequence ' , insert_reverse_complement(remaining_sequence,insert_position)




### Writing final sequence ina file called final_sequence.txt##############
final_sequence_file = open('final_sequence.txt', 'w')
final_sequence_file.write(final_sequence)
final_sequence_file.close()



######################## Generating random sequences ####################
import random
count=0

random_sequence_file = open('random_sequences.txt', 'w')

for i in range(0,100):
    count+=1
    
    '''
        Random index generated could not be greater than length of final
        sequnce - 150 else array index will go out of bound (no sequence
        to fetch)
    '''
    random_position = random.randint(0,len(final_sequence)-150)

    final_sequence=list(final_sequence)

    '''
        Writing random sequences to file
    '''

    random_sequence_file.write('>' + str(count) + '\n')
    random_sequence_file.write("".join(final_sequence[random_position:random_position+150])  + '\n\n')
    

random_sequence_file.close()
    
    
print "\n\nFiles written in the same folder: check final_sequence.txt and random_sequences.txt ... !!\n\n"
















