def show_in_explorer(arg1):
    """
    Shows a specified file in an OS browser and selects it.
    
    :param str arg1:
    """
    pass

def help():
    """
    CCommandDescription("Go to documentation...").GetDescription()
    """
    pass

def set_scale(arg1, arg2, arg3, arg4):
    """
    Sets the scale of ab object.
    
    :param str arg1:
    :param float arg2:
    :param float arg3:
    :param float arg4:
    """
    pass

def export_to_engine():
    """
    Exports the current level to the engine.
    
    :rtype: bool
    """
    pass

def is_helpers_shown():
    """
    Gets the display state of helpers.
    
    :rtype: bool
    """
    pass

def load_all_plugins():
    """
    Loads all available plugins.
    """
    pass

def set_parent_coordinates():
    """
    Use parent coordinates
    """
    pass

def create_object(arg1, arg2, arg3, arg4, arg5, arg6):
    """
    Creates a new object with given arguments and returns the name of the object.
    
    :param str arg1:
    :param str arg2:
    :param str arg3:
    :param float arg4:
    :param float arg5:
    :param float arg6:
    :rtype: PyGameObject
    """
    pass

def set_hidemask_none():
    """
    Sets the current hidemask to 'none'
    """
    pass

def find():
    """
    Find
    """
    pass

def set_custom_material(arg1, arg2):
    """
    Assigns a user material to a given object geometry.
    
    :param str arg1:
    :param str arg2:
    """
    pass

def get_entity_param(arg1, arg2):
    """
    Gets an object param
    
    :param str arg1:
    :param str arg2:
    :rtype: object
    """
    pass

def new_object(arg1, arg2, arg3, arg4, arg5, arg6):
    """
    Creates a new object with given arguments and returns the name of the object.
    
    :param str arg1:
    :param str arg2:
    :param str arg3:
    :param float arg4:
    :param float arg5:
    :param float arg6:
    :rtype: str
    """
    pass

def cut():
    """
    Cut
    """
    pass

def set_local_coordinates():
    """
    Use local coordinates
    """
    pass

def open_level_no_prompt(arg1):
    """
    Opens a level. Doesn't prompt user about saving a modified level
    
    :param str arg1:
    """
    pass

def select_and_go_to_object(arg1):
    """
    Selects and focuses camera on specified object.
    
    :param str arg1:
    """
    pass

def unselect_objects(arg1):
    """
    Unselects a list of objects.
    
    :param object arg1:
    """
    pass

def get_names_of_selected_objects():
    """
    Get the name from selected object/objects.
    
    :rtype: object
    """
    pass

def open_file_box():
    """
    Shows an open file box and returns the selected file path and name.
    
    :rtype: object
    """
    pass

def get_rotation(arg1):
    """
    Gets the rotation of an object.
    
    :param str arg1:
    :rtype: tuple
    """
    pass

def find_previous():
    """
    Find Previous
    """
    pass

def get_object_lods_count(arg1):
    """
    Gets the number of lods of the material of an object.
    
    :param str arg1:
    :rtype: int
    """
    pass

def save():
    """
    Save
    """
    pass

def combo_box(arg1, arg2, arg3):
    """
    Shows an combo box listing each value passed in, returns string value selected by the user.
    
    :param object arg1:
    :param object arg2:
    :param int arg3:
    :rtype: object
    """
    pass

def get_hidemask(arg1):
    """
    Gets the value of a specific object type in the current hidemask
    
    :param str arg1:
    :rtype: bool
    """
    pass

def open_pane(arg1):
    """
    Opens a view pane specified by the pane class name.
    
    :param str arg1:
    """
    pass

def get_pane_class_names():
    """
    Get all available class names for use with open_pane & close_pane.
    
    :rtype: object
    """
    pass

def rename_layer(arg1, arg2):
    """
    Renames layer with specific name.
    
    :param str arg1:
    :param str arg2:
    """
    pass

def select_objects(arg1):
    """
    Selects a list of objects.
    
    :param object arg1:
    """
    pass

def get_current_level_path():
    """
    Gets the fully specified path of the current level.
    
    :rtype: str
    """
    pass

def get_cvar(arg1):
    """
    Gets a cvar value as a string.
    
    :param str arg1:
    :rtype: str
    """
    pass

def unhide_all_objects():
    """
    Unhides all object.
    """
    pass

def set_current_view_rotation(arg1, arg2, arg3):
    """
    Sets the rotation of the current view as given x, y, z Euler angles.
    
    :param float arg1:
    :param float arg2:
    :param float arg3:
    """
    pass

def get_num_selected():
    """
    Returns the number of selected objects
    
    :rtype: int
    """
    pass

def draw_label(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    """
    Shows a 2d label on the screen at the given position and given color.
    
    :param int arg1:
    :param int arg2:
    :param float arg3:
    :param float arg4:
    :param float arg5:
    :param float arg6:
    :param float arg7:
    :param str arg8:
    """
    pass

def message_box(arg1):
    """
    Shows a confirmation message box with ok|cancel and shows a custom message.
    
    :param str arg1:
    :rtype: bool
    """
    pass

def generate_all_cubemaps():
    """
    Generates cubemaps for all environment probes in level.
    """
    pass

def freeze_object(arg1):
    """
    Freezes a specified object.
    
    :param str arg1:
    """
    pass

def get_all_objects_of_layer(arg1):
    """
    Gets all objects of a layer.
    
    :param str arg1:
    :rtype: object
    """
    pass

def enter_game_mode():
    """
    Enters the editor game mode.
    """
    pass

def get_scale(arg1):
    """
    Gets the scale of an object.
    
    :param str arg1:
    :rtype: tuple
    """
    pass

def is_object_hidden(arg1):
    """
    Checks if object is hidden and returns a bool value.
    
    :param str arg1:
    :rtype: bool
    """
    pass

def close():
    """
    Close
    """
    pass

def generate_cubemap(arg1):
    """
    Generates a cubemap (only for environment probes).
    
    :param str arg1:
    """
    pass

def get_object_type(arg1):
    """
    Gets the type of an object as a string.
    
    :param str arg1:
    :rtype: object
    """
    pass

def freeze_layer(arg1):
    """
    Freezes layer with specific name.
    
    :param str arg1:
    """
    pass

def get_object_parent(arg1):
    """
    Gets parent name of an object.
    
    :param str arg1:
    :rtype: str
    """
    pass

def get_default_material(arg1):
    """
    Gets the default material of a given object geometry.
    
    :param str arg1:
    :rtype: object
    """
    pass

def set_config_spec(arg1):
    """
    Sets the system config spec.
    
    :param int arg1:
    """
    pass

def open():
    """
    Open...
    """
    pass

def start_object_creation(arg1, arg2):
    """
    Creates a new object, which is following the cursor.
    
    :param str arg1:
    :param str arg2:
    """
    pass

def delete_layer(arg1):
    """
    Delete layer with specific name.
    
    :param str arg1:
    """
    pass

def exit():
    """
    Exits the editor.
    """
    pass

def set_cvar(arg1, arg2):
    """
    Sets a cvar value from an integer, float or string.
    
    :param str arg1:
    :param object arg2:
    """
    pass

def save_level():
    """
    Saves the current level.
    
    :rtype: bool
    """
    pass

def new():
    """
    New...
    """
    pass

def set_result_to_failure():
    """
    Sets the result of a script execution to failure. Used only for Sandbox AutoTests.
    """
    pass

def take_screenshot():
    """
    Saves the screenshot of the currently active window.
    """
    pass

def get_assigned_material(arg1):
    """
    Gets the name of assigned material.
    
    :param str arg1:
    :rtype: object
    """
    pass

def set_view_coordinates():
    """
    Use view coordinates
    """
    pass

def set_entity_property(arg1, arg2, arg3):
    """
    Sets an entity property or property2
    
    :param str arg1:
    :param str arg2:
    :param object arg3:
    """
    pass

def get_flowgraphs_using_this(arg1):
    """
    Gets the name list of all flow graphs which control this object.
    
    :param str arg1:
    :rtype: object
    """
    pass

def undo():
    """
    Undoes the last operation
    """
    pass

def get_all_layers():
    """
    Gets the list of all layer names in the level.
    
    :rtype: object
    """
    pass

def unhide_layer(arg1):
    """
    Unhides layer with specific name.
    
    :param str arg1:
    """
    pass

def set_object_layer(arg1, arg2):
    """
    Moves an object to an other layer.
    
    :param object arg1:
    :param str arg2:
    """
    pass

def get_current_level_name():
    """
    Gets the name of the current level.
    
    :rtype: str
    """
    pass

def paste():
    """
    Paste
    """
    pass

def get_axis_constraint():
    """
    Gets axis.
    
    :rtype: str
    """
    pass

def export_level_settings():
    """
    Saves the global level settings.
    """
    pass

def get_edit_mode():
    """
    Gets edit mode
    
    :rtype: str
    """
    pass

def get_world_position(arg1):
    """
    Gets the world position of an object.
    
    :param str arg1:
    :rtype: tuple
    """
    pass

def is_in_game_mode():
    """
    Queries if it's in the game mode or not.
    
    :rtype: bool
    """
    pass

def hide_all_objects():
    """
    Hides all objects.
    """
    pass

def set_entity_param(arg1, arg2, arg3):
    """
    Sets an object param
    
    :param str arg1:
    :param str arg2:
    :param object arg3:
    """
    pass

def set_current_view_position(arg1, arg2, arg3):
    """
    Sets the position of the current view as given x, y, z coordinates.
    
    :param float arg1:
    :param float arg2:
    :param float arg3:
    """
    pass

def detach_object(arg1):
    """
    Detaches object from its parent
    
    :param str arg1:
    """
    pass

def suspend_game_input():
    """
    Suspend game input and allow editor to tweak properties
    """
    pass

def add_entity_link(arg1, arg2, arg3):
    """
    Adds an entity link to objectName to targetName with name
    
    :param str arg1:
    :param str arg2:
    :param str arg3:
    """
    pass

def hide_object(arg1):
    """
    Hides a specified object.
    
    :param str arg1:
    """
    pass

def select_layer(arg1):
    """
    Selects the layer with the given name.
    
    :param str arg1:
    """
    pass

def set_selection_mask(arg1):
    """
    Sets the selection mask for the level editor
    
    :param int arg1:
    """
    pass

def open_level(arg1):
    """
    Opens a level.
    
    :param str arg1:
    """
    pass

def get_selection_aabb():
    """
    Returns the aabb of the selection group
    
    :rtype: tuple
    """
    pass

def set_hidemask_invert():
    """
    Inverts the current hidemask
    """
    pass

def set_hidemask_all():
    """
    Sets the current hidemask to 'all'
    """
    pass

def get_entity_geometry_file(arg1):
    """
    Gets the geometry file name of a given entity.
    
    :param str arg1:
    :rtype: object
    """
    pass

def get_current_view_position():
    """
    Returns the position of the current view as a list of 3 floats.
    
    :rtype: tuple
    """
    pass

def redo():
    """
    Redoes the last undone operation
    """
    pass

def hide_layer(arg1):
    """
    Hides layer with specific name.
    
    :param str arg1:
    """
    pass

def save_as():
    """
    Save As...
    """
    pass

def log(arg1):
    """
    Prints the message to the editor console window.
    
    :param str arg1:
    """
    pass

def zoom_in():
    """
    CCommandDescription("Zoom In").GetDescription()
    """
    pass

def attach_object(arg1, arg2, arg3, arg4):
    """
    Attaches object with childObjectName to parentObjectName. If attachmentType is 'CharacterBone' or 'GeomCacheNode' attachmentTarget specifies the bone or node path
    
    :param str arg1:
    :param str arg2:
    :param str arg3:
    :param str arg4:
    """
    pass

def get_pak_from_file(arg1):
    """
    Finds a pak file name for a given file
    
    :param str arg1:
    :rtype: str
    """
    pass

def edit_box_check_data_type(arg1):
    """
    Shows an edit box and checks the custom value to use the return value with other functions correctly.
    
    :param str arg1:
    :rtype: object
    """
    pass

def duplicate():
    """
    Duplicate
    """
    pass

def get_all_objects(arg1, arg2):
    """
    Gets the name list of all objects of a certain type in a specific layer or in the whole level if an invalid layer name given.
    
    :param object arg1:
    :param object arg2:
    :rtype: object
    """
    pass

def run_file_parameters(arg1, arg2):
    """
    Runs a script file with parameters. A relative path from the editor user folder or an absolute path should be given as an argument. The arguments should be separated by whitespace.
    
    :param str arg1:
    :param str arg2:
    """
    pass

def get_selection_center():
    """
    Returns the center point of the selection group
    
    :rtype: tuple
    """
    pass

def create_layer(arg1):
    """
    Creates new layer with specific name and returns bool value if layer was created or not.
    
    :param str arg1:
    :rtype: bool
    """
    pass

def set_world_coordinates():
    """
    Use world coordinates
    """
    pass

def zoom_out():
    """
    CCommandDescription("Zoom Out").GetDescription()
    """
    pass

def get_object_children(arg1):
    """
    Gets children names of an object.
    
    :param str arg1:
    :rtype: object
    """
    pass

def cycle_displayinfo():
    """
    Cycle display info.
    """
    pass

def create_level(arg1, arg2, arg3, arg4):
    """
    Creates a level with the parameters of 'levelName', 'resolution', 'unitSize' and 'bUseTerrain'.
    
    :param str arg1:
    :param int arg2:
    :param int arg3:
    :param bool arg4:
    :rtype: int
    """
    pass

def set_entity_geometry_file(arg1, arg2):
    """
    Sets the geometry file name of a given entity.
    
    :param str arg1:
    :param str arg2:
    """
    pass

def copy():
    """
    Copy
    """
    pass

def get_entity_property(arg1, arg2):
    """
    Gets an entity property or property2
    
    :param str arg1:
    :param str arg2:
    :rtype: object
    """
    pass

def set_rotation(arg1, arg2, arg3, arg4):
    """
    Sets the rotation of the object.
    
    :param str arg1:
    :param float arg2:
    :param float arg3:
    :param float arg4:
    """
    pass

def set_result_to_success():
    """
    Sets the result of a script execution to success. Used only for Sandbox AutoTests.
    """
    pass

def message_box_yes_no(arg1):
    """
    Shows a confirmation message box with yes|no and shows a custom message.
    
    :param str arg1:
    :rtype: bool
    """
    pass

def unfreeze_layer(arg1):
    """
    Unfreezes layer with specific name.
    
    :param str arg1:
    """
    pass

def import_level_settings():
    """
    Loads and sets the global level settings.
    """
    pass

def set_hidemask(arg1, arg2):
    """
    Assigns a specified value to a specific object type in the current hidemask
    
    :param str arg1:
    :param bool arg2:
    """
    pass

def unhide_object(arg1):
    """
    Unhides a specified object.
    
    :param str arg1:
    """
    pass

def find_next():
    """
    Find Next
    """
    pass

def delete():
    """
    Delete
    """
    pass

def select_object(arg1):
    """
    Selects a specified object.
    
    :param str arg1:
    """
    pass

def delete_object(arg1):
    """
    Deletes a specified object.
    
    :param str arg1:
    """
    pass

def execute_command(arg1):
    """
    Executes a given string as an editor command.
    
    :param str arg1:
    """
    pass

def nav_insert_point(arg1, arg2, arg3, arg4, arg5):
    """
    Added a point at the given position to the given nav area
    
    :param str arg1:
    :param int arg2:
    :param float arg3:
    :param float arg4:
    :param float arg5:
    """
    pass

def run_lua(arg1):
    """
    Runs a lua script command.
    
    :param str arg1:
    """
    pass

def edit_box(arg1):
    """
    Shows an edit box and returns the value as string.
    
    :param str arg1:
    :rtype: object
    """
    pass

def toggle_helpers():
    """
    Toggles the display of helpers.
    """
    pass

def set_position(arg1, arg2, arg3, arg4):
    """
    Sets the position of an object.
    
    :param str arg1:
    :param float arg2:
    :param float arg3:
    :param float arg4:
    """
    pass

def get_object_layer(arg1):
    """
    Gets the name of the layer of an object.
    
    :param object arg1:
    :rtype: object
    """
    pass

def get_materials(arg1 [, arg2]]):
    """
    
    
    :param   (object arg1 [:
    :param bool arg2]]:
    :rtype: lis
    """
    pass

def select_all():
    """
    Select All
    """
    pass

def set_custom_coordinates():
    """
    Use custom coordinates
    """
    pass

def get_game_folder():
    """
    Gets the path to the Game folder of current project.
    
    :rtype: object
    """
    pass

def create_sw_level(arg1, arg2, arg3, arg4, arg5):
    """
    Creates a level with the parameters of 'levelName', 'unitSize', 'segmentSize', 'segmentX', 'segmentY' and 'bUseSegmentedTerrain.
    
    :param str arg1:
    :param int arg2:
    :param int arg3:
    :param int arg4:
    :param int arg5:
    :rtype: int
    """
    pass

def unfreeze_object(arg1):
    """
    Unfreezes a specified object.
    
    :param str arg1:
    """
    pass

def get_current_view_rotation():
    """
    Returns the rotation of the current view as a list of 3 floats, each of which represents x, y, z Euler angles.
    
    :rtype: tuple
    """
    pass

def focus_level_editor():
    """
    Brings the level editor window to frotn
    """
    pass

def message_box_ok(arg1):
    """
    Shows a confirmation message box with only ok and shows a custom message.
    
    :param str arg1:
    :rtype: bool
    """
    pass

def get_name_of_selected_layer():
    """
    Returns the name of the selected layer.
    
    :rtype: str
    """
    pass

def get_position(arg1):
    """
    Gets the position of an object.
    
    :param str arg1:
    :rtype: tuple
    """
    pass

def set_axis_constraint(arg1):
    """
    Sets axis.
    
    :param object arg1:
    """
    pass

def clear_selection():
    """
    Clears selection.
    
    :rtype: int
    """
    pass

def is_layer_exist(arg1):
    """
    Checks existence of layer with specific name.
    
    :param str arg1:
    :rtype: bool
    """
    pass

def run_console(arg1):
    """
    Runs a console command.
    
    :param str arg1:
    """
    pass

def get_names_of_all_layers():
    """
    Get a list of all layer names in the level.
    
    :rtype: object
    """
    pass

def exit_game_mode():
    """
    Exits the editor game mode.
    """
    pass

def run_file(arg1):
    """
    Runs a script file. A relative path from the editor user folder or an absolute path should be given as an argument
    
    :param str arg1:
    """
    pass

def new_object_at_cursor(arg1, arg2, arg3):
    """
    Creates a new object at a position targeted by cursor and returns the name of the object.
    
    :param str arg1:
    :param str arg2:
    :param str arg3:
    :rtype: str
    """
    pass

def unload_all_plugins():
    """
    Unloads all available plugins.
    """
    pass

def idle_wait(arg1):
    """
    Waits idling for a given seconds. Primarily used for auto-testing.
    
    :param float arg1:
    """
    pass

def get_custom_material(arg1):
    """
    Gets the user material assigned to a given object geometry.
    
    :param str arg1:
    :rtype: object
    """
    pass

def set_coord_sys(arg1):
    """
    Sets the coordinate system to use for level editor
    
    :param int arg1:
    """
    pass

def rename_object(arg1, arg2):
    """
    Renames object with oldObjectName to newObjectName
    
    :param str arg1:
    :param str arg2:
    """
    pass

def set_edit_mode(arg1):
    """
    Sets edit mode
    
    :param object arg1:
    """
    pass

