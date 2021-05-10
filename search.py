# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# William Taylor
# 010840237
# wjtaylor@uark.edu
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    stack = util.Stack()
    expanded = util.Counter()
    start = problem.getStartState()
    stack.push((start, []))

    while not stack.isEmpty():
      nextNode = stack.pop()
      coordinate = nextNode[0]
      answer = nextNode[1]

      if problem.isGoalState(coordinate):
        return answer

      if coordinate not in expanded:
          expanded.__getitem__(coordinate)
          for i in problem.getSuccessors(coordinate):
              if i[0] not in expanded:
                  stack.push((i[0], answer + [i[1]]))


def breadthFirstSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    queue = util.Queue()
    expanded = util.Counter()
    start = problem.getStartState()
    queue.push((start, []))

    while not queue.isEmpty():
        nextNode = queue.pop()
        coordinate = nextNode[0]
        answer = nextNode[1]

        if problem.isGoalState(coordinate):
            return answer
        if coordinate not in expanded:
            expanded.__getitem__(coordinate)
            for i in problem.getSuccessors(coordinate):
                if i[0] not in expanded:
                    queue.push((i[0], answer + [i[1]]))

def uniformCostSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    queue = util.PriorityQueue()
    expanded = util.Counter()
    start = problem.getStartState()
    queue.push((start, []), 0)

    while not queue.isEmpty():
      nextNode = queue.pop()
      coordinate = nextNode[0]
      answer = nextNode[1]

      if problem.isGoalState(coordinate):
          return answer
      if coordinate not in expanded:
          expanded.__getitem__(coordinate)
          for i in problem.getSuccessors(coordinate):
              if i[0] not in expanded:
                  cost = problem.getCostOfActions(answer + [i[1]])
                  queue.push((i[0], answer + [i[1]]), cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    queue = util.PriorityQueue()
    expanded = util.Counter()
    start = problem.getStartState()
    queue.push((start, []), 0)

    while not queue.isEmpty():
        nextNode = queue.pop()
        coordinate = nextNode[0]
        answer = nextNode[1]

        if problem.isGoalState(coordinate):
            return answer
        if coordinate not in expanded:
            expanded.__getitem__(coordinate)
            for i in problem.getSuccessors(coordinate):
                if i[0] not in expanded:
                    cost = problem.getCostOfActions(answer + [i[1]])
                    queue.push((i[0], answer + [i[1]]), cost + heuristic(i[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
