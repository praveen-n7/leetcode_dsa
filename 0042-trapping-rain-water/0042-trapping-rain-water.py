class Solution:
    def trap(self, height: List[int]) -> int:
        #l,lm,r,rm=1,0,len(height)-2,len(height)-1 took lm and rm as index/pointers and moving it instaed make them the max value and not pointers
        l,r=0,len(height)-1
        rm=lm=w=0
        while(l<r):
           # if(height[lm]<=height[rm]): must check the moving pointers and not fixed one 
            if(height[l]<=height[r]):

                if(height[l]<=lm):
                  #w+=height[lm]-height[l] msitake
                  w+=lm-height[l]
                  l+=1
                else :
                  lm=height[l]
                  l+=1
            else :
                if(height[r]<=rm):
                  w+=rm-height[r]
                  r-=1
                else :
                     rm=height[r]
                     r-=1
            
            
        return w
