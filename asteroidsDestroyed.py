def asteroidsDestroyed(mass,asteroid):
    # Sorting the asteroid list with O(nlogn)
    asteroid.sort()

    for astre in asteroid:
        if astre > mass:
            return False
        else:
            mass += astre

    return True


asteroidsDestroyed(5,[4,9,23,4])
