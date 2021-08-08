import time, random
raw_words="about|above|add|after|again|air|all|almost|along|also|always|America|an|and|animal|another|answer|any|are|around|as|ask|at|away|back|be|because|been|before|began|begin|being|below|between|big|book|both|boy|but|by|call|came|can|car|carry|change|children|city|close|come|could|country|cut|day|did|different|do|does|don't|down|each|earth|eat|end|enough|even|every|example|eye|face|family|far|father|feet|few|find|first|follow|food|for|form|found|four|from|get|girl|give|go|good|got|great|group|grow|had|hand|hard|has|have|he|head|hear|help|her|here|high|him|his|home|house|how|idea|if|important|in|Indian|into|is|it|its|it's|just|keep|kind|know|land|large|last|later|learn|leave|left|let|letter|life|light|like|line|list|little|live|long|look|made|make|man|many|may|me|mean|men|might|mile|miss|more|most|mother|mountain|move|much|must|my|name|near|need|never|new|next|night|no|not|now|number|of|off|often|oil|old|on|once|one|only|open|or|other|our|out|over|own|page|paper|part|people|picture|place|plant|play|point|put|question|quick|quickly|quite|read|really|right|river|run|said|same|saw|say|school|sea|second|see|seem|sentence|set|she|should|show|side|small|so|some|something|sometimes|song|soon|sound|spell|start|state|still|stop|story|study|such|take|talk|tell|than|that|the|their|them|then|there|these|they|thing|think|this|those|thought|three|through|time|to|together|too|took|tree|try|turn|two|under|until|up|us|use|very|walk|want|was|watch|water|way|we|well|went|were|what|when|where|which|while|white|who|why|will|with|without|word|work|world|would|write|year|you|young|your"
words=raw_words.split("|")  #words are from 10 fast fingers website
print("Hi this the a typing test!!! \nby Abhay")
print("\n INSTRUCTIONS:\n Type done after finishing \n")

num=int(input("Enter the num of words for test:"))
print()
print("------------------------------------------------------------")
print()
time.sleep(1)
x=random.choices(words,k=num)
for i in x:
    print(i, end=" ")

time.sleep(1)
start=time.time()
print()
user_in=input("START!!")

if "done" in user_in:
    end=time.time()
time_taken_min=round((end-start)/60,2)
wpm=round((len(x)+1)/time_taken_min,1) # added one cause of extra word done

user_in=user_in.split()
user_in.pop() # to remove the done word

correct=0 #no of coorect words
for j in range(len(user_in)):
    if user_in[j]==x[j]:
        correct+=1

accuracy=round((correct/len(x)*100),2)

print("------------------------------------------------------------")
print("TEST RESULTS!!!\n")
print("TIME TAKEN:",str((end-start)//60)+" min "+str(round((end-start)%60,2))+" sec")
print("WORDS PER MIN:",wpm)
print("ACCURACY:",accuracy,"%")
print("------------------------------------------------------------")
