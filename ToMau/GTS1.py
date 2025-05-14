def gts1(graph = []):
    colors = []
    color = [-1] * len(graph)
    for i in range(len(graph)):
        color_used = []
        for neighbor in range(len(graph)):
            if color[neighbor] == -1 and graph[i][neighbor] == 1:
                color_used.append(color[neighbor])

        for i in range(len(graph)):
            if i not in color_used:
                colors.append(i)
                break
            
    return colors