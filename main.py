# This is a sample Python script.
from graph import Graph
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##################################
    #Graph of WORD vertices
    def buildGraph(wList):
        d = {}
        g = Graph()
        # phân hoạch các từ cùng độ dài chỉ khác nhau 1 ký tự
        for line in wList:  # lấy từng từ trong từ điển
            word = line[:]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
                    # thêm các đỉnh và các cạnh cho các từng trong cùng bucket
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
        return g

    # main
    wList = ["FOOD", "FOOT", "FOOL", "FORT",
             "GOOD",
             "PALE", "PALM", "POLE", "POLL", "POOL",
             "SAGE", "SALE", "SALT"]
    g = buildGraph(wList)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

    #Uncomment to run
    #BFS
    #g.bfs(g.vertList['FOOD'])
    #g.traverse(g.vertList['SAGE'])

    #DFS
    #g.resetColornPred()
    #g.dfs(g.vertList['FOOD'])
    #g.traverse(g.vertList['SAGE'])

    ##################################
    #Graph of number vertices
    g2 = Graph()
    g2.loadFromTextFile('input/exp1.txt')
    g2.is_direct = True

    #Uncomment to run
    #g2.bfs(g2.vertList['0'])
    #g2.traverse(g2.vertList['0'])

    g2.resetColornPred()
    g2.dfs(g2.vertList['0'])
    g2.traverse(g2.vertList['0'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
