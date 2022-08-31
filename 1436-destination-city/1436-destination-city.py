class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #collecting the departure cities
        departure = set()
        for cities in paths:
            departure.add(cities[0])
        for cities in paths:
            if cities[1] not in departure:
                return cities[1]
        
            
            
            