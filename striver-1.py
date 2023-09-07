#User function Template for python3

class AutoCompleteSystem():
    def __init__(self, sentences, times):
        # write code for constructor
        self.thisdict = {}
        for i in range(len(sentences)):
            self.thisdict[times[i]] = sentences[i]
        reversed(sorted(self.thisdict.items()))
        
        
    
    def input(self,c):
        '''
            write code to return the top 3 suggestions when the current character in the stream is c
            c == '#' means , the current query is complete and you may save the entire query into
            historical data
        '''
        print(c)
        
        return self.thisdict

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    for _ in range(int(input("Enter number of lists for input"))):
        n = int(input("Enter Value for n"))
        sentences = ['']*n
        times = [0]*n
    for i in range(n):
        sentences[i] = input("Enter Value for sentence")
        times[i] = int(input("Enter Value for iterations"))

    obj = AutoCompleteSystem(sentences,times)
    q = int(input("Enter number of queries"))
    for i in range(q):
        query = input("Enter The query")
        qq = ""
        for x in query:
            qq+=x
            suggestions = obj.input(x)
            if(x=='#'):
                continue
            print('Typed : "%s" , Suggestions: ' %(qq))
            for y in suggestions:
                print(y)
# } Driver Code Ends