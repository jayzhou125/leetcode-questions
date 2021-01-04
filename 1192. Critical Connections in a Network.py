class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)
            
        # print(g)
        jump = [-1] * n
        
        """
        start fron the current node, explore all the node conecting to this node except for its parent, and return minimum value node.
        """
        def dfs(cur:int , par:int, lvl: int, jump:list, res:list, g) -> int:
            jump[cur] = lvl + 1
            for child in g[cur]:
                if child == par:
                    continue
                elif jump[child] == -1:
                    jump[cur] = min(jump[cur], dfs(child, cur, lvl+1, jump, res, g))
                else:
                    jump[cur] = min(jump[cur], jump[child])
                    
            if jump[cur] == lvl + 1 and cur != 0:
                res.append([par, cur])
            return jump[cur]
        
        res = []
        dfs(0, -1, 0, jump, res, g)
        return res
