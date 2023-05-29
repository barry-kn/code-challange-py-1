# #!/usr/bin/env python3
# import ipdb;


# if __name__ == '__main__':
# #  WRITE YOUR TEST CODE HERE ###









# # DO NOT REMOVE THIS
#     ipdb.set_trace()

###  IMPORT THE CLASSES 
##  CREAT THE OUTHERS   USING AUTHERS  CLASS

 
import ipdb
from Magazine import Magazine
from Author import Author
from Article import Article

if __name__ == '__main__':
     
    author1 = Author("barry klein")
    author2 = Author("james kinuithia")
    author3 = Author("cleith")
    author4 = Author("kimani")
    author5 = Author("poul")
    author6 = Author("cleith")
    magazine1 = Magazine("Nairobian", "food")
    magazine2 = Magazine("Daily Nation", "cars")
    magazine3 = Magazine("The bigO", "The O")
    magazine4 = Magazine("sport M", "all sport")
    magazine5 = Magazine("Music M", "the heats")
    magazine6 = Magazine("FuN", "Trip Naivasha")
    
    article1 = Article(author1, magazine1, "what to eat to be healthy")
    article2 = Article(author2, magazine1, "which is the most laxurious car")

    print(magazine4.category())
    print(author1.name())
    print(article2.author())
    print(magazine2.name())
    print(article1.title())
   

    






    
    ipdb.set_trace()
