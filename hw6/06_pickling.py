#pickling

mylist = ['a',123,[4,5,True]]
mylist
import pickle
f = open('mylist.pickle','w')
pickle.dump(mylist,f)
f.close
