

class Node:
      def __init__(self,location,last_Node,last_direction):
            self.location=location
            self.last_Node=last_Node
            self.last_direction=last_direction
      def set_up_down_left_right_location(self):
            now_location=self.location
            up_location=[now_location[0]-1,now_location[1]]
            down_location=[now_location[0]+1,now_location[1]]
            left_location=[now_location[0],now_location[1]-1]
            right_location = [now_location[0], now_location[1] + 1]
            self.around_Node=[]#默认0为上，1为下，2为左，3为右
            if Maze[up_location[0]][up_location[1]]!=1 and self.last_direction!=1:
                  self.around_Node.append(Node(up_location,self,0))
            else:
                  self.around_Node.append(None)
            if Maze[down_location[0]][down_location[1]]!=1 and self.last_direction!=0:
                  self.around_Node.append(Node(down_location,self,1))
            else:
                  self.around_Node.append(None)
            if Maze[left_location[0]][left_location[1]] != 1 and self.last_direction!=3:
                  self.around_Node.append(Node(left_location,self,2))
            else:
                  self.around_Node.append(None)
            if Maze[right_location[0]][right_location[1]] != 1 and self.last_direction!=2:
                  self.around_Node.append(Node(right_location,self,3))
            else:
                  self.around_Node.append(None)

def print_maze_copy(maze):
      for line in maze:
            print(line)
      print("")
def search_exit(search_Node):
      if search_Node==None or search_Node.location in close_list:
            '''如果search_Node这个位置1或者这个点已经重复走过了'''
            return
      if search_Node.location==[exit_location[0],exit_location[1]]:
            '''如果找到了出口，打印路径并返回'''
            have_path[0]=True
            print("其中一条路径可以为：")
            print_path(search_Node)
            for i in path:
                  print_maze_copy(i)
            print("")
            path.clear()
            return
      search_Node.set_up_down_left_right_location()
      for around_node in search_Node.around_Node:
            '''搜索周围的四个节点'''
            close_list.append(search_Node.location)
            search_exit(search_Node=around_node)
            close_list.remove(search_Node.location)
def print_path(lower_Node):
      '''回溯记录路径'''
      Maze_copy = return_copy_maze()
      Maze_copy[lower_Node.location[0]][lower_Node.location[1]] = 3
      path.insert(0,Maze_copy)
      if lower_Node.location==[1,0]:
            return
      print_path(lower_Node.last_Node)
def search_exit_location(Maze):
      for i in range(len(Maze)):
            for j in range(len(Maze[i])):
                  if Maze[i][j]==2:
                        return [i,j]
      return None
def return_copy_maze():
      Maze_copy = []
      for line in Maze:
            a = []
            for i in line:
                  a.append(i)
            Maze_copy.append(a)
      return Maze_copy




Maze=[[1,1,1,1,1,1,1,1,1,1,1],
      [0,0,0,0,0,0,1,1,1,1,1],
      [1,1,1,0,1,0,0,0,0,0,1],
      [1,0,0,0,0,1,0,1,1,1,1],
      [1,0,1,0,1,0,0,0,0,0,1],
      [1,0,1,0,0,0,1,0,1,0,1],
      [1,0,0,1,1,1,1,1,1,0,1],
      [1,1,0,0,0,0,0,0,0,1,1],
      [1,0,0,1,0,1,0,1,0,0,2],
      [1,1,1,1,1,1,1,1,1,1,1]]
entrance_location=[1,0]
exit_location=search_exit_location(Maze=Maze)
close_list=[]
path=[]
have_path=[False]
#每个结点里面存储了
init_Node=Node(entrance_location,None,3)
search_exit(init_Node)
if not have_path[0]:
      print("不存在通往终点的路径")
