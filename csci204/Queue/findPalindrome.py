'''
Find Palindromes in Tweets

Tung Tran
'''
from FastPriorityQ import *
import time

NUM_TESTS = 10
FILE_NAME = 'bucknell_tweets.txt'
OUTPUT_FILE = 'palindromes.txt'
NUM_WORDS_PER_LINE = 40

def is_palindrome(word):
    '''
    Check if word is a palindrome
    
    :param word: String
    :return: Boolean
    '''
    word = word.decode('utf-8')
    if word[0] == '#':
        return False
    
    for i in range( len(word) // 2 ):
        if word[i].lower() != word[ len(word)-1 - i ].lower():
            return False
    return True


def find_palindrome(file_name):

    '''
    Function to find all palindromes in a file (for word of length > 2)
    
    :param file_name: File name of tweets file
    :return: Priority Queue of palindromes 
    '''
    # Timing
    start = time.process_time()
    
    # Find max length of all palindrome 
    # (cuz it's so inexpensive to find palindromes)
    max_length = 0
    with open(file_name, 'rb') as f:
        for line in f.readlines():
            line = line.strip().split()
            
            for word in line:
                if is_palindrome(word) and len(word) > max_length:
                    max_length = len(word)
    global pQueue
    pQueue = FastPriorityQueue(min_priority=max_length)
                
    # Open file
    with open(file_name, 'rb') as f:
        for line in f.readlines():
            # Clean up
            line = line.strip().split()
            
            # Add Palindromes to Queue
            for word in line:
                if is_palindrome(word):
                    word = word.decode('utf-8')
                    pQueue.enqueue( len(word), word )
                    
    # Write into file
    print( len(pQueue) )
    with open(OUTPUT_FILE, 'w') as f:
        count = 1
        for i in range( len(pQueue) ):
            item = pQueue.dequeue()
            if count % NUM_WORDS_PER_LINE == 0:
                f.write( '{},\n'.format(item) )
                count += 1
                continue
        
            f.write( '{},'.format(item) )
            count += 1

    return time.process_time() - start
    

def test_run_time(n=NUM_TESTS, file_name=FILE_NAME):
    '''
    Function to print average running time of function find_palindrome
    
    :param n: Times repeated
    :param file_name: File name of tweets file
    '''
    
    count = 0
    time_total = 0

    while count < n:
        time_total += find_palindrome(file_name)
        count += 1

    print(time_total/n)

   
def main():
    test_run_time()
              

if __name__ == '__main__':
    main()
