def findMinArrowShots(points):
        # Sort the balloons based on their end coordinates
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        prevEnd = points[0][1]
        
        # Count the number of non-overlapping intervals
        for i in range(1, len(points)):
            if points[i][0] > prevEnd:
                arrows += 1
                prevEnd = points[i][1]
        
        return arrows
findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])