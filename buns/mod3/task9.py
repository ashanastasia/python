def find_robot_coordinates(n):
    x = 0
    y = 0
    direction = 0
    current_step = 0
    
    while current_step < n:
        if direction == 0:
            x -= 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x += 1
        elif direction == 3:
            y += 1
            
        if (current_step + 1) % 2 == 0: 
            direction = (direction + 1) % 4
            
        current_step += 1
    
    return x, y


n = int(input())  
x, y = find_robot_coordinates(n)
print(x, y)
