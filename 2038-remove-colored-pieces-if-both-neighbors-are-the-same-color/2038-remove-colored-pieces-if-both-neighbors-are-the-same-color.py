class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n=len(colors)
        if n<=2:
            return 0
        # t=0
        # while True:
        #     if t==0:
        #         f=0
        #         for i in range(1,n-1):
        #             if colors[i]=='A' and colors[i-1]=='A' and colors[i+1]=='A':
        #                 colors=colors[:i]+colors[i+1:]
        #                 n-=1
        #                 f=1
        #                 break
        #         if not f:
        #             return 0
        #         t=1
        #     else:
        #         f=0
        #         for i in range(1,n-1):
        #             if colors[i]=='B' and colors[i-1]=='B' and colors[i+1]=='B':
        #                 colors=colors[:i]+colors[i+1:]
        #                 n-=1
        #                 f=1
        #                 break
        #         if not f:
        #             return 1
        #         t=0
        
        a=0
        for i in range(1,n-1):
            if colors[i]=='A' and colors[i-1]=='A' and colors[i+1]=='A':
                a+=1
            if colors[i]=='B' and colors[i-1]=='B' and colors[i+1]=='B':
                a-=1
        if a>0:
            return 1
        return 0