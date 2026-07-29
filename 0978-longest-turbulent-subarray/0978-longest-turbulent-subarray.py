class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up=down=best=1
        for i in range(1,len(arr)):
            if(arr[i-1]<arr[i]):
                up,down=down+1,1 #track length of even pos,up is the continuation of odd pos that is down in the loop
            elif(arr[i-1]>arr[i]):
                down,up=up+1,1#continue the track of even with odd pos thats why down added with up 
            else:
                up,down=1,1 #reset values if any of the above condition does not meet
            best=max(best,up,down)
        return best
        