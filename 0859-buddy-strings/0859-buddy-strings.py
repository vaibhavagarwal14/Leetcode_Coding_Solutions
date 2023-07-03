class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # n=len(s)
        # m=len(goal)
        # if(n!=m):
        #     return False
        # c=0
        # sc={}
        # gc={}
        # sl=[]
        # gl=[]
        # for i in range(n):
        #     if(s[i]!=goal[i]):
        #         c+=1
        #         sl.append(s[i])
        #         gl.append(goal[i])
        #     if s[i] in sc:
        #         sc[s[i]]+=1
        #     else:
        #         sc[s[i]]=1
        #     if(goal[i] in gc):
        #         gc[goal[i]]+=1
        #     else:
        #         gc[goal[i]]=1
        # sl.sort()
        # gl.sort()
        # if(c==2 and sl==gl):
        #     return True
        # myKeys = list(sc.keys())
        # myKeys.sort()
        # stc = {i: sc[i] for i in myKeys}
        # myKeys = list(gc.keys())
        # myKeys.sort()
        # gtc = {i: gc[i] for i in myKeys}
        # f=0
        # for i in stc:
        #     if(stc[i]>=2 and gtc[i]>=2):
        #         f=1
        #         break
        # if(c==0 and f==1):
        #     return True
        # return False
        
        #Optimised Code
        
        if(len(s)!=len(goal)):
            return False
        if(s==goal and len(set(s))<len(s)):
            return True
        diff=[(a,b) for a,b in zip(s,goal) if a!=b]
        if len(diff)==2 and diff[0]==diff[1][::-1]:
            return True
        return False