"""
DIGM 131 - Assignment 3: Function Library (scene_functions.py)
===============================================================

OBJECTIVE:
    Create a library of reusable functions that each generate a specific
    type of scene element. This module will be imported by main_scene.py.

REQUIREMENTS:
    1. Implement at least 5 reusable functions.
    2. Every function must have a complete docstring with Args and Returns.
    3. Every function must accept parameters for position and/or size so
       they can be reused at different locations and scales.
    4. Every function must return the name(s) of the Maya object(s) it creates.
    5. Follow PEP 8 naming conventions (snake_case for functions/variables).

GRADING CRITERIA:
    - [30%] At least 5 functions, each creating a distinct scene element.
    - [25%] Functions accept parameters and use them (not hard-coded values).
    - [20%] Every function has a complete docstring (summary, Args, Returns).
    - [15%] Functions return the created object name(s).
    - [10%] Clean, readable code following PEP 8.
"""

import maya.cmds as cmds

def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a simple building from a cube, placed on the ground plane.
    
    The building is a single scaled cube whose base sits at ground level
    (y = o) at the given position.
    
    Args: 
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.
    
    Returns:
        str: The name of the created building transform node.
    """
    
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
     
       cmds.move(x, height / 2.0, z, building)
        
        return building

    def create_tree(x, z, trunk_radius=0.3, trunk_height=3.0, canopy_radius=2.0):
        """Create a simple tree using a cylinder trunk and a sphere canopy.
        
        Args:
            trunk_radius (float): Radius of the cylindrical trunk.
            trunk_height (float): Height of the trunk cylinder.
            canopy_radius (float): Radius of the sphere used for the canopy.
            position (tuple): (x, y, z) ground-level position for the tree base.
       
        Returns:
           str: The name of a group node containing the trunk and canopy.
    """
    
    trunk = cmds.polyCylinder(
        radius=trunk_radius,
        height=trunk_height
        )[0]
    cmds.move(x, trunk_height / 2.0, z, trunk)
    
    canopy = cmds.polySphere(radius=canopy_radius)[0]    
    cmds.move(x, trunk_height + canopy_radius, z, canopy) 
    
    return tree_group
                

def create_fence(length=10, height=1.5, post_count=6, position=(0,0,0)):
    """Create a simple fence made of posts and rails.
    
    The fence runs along the X axis starting at the given position.
    
    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
    """
    
    spacing = length / (post_count - 1)
    parts = []

    for i in range(post_count):
        post = cmds.polyCube(w=0.2, h=height, d=0.2)[0]
        cmds.move(i * spacing, height / 2.0, 0, post)
        parts.append(post)

    rail = cmds.polyCube(w=length, h=0.2, d=0.2)[0]
    cmds.move(length / 2.0, height * 0.75, 0, rail)
    parts.append(rail)

    fence_group = cmds.group(parts, name="fence_grp")
    cmds.move(position[0], position[1], position[2], fence_group)

    return fence_group


def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    
     """Create a street lamp using a cylinder pole and a sphere light.

    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """
    pole = cmds.polyCylinder(r=0.1, h=pole_height)[0]
    cmds.move(0, pole_height / 2.0, 0, pole)

    light = cmds.polySphere(r=light_radius)[0]
    cmds.move(0, pole_height + light_radius, 0, light)

    lamp_group = cmds.group(pole, light, name="lamp_post_grp")
    cmds.move(position[0], position[1], position[2], lamp_group)

    return lamp_group


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                    **kwargs):
    """Place objects created by 'create_func' in a circular arrangement.

    Args:
        create_func (callable): Function that creates an object and accepts
            a 'position' argument.
        count (int): Number of objects to place.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Extra arguments passed to create_func.

    Returns:
        list: List of created object names.
    """
    results = []

    for i in range(count):
        angle = 2 * math.pi * i / count
        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)

        obj = create_func(position=(x, center[1], z), **kwargs)
        results.append(obj)
return results
