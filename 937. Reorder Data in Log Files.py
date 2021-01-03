class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # leetcode solution:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            if rest[0].isalpha():
                return (0, rest, _id) 
            else:
                return (1, ) 

        return sorted(logs, key=get_key)
    
        # another way without using sorted():
#         letters = []
#         numbers = []
        
#         for log in logs:
#             if log.split(" ", 2)[1].isnumeric() == False:
#                 letters.append(log)
#             else:
#                 numbers.append(log)
                
#         letters = sorted(letters, key = lambda log: (log.split(" ", 2))[0])
#         letters = sorted(letters, key = lambda log: (log.split(" "))[1: ])
                
#         return letters+numbers
