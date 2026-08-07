class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #the idea is storing the index of the unresolved elements for resolving infurther iteration
        stack,best=[],0
        for i in range(len(heights)+1): #height+1 because stack index starts from -1 hence gives actual length-1 as answer so we add +1 in range to touch all indexes
            cur= 0 if i==len(heights) else heights[i] #cur=0 for last element as its already in the logic of second last element so no need to invovle again
            while stack and cur<heights[stack[-1]]: # check for stack empty and check if cur height is less than height of element whose index stored in stack which is unresolved 
                h=heights[stack.pop()] # if above condn true pop the top frm stack and the result becomes the index for the height
                left=stack[-1] if stack else -1 #calculate left which is unresolved elemnts 
                best=max(best,h*(i-left-1)) #update max 
            stack.append(i)# pushing of unresolved elements if above condition doesnt satisfy
        return best 
        