
###The self keyword is like a placeholder that refers to the
## current article we are creating.

class Article: ### 
    all_articles = []### CONTATAINER FOR ALL THE ARTICLES CREATED
    ## THIS WILL KEEP TRACK OF ALL  OF ALL THE ARTICLES 
    ##Whenever a new article is created, it will be added to the all_articles container so that we can access it later.

    def __init__(self, author, magazine, title):##>>> author, magazine, title THEY ARE TAKEN AS PARAMETERS
        ##  THE NEW ATICLE WIL HAVE   author, magazine, and title
        self._author = author        
        self._magazine = magazine   #### INSTANCE VARIABLES AND THERE VALUES 
        self._title = title

 
        self.all_articles.append(self) ### APPENDING THE CURRENT INSTANCE TO ALL_ARTICLES
        ####  

    def title(self):
        return self._title

    @classmethod
    def all(cls):### >>> IT AM METHORD  STANDS FOR CLASS 
        ## return cls.all_articles returns the value of cls.all_articles.
        return cls.all_articles

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine
