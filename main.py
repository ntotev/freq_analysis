"""
Challenge #1

Write a function that takes a paragraph of text and returns a dictionary containing the frequency of each word.
"""
def par_int (text):
  words = text.lower().split()
  frequency = {}
  for i in words:
    if i.isalpha():
      if i in frequency:
        frequency[i]+=1
      else:
        frequency[i]=1
  return frequency

text = "Once upon a time, in a quaint little village, there lived a curious cat named Whiskers. Whiskers, with his sleek black fur and bright green eyes, had a penchant for exploring every nook and cranny of the village. Village folks often chuckled at Whiskers' antics, but they couldn't deny the charm he brought to their quiet lives.One sunny afternoon, Whiskers decided to embark on a particularly adventurous adventure. Adventure, you see, was the essence of Whiskers' existence. He sauntered down the cobblestone streets, streets that had witnessed countless tales of everyday life.Life in the village was simple, simple yet filled with joy. Joy echoed through the laughter of children playing in the meadows and the cheerful chatter of neighbors sharing stories. Stories that became woven into the fabric of the community.Community spirit thrived, thrived like the vibrant flowers that adorned the village square. Square dances on festive occasions united young and old, old memories mingling with new ones.On this day, however, something extraordinary happened. Happened in a way that would be talked about for generations. Generations to come would recount the day Whiskers, with his mischievous charm, stumbled upon a mysterious portal. A portal hidden in the depths of the ancient forest, forest that whispered secrets to those who dared to listen.Listen carefully, for the tale unfolds as Whiskers, with wide-eyed curiosity, curiosity that mirrored the villagers', stepped through the shimmering portal. Portal to a realm unknown, unknown to both cat and villager alike.Alike in their fascination, fascination that bound the two worlds together. Together, they would discover the magic that dwelled in the ordinary and the extraordinary. Extraordinary adventures awaited, awaited on the other side of that magical portal, portal that beckoned with promises of enchantment.Enchantment filled the air as Whiskers took his first step into the unknown. Unknown wonders awaited him, him who had a heart as adventurous as the tales that echoed through the village. Village and cat, cat and village, intertwined in a story that repeated itself with each new chapter, chapter that unfolded in the enchanting embrace of the unknown."
result = par_int(text)
print(result)



"""
Challenege #2

Write a function to check if a number is prime.
"""

def prime_finda(num):
  if num <= 1:
    return False
  for i in range(2,num):
    if num%i == 0:
      return False
  return True

print(prime_finda(406))
print(prime_finda(11))
print(prime_finda(29))
print(prime_finda(8949263978469238742))
print(prime_finda(123))
print(prime_finda(127))

