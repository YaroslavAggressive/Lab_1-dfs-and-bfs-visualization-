import pytest
import networkx as nwx
from GraphVisual import MyGraph


class Case:
    def __init__(self, name: str, input: dict, start_node: str, expected: list):
        self._name = name  #
        self.expected = expected  # требуемая последовательность вершин после bfs/dfs
        self.start_node = start_node  # вершина откуда ищем в глубину/ширину
        self.input = input  # сам граф

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


dict_1 = {'A': ['C', 'D'],
          'B': [],
          'C': ['B', 'D'],
          'D': ['A', 'C', 'E'],
          'E': ['A', 'D']}
G_1 = nwx.Graph(dict_1)
res_1 = list(nwx.algorithms.traversal.dfs_tree(G_1, 'A'))

dict_2 = {'A': ['C', 'D'],
          'B': ['A', 'S'],
          'C': ['B', 'D'],
          'D': ['A', 'C', 'E'],
          'E': ['A', 'D']}
G_2 = nwx.Graph(dict_2)
res_2 = list(nwx.algorithms.traversal.dfs_tree(G_2, 'A'))

dict_3 = {'A': ['C', 'D'],
          'B': ['A', 'S'],
          'C': ['B', 'Y'],
          'D': ['A', 'C', 'A'],
          'E': []}
G_3 = nwx.Graph(dict_3)
res_3 = list(nwx.algorithms.traversal.dfs_tree(G_3, 'A'))

dict_4 = {'A': ['D'],
          'B': ['A', 'S'],
          'C': ['B', 'D'],
          'D': ['A', 'C', 'E'],
          'E': ['A', 'D']}
G_4 = nwx.Graph(dict_4)
res_4 = list(nwx.algorithms.traversal.dfs_tree(G_4, 'A'))

dict_5 = {'A': ['C', 'D'],
          'B': ['A', 'S'],
          'C': ['B', 'D'],
          'D': ['B', 'B', 'E'],
          'E': ['A', 'D']}
G_5 = nwx.Graph(dict_5)
res_5 = list(nwx.algorithms.traversal.dfs_tree(G_5, 'A'))

dict_6 = {'A': ['C', 'D'],
          'B': ['A', 'S'],
          'C': ['B', 'D'],
          'D': ['A', 'C', 'E'],
          'E': ['A']}
G_6 = nwx.Graph(dict_6)
res_6 = list(nwx.algorithms.traversal.dfs_tree(G_6, 'A'))

TEST_CASES_FOR_DFS = [
    Case(name='№1', input=dict_1, start_node='A', expected=res_1),
    Case(name='№2', input=dict_2, start_node='A', expected=res_2),
    Case(name='№3', input=dict_3, start_node='A', expected=res_3),
    Case(name='№4', input=dict_4, start_node='A', expected=res_4),
    Case(name='№5', input=dict_5, start_node='A', expected=res_5),
    Case(name='№6', input=dict_6, start_node='A', expected=res_6)
]


res_1 = list(nwx.algorithms.traversal.bfs_tree(G_1, 'A'))
res_2 = list(nwx.algorithms.traversal.bfs_tree(G_2, 'A'))
res_3 = list(nwx.algorithms.traversal.bfs_tree(G_3, 'A'))
res_4 = list(nwx.algorithms.traversal.bfs_tree(G_4, 'A'))
res_5 = list(nwx.algorithms.traversal.bfs_tree(G_5, 'A'))
res_6 = list(nwx.algorithms.traversal.bfs_tree(G_6, 'A'))

# тесты считаются на том же наборе графов, что и dfs
TEST_CASES_FOR_BFS = [
    Case(name='№1', input=dict_1, start_node='A', expected=res_1),
    Case(name='№2', input=dict_2, start_node='A', expected=res_2),
    Case(name='№3', input=dict_3, start_node='A', expected=res_3),
    Case(name='№4', input=dict_4, start_node='A', expected=res_4),
    Case(name='№5', input=dict_5, start_node='A', expected=res_5),
    Case(name='№6', input=dict_6, start_node='A', expected=res_6)
]


@pytest.mark.parametrize('bfs', TEST_CASES_FOR_BFS, ids=str)
def test_breadth_first_search(bfs: Case) -> None:
    graph = MyGraph(bfs.input)
    answer = graph.BFS(bfs.start_node)
    assert answer == bfs.expected


@pytest.mark.parametrize('dfs', TEST_CASES_FOR_DFS, ids=str)
def test_depth_first_search(dfs: Case) -> None:
    graph = MyGraph(dfs.input)
    answer = graph.DFS(dfs.start_node)
    assert answer == dfs.expected