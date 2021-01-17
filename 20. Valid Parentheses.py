class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0: return True
        
        stack = []
        matching = {")" : "(", "]" : "[",  "}" : "{"}

        for p in s:
            # if p is a close bracket, 
            if p == ')' or p == ']' or p == '}':
                # return False if the stack is empty
                if len(stack) == 0: 
                    return False    
                else:   
                    # check the top element of the stack
                    top = stack.pop() 
                    
                    # return False if the brackets not matching
                    if top != matching[p]:
                        return False
            
            else:  
                # p is open bracket, add p to stack
                stack.append(p)
                
        if len(stack) == 0: return True
        
        return False
