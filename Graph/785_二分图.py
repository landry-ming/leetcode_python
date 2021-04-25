class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):  ### 是为了防止孤立节点的存在
            queue = []                  ### 每一次开始生成一个queue， 若该节点被看过， 说明在上次的循环中看过该节点， 跳过该循环即可。
            if node not in color:
                color[node] = 1
                queue.append(node)
            
            while queue:
                cur = queue.pop(0)
                for next_node in graph[cur]:
                    if next_node not in color:
                        color[next_node] = color[cur] ^ 1
                        queue.append(next_node)
                    else:
                        if color[next_node] == color[cur]:
                            return False
        return True
                

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            stack = []
            if node not in color:
                color[node] = 1
                stack.append(node)
            
            while stack:
                cur = stack.pop()
                for next_node in graph[cur]:
                    if next_node not in color:
                        color[next_node] = color[cur] ^ 1
                        stack.append(next_node)
                    else:
                        if color[next_node] == color[cur]:
                            return False
        return True