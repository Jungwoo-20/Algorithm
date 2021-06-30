def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for i in tickets:
        routes[i[0]] = routes.get(i[0], []) + [i[1]]
    for i in routes:
        routes[i].sort(reverse=True)
    stk = ['ICN']
    path = []
    while stk:
        top = stk[-1]
        if top in routes and routes[top]:
            stk.append(routes[top].pop())
        else:
            path.append(stk.pop())
    return path[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

solution(tickets)
