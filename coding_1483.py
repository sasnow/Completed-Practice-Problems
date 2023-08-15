"""
A competitive runner would like to create a route that starts and ends at his house, with the 
condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths 
between some of these locations to their corresponding distances, find the length of the shortest 
route satisfying the condition above. Assume the runner's home is location 0.


"""
import sys

class RouteHolder:
    def __init__(self, initialsteps):
        self.routes = {}
        self.distances = {}
        self.keys = []
        self.i = 1
        for x in initialsteps:
            self.addPath(x,initialsteps[x])
            
    def __str__(self):
        return str({tuple(self.routes[x]):self.distances[x] for x in self.keys})
       
    def addPath(self,route,distance):
        thiskey = "route" + str(self.i)
        self.routes[thiskey] = list(route)
        self.distances[thiskey] = distance
        self.keys.append(thiskey)
        self.i += 1
     
    def delPath(self, key):
        self.routes.pop(key)
        self.distances.pop(key)
        self.keys.remove(key)
        
    def getLeastPath(self):
        mindist = sys.maxsize
        minkey = ""
        for x in self.keys:
            if self.distances[x] < mindist:
                mindist = self.distances[x]
                minkey = x
        return {tuple(self.routes[minkey]),self.distances[minkey]}
        
        



def verifyElevation(route, elevations):
    """
        go up until change in direction
        return false if second change found
        return true if done
    """
    goingdownhill = False
    prevelev = elevations[0]
    for phase in route[1:]:
        if goingdownhill and elevations[phase] > prevelev:
            # supposed to be going downhill but next stop is uphill
            return False
        if elevations[phase] < prevelev:
            # downhill starting
            goingdownhill = True
        # continue uphill
        prevelev = elevations[phase]
    return True
   
def generateRoutes(paths,buildingroutes,elevations):
    """
        go through all connections from home     
        get first stops
        ...
        for all n stops
        if n is 0
            return route
        else
            get n -> k stops
    """
    connections = buildingroutes.routes
    lastcontinues = -1
    routesremain = True
    while routesremain:
        print("------------------------------------------")
        print(buildingroutes)
        ctcontinues = 0
        currentkeys = buildingroutes.keys
        for x in currentkeys:
            currentroute = buildingroutes.routes[x]
            currentdist = buildingroutes.distances[x]
            currentstop = currentroute[len(currentroute) - 1]
            if currentstop == 0:
                #route is already done
                if verifyElevation(currentroute,elevations):
                    ctcontinues += 1
                else:
                    print("deletion here")
                    print(currentroute)
                    buildingroutes.delPath(x)
            else:
                nextstops = [x[1] for x in paths.keys() if x[0] == currentstop]
                if len(nextstops) > 0:
                    buildingroutes.routes[x] = buildingroutes.routes[x] + [nextstops[0]]
                    buildingroutes.distances[x] += paths[(currentstop,nextstops[0])]
                if len(nextstops) > 1:
                    for k in nextstops[1:]:
                        newpath = currentroute + [k]
                        newdist = currentdist + paths[(currentstop,k)]
                        buildingroutes.addPath(newpath, newdist)
        if ctcontinues == lastcontinues:
            routesremain = False
        else:
            lastcontinues = ctcontinues
    print(buildingroutes)
    return buildingroutes.getLeastPath()
                        
    
    
    
        
        











elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

firststops = RouteHolder({(0,x[1]):paths[x] for x in paths.keys() if x[0] == 0})
print(generateRoutes(paths,firststops,elevations))
