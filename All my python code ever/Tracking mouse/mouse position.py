import win32api
import time
import os.path


file_counter = 0
save_path = 'C:\Python34\Scripts\Tracking mouse\mouse_coords_file'


while True:
    file_counter = file_counter +1
    a = 0
    while a < 1800:
        a = a + 1
        x, y = win32api.GetCursorPos()
        coords = str(x)+" "+str(y)                                                              #tidy this chunk up
        complete_file = os.path.join(save_path,"mouse_coords{0}.txt".format(file_counter))
        with open(complete_file, 'a') as coords_file:
            coords_file.write(coords+"\n")
        time.sleep(0.03)

#win32api.SetCursorPos((10,10))