from typing import List # Tuple, Set, etc

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg([10,15])