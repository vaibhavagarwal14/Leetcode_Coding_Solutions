class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b=0
        c=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                b+=1
        c=sum(min(secret.count(x),guess.count(x)) for x in set(guess))
        res=str(b)+"A"+str(c-b)+"B"
        return res