class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        nt=ord(target)
        for i in range(len(letters)):
            ni=ord(letters[i])
            if(ni==nt and i!=len(letters)-1):
                if(letters[i+1]!=letters[i]):
                    return letters[i+1]
                else:
                    continue
            elif(ni>nt):
                return letters[i]
        return letters[0]