##We have provided a pack of tarot cards, tarot. You are going to do a three card spread of your past, present, and future.

Create an empty dictionary called spread.

Checkpoint 2 Passed
2.
The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.

Checkpoint 3 Passed

Stuck? Get a hint
3.
The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.

Checkpoint 4 Passed
4.
The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.

Checkpoint 5 Passed
5.
Iterate through the items in the spread dictionary and for each key: value pair, print out a string that says:

Your {key} is the {value} card.




tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread ={}
spread["past"] = tarot.pop(13,0)
print(spread)
spread["present"] = tarot.pop(22,0)
spread["future"] = tarot.pop(10,0)
for key,value in spread.items():
  print("Your "+str(key)+" is the "+value+" card. ")