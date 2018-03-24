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

## Rooms


