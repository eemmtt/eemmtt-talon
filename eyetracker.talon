#Commands for Eyetracker
# tracking.control_enabled()
# tracking.control_gaze_toggle()
# tracking.control_head_toggle()
# tracking.control_mouse_jump_toggle()
# tracking.control_toggle()
# tracking.control_zoom_enabled()
# tracking.control_zoom_toggle()

-

key(ctrl-alt-f): 
    user.mouse_reset(10,10)
    tracking.control_toggle()
key(ctrl-alt-g): tracking.control_gaze_toggle()
key(ctrl-alt-c): tracking.calibrate()
key(ctrl-alt-j): tracking.control_mouse_jump_toggle()

#experiment with home footpedal
key(f24:down): user.mouse_hover("start")
key(f24:up): user.mouse_hover("stop")
