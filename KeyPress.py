# Given string
key_press_event = "<KeyPress event send_event=True state=Shift|Control keysym=Shift_L keycode=16 x=468 y=216>"

# Split the string by spaces
def get_pressed_status(event):
    result = {}
    for part in str(event).split():
        if 'state=' in part:
            state_value = part.split('=')[1]
            state_value = state_value.rstrip('>')
            result["state"] = state_value.split('|') if '|' in state_value else state_value

        if 'keysym=' in part:
            key_value = part.split('=')[1]
            key_value = key_value.rstrip('>')
            result["key"] = key_value

    return result