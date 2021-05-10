
The following files are they only ones I have altered (the rest were given by the instructor, most of the others are just to display the final path the algorithms find):
search.py
searchAgents.py

In this assignment we made 4 search algorithms Located in search.py: 
breadth First Search
depth First Search
Star* Search
uniform Cost Search

Running program:
WORKS WITH ANACONDA3 (Might work with other python platforms)
DO the commands following in anaconda3 prompt to create enviornment:

Conda create –n env_name python=2.7
Conda activate env_name 

To run a pacman search do:
python pacman.py -l [maze type] -p [agent type] -a fn=[search type]

The display after a command is the path the agent found. The search happens too fast to display the full process.
example:
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

Maze types:
tinyMaze, mediumMaze, bigMaze, mediumDottedMaze, mediumScaryMaze, tinyCorners, trickySearch, bigSearch
**In this assignment pacman does not know to avoid ghosts (ScaryMaze types)

agent types: 
SearchAgent
(GoWestAgent and StayEastSearchAgent also exist but they only go left/stay right respectively)

search types:
bfs
dfs
astar
ucs

Full list of example commands:
python pacman.py
python pacman.py --layout testMaze --pacman GoWestAgent
python pacman.py --layout tinyMaze --pacman GoWestAgent
python pacman.py -h
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python eightpuzzle.py
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
python pacman.py -l bigSearch -p ApproximateSearchAgent -z .5 -q 

