def get_data(file_data):
    row = -1
    graph = []
    with open(file=file_data) as file:
        row = int(file.readline())
        for i in range(row):
            line = file.readline().strip()
            numbers = list(map(int, line.split()))
            graph.append(numbers)
            
    return row, graph


def welsh_powell(graph = []):
    # Tính bậc đỉnh
    edges = {i: sum(graph[i]) for i in range(len(graph))}
    # Xắp xếp bậc đỉnh giảm dần
    sorted_edges = sorted(edges.items(), key=lambda x: x[1], reverse=True)
    
    colors = [-1] * len(graph)
    
    for edge in sorted_edges:
        index = edge[0] 
        color_used = []
        for neighbor in range(len(graph)):
            if colors[neighbor] != -1 and graph[index][neighbor] == 1:
                color_used.append(colors[neighbor])
        
        color = 0
        while color in color_used:
            color += 1
        
        colors[index] = color
        
    print(colors)

    return colors
            



if __name__ == '__main__':
    row, graph = get_data('color1.txt')
    colors = welsh_powell(graph=graph)
    print(max(colors) + 1)
    '''
    Tô màu: [0, 1, 2, 1, 2, 0, 2, 1]
Số màu cần: 3
'''
    
