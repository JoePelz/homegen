# House Generator!


## Methods

* ~Room-first~
    1. Generate rooms
    1. Stick them together
    1. Reshape rooms to fill in gaps
* ~Floor-first~
    1. Generate house shell
    1. Draw walls in house to mark off spaces as rooms
* ~Movement graph~
    1. Given a starting point (entrance door)
    1. generate a branching graph of rooms.
        * branching is based on room type
        * bedroom would probably be a leaf
        * hallways would have many branches
    1. Grow house from door inward
* Graph and Grid
    1. Given a starting point
    1. Build a graph of the paths a person could take through the house. i.e. which rooms connect to which others.
    1. Draw a convex hull around the house
        1. Make wall. Mark as exterior wall.
        1. Problem: entrance may not be on the convex hull
    1. crop overlapping rooms to belong to the room closest to their entrance door
    1. grow rooms to fill convex hull. Put walls at meeting places between rooms
    1. simplify walls (less zigzagging and fewer small walls).


## Components

### Rooms
* Kitchen
* Bedroom
* Bathroom (min 72" x 72")
* Dining Room
* Social Room
* Flex space
* Work room
* Hallway (min 43" x 43")
* Boot room

### Walls
* internal (5" thick)
* external (9" thick)

### Passages < Walls
* External door (35.75" wide)
* Standard door (30" wide)
* Door hole without door
* Arched opening
* Double doors
* French doors
* Folding closet door (3" thick)
* sliding closet door (3" thick)

### Barriers < Walls
* solid wall
* half wall, only: internal
* wall with window (bay window)
* wall with frosted window

### Architectural Decorations
* square windows
* floor-to-ceiling windows
* baseboards
* crown molding
* brick wall
* fireplace

## Program Structure

Version 1 is a single 2D floor.

Will be following the graph & grid approach
```
Example:
- Door (key-locking, metal, external)
 \- Hallway
  |-- Hallway2
  | |-- Folding double door
  | |  \- Closet
  | |-- Folding double door
  | |  \- Closet
  |  \- Standard door
  |    \- Bathroom
  |-- Kitchen
  |-- Flex space
   \- Bedroom
     \- Sliding door (locking, glass, external)
       \- Patio
```

### Idea
Create a Domain Specific Language, like in a yaml file, that lets 
1. you specify 
    * rooms: names, occurrences (number/range), constraints (size/shape) 
    * specify any other constraints, like overall square footage
    * define styles as well (colors, materials, molding)
2. Then in the app you load that definition file, and click "Generate"
3. The app returns or saves the svg file. 
