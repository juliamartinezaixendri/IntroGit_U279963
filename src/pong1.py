def get_config() -> tuple[int, int, int, int, int]:


    
    """ Ask the user whether they want to modify the main game parameters:
    (paddle height, paddle speed, ball X speed, ball Y speed, and ball radius).
   
    If the user chooses **not** to open the configuration menu, the function
    simply returns the default constant values defined at the top of the program:
        (PADDLE_H, SPEED_PADDLE, SPEED_BALL_X, SPEED_BALL_Y, BALL_RADIUS)

    If the user answers **yes**, the function should:
      - For each configurable value, call `read_int_in_range()` to ask for a new number
        within reasonable limits (for example: paddle height between 60-160).
      - Collect the five resulting integers and return them together in the following order:
            (paddle_height, paddle_speed, ball_x_speed, ball_y_speed, ball_radius)

    Parameters
    ----------
    None

    Returns
    -------
    int, int, int, int, int : 
        the selected configuration values in the specified order ->
        paddle_height, paddle_speed, ball_x_speed, ball_y_speed, ball_radius

    Notes and hints
    ---------------
    - Use `ask_yes_no(prompt)` to decide whether to open the menu.
    - Use `read_int_in_range(prompt, low, high)` to read each numeric value.
    - Keep the function free of global assignments: it should only **return**
      the chosen values, not modify constants.
    - Remember to maintain the same order of the returned elements.
    """

    # TODO: put your code!!!!

    # This line of code has been left for letting the full program work
    # It corresponds to the user answering NO to changing any default values 
    # You will need to eliminate it when adding your code
    return PADDLE_H, SPEED_PADDLE, SPEED_BALL_X, SPEED_BALL_Y, BALL_RADIUS 