# House Generator!


## Methods

* Room-first
    1. Generate rooms
    1. Stick them together
    1. Reshape rooms to fill in gaps
* Floor-first
    1. Generate house shell
    1. Draw walls in house to mark off spaces as rooms
* Movement graph
    1. Given a starting point (entrance door)
    1. generate a branching graph of rooms.
        * branching is based on room type
        * bedroom would probably be a leaf
        * hallways would have many branches
    1. Grow house from door inward


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

Easy way would be to align everything to a square-foot grid, 
but would only allow for boring floor plans, and walls 
wouldn't have thickness.  Not good enough for this project.

If I need to consider the 2D layout of a space is it useful 
to start with a graph?

What about the graph edges and vertices both being things?

```
example:
+ Door (key-locking, metal, external)
  + Hallway
    + Hallway2
      + folding double door
        - closet
      + folding double door
        - closet
      + standard door
        - bathroom
    - Kitchen
    - Flex space
    + bedroom
      + sliding door (locking, glass, external)
        - patio
```

### Models
* House
    * is a collection of polygons
* Room
    * is a polygon
    * shares some edges with other rooms
        * but maybe not the whole edge. (rooms shares part of hallway's edge)
* Architect
    * .generate_blueprints
        * no args
        * returns house
* Renderer 
    * https://svgwrite.readthedocs.io/en/master/
    * .render_to_svg
        * accepts house
        * accepts path
        * writes to file
        * returns none


This is the bottom line.