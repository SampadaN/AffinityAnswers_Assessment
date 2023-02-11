
#The file containing tweets is considered to be in csv format.

def  profanity(line):

#slurs represents the set of racial slurs
  slurs ={'blue','white','pink','black','indigo','purple','maroon','teal','green','red'}
  total = len(slurs)
  profanity_degree = 0
  
  for word in line:
  #words converted to lowercase to compare them with the words in the set.
    if(word.lower() in slurs):
      profanity_degree +=1

  #Degree of Profanity is taken as ---->
  #No. of slur words present in tweet / Total no of words in the set.
  return profanity_degree/total


tweets = open('tweets.csv','r')   #filename ---> tweets.csv

scores = tweets.readlines()[0:]
line_no = 0
for line in scores:
  t = list(line.strip().split(','))
  line_no += 1

  #DOF -----> Degree of Profanity
  print("Tweet no. ",line_no, "  DOF ---> ", profanity(t))

  #Output Sample based on tweets.csv
  '''
  Tweet no. 1  DOF ---> 0.3
  Tweet no. 2  DOF ---> 1.0
  Tweet no. 3  DOF ---> 0.0
  Tweet no. 4  DOF ---> 0.5
  Tweet no. 5  DOF ---> 0.3
  '''

  



