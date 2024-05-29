def count_collisions(robots):
    collisions = [0] * len(robots)
    
    for i in range(len(robots)):
        for j in range(i+1, len(robots)):
            if robots[i] != robots[j]:
                distance = abs(i - j)
                if distance % 2 == 0:
                    collisions[i] += 1
                    collisions[j] += 1
                
    return collisions
	
#Para ejecutar las pruebas de unidad, se puede utilizar el siguiente código de ejemplo:

 
def test_count_collisions():
    assert count_collisions(['R', 'L', 'R', 'L', 'R']) == [2, 2, 2, 0, 0]
    assert count_collisions(['R', 'R', 'R', 'R', 'R']) == [4, 0, 0, 0, 0]
    assert count_collisions(['L', 'L', 'L', 'L', 'L']) == [0, 0, 0, 0, 4]

if __name__ == "__main__":
    test_count_collisions()
    print("All tests passed")
