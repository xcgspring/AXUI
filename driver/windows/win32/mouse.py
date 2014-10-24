
import ctypes
from ctypes import \
    c_int, c_uint, c_long, c_ulong, c_void_p, c_wchar, c_char, \
    c_ubyte, c_ushort, c_wchar_p, \
    POINTER, sizeof, alignment, Union

SendInput           =   ctypes.windll.user32.SendInput
SetCursorPos        =   ctypes.windll.user32.SetCursorPos
GetSystemMetrics    =   ctypes.windll.user32.GetSystemMetrics

MOUSEEVENTF_LEFTUP = 4 # Variable c_int
MOUSEEVENTF_RIGHTUP = 16 # Variable c_int
MOUSEEVENTF_MIDDLEUP = 64 # Variable c_int

MOUSEEVENTF_LEFTDOWN = 2 # Variable c_int
MOUSEEVENTF_RIGHTDOWN = 8 # Variable c_int
MOUSEEVENTF_MIDDLEDOWN = 32 # Variable c_int

MOUSEEVENTF_MOVE = 1 # Variable c_int
MOUSEEVENTF_ABSOLUTE = 32768 # Variable c_int
MOUSEEVENTF_WHEEL = 2048 # Variable c_int

SM_SWAPBUTTON = 23 # Variable c_int

INPUT_MOUSE     = 0
INPUT_KEYBOARD  = 1
INPUT_HARDWARE  = 2

BOOL = c_int
BYTE = c_ubyte
CHAR = c_char
DWORD = c_ulong
HANDLE = c_void_p
HBITMAP = c_long
LONG = c_long
LPARAM = LONG
LPVOID = c_void_p
PVOID = c_void_p
UINT = c_uint
WCHAR = c_wchar
WORD = c_ushort
WPARAM = UINT


COLORREF = DWORD
HBITMAP = LONG
HINSTANCE = LONG
HMENU = LONG
HBRUSH = LONG
HTREEITEM = LONG
HWND = LONG
LPARAM = LONG
LPBYTE = POINTER(BYTE)
LPWSTR = c_long# POINTER(WCHAR)

class Structure(ctypes.Structure):
    "Override the Structure class from ctypes to add printing and comparison"
    #----------------------------------------------------------------
    def __str__(self):
        """Print out the fields of the ctypes Structure

        fields in exceptList will not be printed"""

        lines = []
        for f in self._fields_:
            name = f[0]
            lines.append("%20s\t%s"% (name, getattr(self, name)))

        return "\n".join(lines)

    #----------------------------------------------------------------
    def __eq__(self, other_struct):
        "return true if the two structures have the same coordinates"

        if isinstance(other_struct, ctypes.Structure):

            try:
                # pretend they are two structures - check that they both
                # have the same value for all fields
                are_equal = True
                for field in self._fields_:
                    name = field[0]
                    if getattr(self, name) != getattr(other_struct, name):
                        are_equal = False
                        break

                return are_equal

            except AttributeError:
                return False

        if isinstance(other_struct, (list, tuple)):
            # Now try to see if we have been passed in a list or tuple
            try:
                are_equal = True
                for i, field in enumerate(self._fields_):
                    name = field[0]
                    if getattr(self, name) != other_struct[i]:
                        are_equal = False
                        break
                return are_equal

            except:
                return False

        return False

# C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4283
class MOUSEINPUT(Structure):
    _pack_ = 2
    _fields_ = [
        # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4283
        ('dx', LONG),
        ('dy', LONG),
        ('mouseData', DWORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', DWORD),
    ]
assert sizeof(MOUSEINPUT) == 24, sizeof(MOUSEINPUT)
assert alignment(MOUSEINPUT) == 2, alignment(MOUSEINPUT)

# C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4292
class KEYBDINPUT(Structure):
    _pack_ = 2
    _fields_ = [
        # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4292
        ('wVk', WORD),
        ('wScan', WORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', DWORD),
    ]
assert sizeof(KEYBDINPUT) == 16, sizeof(KEYBDINPUT)
assert alignment(KEYBDINPUT) == 2, alignment(KEYBDINPUT)


class HARDWAREINPUT(Structure):
    _pack_ = 2
    _fields_ = [
        # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4300
        ('uMsg', DWORD),
        ('wParamL', WORD),
        ('wParamH', WORD),
    ]
assert sizeof(HARDWAREINPUT) == 8, sizeof(HARDWAREINPUT)
assert alignment(HARDWAREINPUT) == 2, alignment(HARDWAREINPUT)

# C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4314
class UNION_INPUT_STRUCTS(Union):
    _fields_ = [
        # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4314
        ('mi', MOUSEINPUT),
        ('ki', KEYBDINPUT),
        ('hi', HARDWAREINPUT),
    ]
assert sizeof(UNION_INPUT_STRUCTS) == 24, sizeof(UNION_INPUT_STRUCTS)
assert alignment(UNION_INPUT_STRUCTS) == 2, alignment(UNION_INPUT_STRUCTS)

class INPUT(Structure):
    _pack_ = 2
    _fields_ = [
        # C:/PROGRA~1/MICROS~4/VC98/Include/winuser.h 4310
        ('type', DWORD),
        # Unnamed field renamed to '_'
        ('_', UNION_INPUT_STRUCTS),
    ]
assert sizeof(INPUT) == 28, sizeof(INPUT)
assert alignment(INPUT) == 2, alignment(INPUT)



def SendMouseInput(
    coords,
    button = "left",
    double = False,
    button_down = True,
    button_up = True,
    wheel_dist = 0):
    """Peform a click action using SendInput

    All the *ClickInput() and *MouseInput() methods use this function.
    
    Thanks to a bug report from Tomas Walch (twalch) on sourceforge and code 
    seen at http://msdn.microsoft.com/en-us/magazine/cc164126.aspx this 
    function now always works the same way whether the mouse buttons are 
    swapped or not.
    
    For example if you send a right click to Notepad.Edit - it will always
    bring up a popup menu rather than 'clicking' it.
    """

    # Handle if the mouse buttons are swapped
    if GetSystemMetrics(SM_SWAPBUTTON):
        if button.lower() == 'left':
            button = 'right'
        else:
            button = 'left'

    events = []
    if button.lower() == 'left':
        if button_down:
            events.append(MOUSEEVENTF_LEFTDOWN)
        if button_up:
            events.append(MOUSEEVENTF_LEFTUP)
    elif button.lower() == 'right':
        if button_down:
            events.append(MOUSEEVENTF_RIGHTDOWN)
        if button_up:
            events.append(MOUSEEVENTF_RIGHTUP)
    elif button.lower() == 'middle':
        if button_down:
            events.append(MOUSEEVENTF_MIDDLEDOWN)
        if button_up:
            events.append(MOUSEEVENTF_MIDDLEUP)

    if button.lower() == 'wheel':
        events.append(MOUSEEVENTF_WHEEL)

    # if we were asked to double click (and we are doing a full click
    # not just up or down.
    if double and button_down and button_up:
        events *= 2

    # set the cursor position
    SetCursorPos(coords[0], coords[1])

    inp_struct = INPUT()
    inp_struct.type = INPUT_MOUSE

    for event in events:
        inp_struct._.mi.dwFlags = event
        if button.lower() == 'wheel':
            inp_struct._.mi.mouseData = wheel_dist
        else:
            inp_struct._.mi.mouseData = 0

        SendInput(
            1,
            ctypes.pointer(inp_struct),
            ctypes.sizeof(inp_struct))
