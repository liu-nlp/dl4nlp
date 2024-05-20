def heads_to_graph(heads):
    graph = {h: set() for h in range(len(heads) + 1)}
    for word, head in enumerate(heads, start=1):
        graph[head].add(word)
    return graph


def graph_properties(graph):
    # Depth-first search
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not dfs(neighbor, node):
                    return False
            elif neighbor != parent:
                return False
        return True

    visited = set()

    # acyclic? connected?
    return dfs(0, None), len(visited) == len(graph)


DN = +1
SH = 0
UP = -1


def traverse(heads):
    marked = [False] * len(heads)
    cursor = 0
    marked[cursor] = True
    for i in range(len(heads)):
        bend = i
        path = []
        while not marked[bend]:
            path.append(bend)
            bend = heads[bend]
        while cursor != bend:
            yield cursor, UP
            marked[cursor] = False
            cursor = heads[cursor]
        while len(path) > 0:
            cursor = path.pop()
            marked[cursor] = True
            yield cursor, DN
        yield cursor, SH
        assert cursor == i
    while cursor != 0:
        yield cursor, UP
        marked[cursor] = False
        cursor = heads[cursor]


def is_projective(heads):
    heads = [0] + heads
    seen = [False] * len(heads)
    for cursor, d in traverse(heads):
        if d == DN:
            if seen[cursor]:
                return False
            else:
                seen[cursor] = True
    return True


if __name__ == '__main__':
    import json
    import sys

    n_graphs = 0

    statistics = {
        'total': 0,
        'gold': {'acyclic': 0, 'connected': 0, 'tree': 0, 'projective': 0},
        'pred': {'acyclic': 0, 'connected': 0, 'tree': 0, 'projective': 0},
    }

    with open(sys.argv[1]) as fp:
        for line in fp:
            gold_heads, pred_heads = json.loads(line.rstrip())
            gold_graph = heads_to_graph(gold_heads)
            pred_graph = heads_to_graph(pred_heads)

            statistics['total'] += 1

            is_acyclic_gold, is_connected_gold = graph_properties(gold_graph)
            statistics['gold']['acyclic'] += is_acyclic_gold
            statistics['gold']['connected'] += is_connected_gold
            statistics['gold']['tree'] += is_acyclic_gold and is_connected_gold
            if is_acyclic_gold and is_connected_gold:
                statistics['gold']['projective'] += is_projective(gold_heads)

            is_acyclic_pred, is_connected_pred = graph_properties(pred_graph)
            statistics['pred']['acyclic'] += is_acyclic_pred
            statistics['pred']['connected'] += is_connected_pred
            statistics['pred']['tree'] += is_acyclic_pred and is_connected_pred
            if is_acyclic_pred and is_connected_pred:
                statistics['pred']['projective'] += is_projective(pred_heads)

    print(statistics)
