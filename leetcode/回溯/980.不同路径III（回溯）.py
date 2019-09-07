class Solution:
    def __init__(self):
        self.grid = None
        self.result = None
#        self.path = []
        
    def uniquePathsIII(self, grid):
        
        def isValid(visited,x,y):
            if 0<=x<m and 0<=y<n and visited[x][y] != 1:
                return True
            else:
                return False
            
        def back(visited,step,path,x,y):
            walk_dir = [[1,0],[0,1],[-1,0],[0,-1]]
            if x==end[0] and y==end[1] and step==steps:
                self.result.append(path)
                return 
            
            for direction in walk_dir:
                next_x = x+direction[0]
                next_y = y+direction[1]               
                if isValid(visited,next_x,next_y):
                    visited[next_x][next_y] = 1
                    new_path = path.copy()
                    new_path.append([next_x,next_y])
                    back(visited,step+1,new_path,next_x,next_y)
                    
                    visited[next_x][next_y] = 0

                           
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        steps = 0
        self.result = []
#        path = []

        for i in range(m):
            for j in range(n):
                num = grid[i][j]
                if num==1:
                    start = [i,j]
                    visited[i][j] = 1
                elif num==2:
                    end = [i,j]
                    steps += 1
                elif num==-1:
                    visited[i][j] = 1
                else:
                    steps += 1
        
        back(visited,0,[start],start[0],start[1])
        return len(self.result)
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
so = Solution()
res = so.uniquePathsIII(grid)
print(len(res))
      

