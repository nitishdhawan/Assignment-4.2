
# coding: utf-8

# In[2]:


def WordsCount(wordsArray):
  lengthArray =[]
  lengthArray=[len(a) for a in wordsArray]
  print(lengthArray)
  
WordsCount(["abc","defg","nitish"])


# In[15]:


vowel = "aeiou"
def Input():
    userInput = input("Enter a Letter")
    if(len(userInput)>1):
        print("please enter single letter")
        Input()
    else:
        if(userInput in vowel ):
            return True
        else:
            return False
        
        
result = Input()
print(result)

