'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

  count = 0
  substring = "th"

  # find the substring in word
  substring_index = word.find(substring) 

  if substring_index >= 0:

    #increment count
    cur_count = count + 1
    print(cur_count)

    # slice off word from where substring is found
    sliced_word = word[substring_index + len(substring):]
    print("word-slice", sliced_word)

    # increment count and recursively call count_th
    count = cur_count + count_th(sliced_word)
  
  return count

print(count_th("thethetoothhurts"))