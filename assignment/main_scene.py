"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import scene_functions as sf

cmds.file(new=True, force=True)

ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

b1 = sf.create_building(width=4, height=8, depth=4, position=(0, 0, 0))
b2 = sf.create_building(width=5, height=4, depth=7, position=(-5, 0, 15))
b3 = sf.create_building(width=7, height=14, depth=4, position=(-10, 0, 10))

park_trees = sf.place_in_circle(
    sf.create_tree,
    count=8,
    radius=12,
    center=(0, 0, 0),
    trunk_height=3.0
)
 

t1 = sf.create_tree(position=(8, 0, -12))
t2 = sf.create_tree(position=(-8, 0, -4))

fence = sf.create_fence(length=20, post_count=8, position=(-3, 0, -9))

lamp1 = sf.create_lamp_post(position=(4, 0, 3))
lamp2 = sf.create_lamp_post(position=(11, 0, 9))
lamp3 = sf.create_lamp_post(position=(9, 0, 2))
lamp4 = sf.create_lamp_post(position=(2, 0, -3))

if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
