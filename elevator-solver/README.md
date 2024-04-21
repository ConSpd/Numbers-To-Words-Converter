# Building evacuation using DFS, BFS and BestFS Algorithms

_"A building gets set on fire and there's an elevator with capacity of 10 persons. 
The elevator moves automatically to evacuate the residents as optimally as possible"_

The state of the problem is depicted in the following vector.
`[0, 12, 3, 7, 8, 0]`

Each index represents:
1. The floor in which the elevator is at that moment
2. Number of Residents on First Floor
3. Number of Residents on Second Floor
4. Number of Residents on Third Floor
5. Number of Residents on Fourth Floor
6. The passengers inside the elevator

The state that we wish to achieve is `[0, 0, 0, 0, 0, 0]`

The script evacuates the residents by using Depth-First Search, Breadth-first Search and Best-First Search _(depending on what the user picks)_ 
showing in each approach how the elevator moves.

### Screenshots of script Running
<img width="350" alt="image" src="https://github.com/ConSpd/python-miniprojects/assets/74179715/cc285912-3053-4a34-b621-48006dbeb827"><br>
<img width="350" alt="image" src="https://github.com/ConSpd/python-miniprojects/assets/74179715/c0291c9f-bfd5-4823-8d87-ef5092a24e68"><br>
<img width="350" alt="image" src="https://github.com/ConSpd/python-miniprojects/assets/74179715/cebc6a32-cb87-4b21-a2f4-2631ca51627b"><br>


We can change the number of residents in each floor as we will.
