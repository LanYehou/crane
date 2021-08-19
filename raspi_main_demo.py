from visulpart import get_boxtype
import raspi_message
import threading
grayscale_sensor=[]
box=[]
storage_cache=[['0','0'],['0','0'],['0','0'],['0','0'],['0','0'],['0','0']]
stacking_area=['0','0','0']
mylocation_list=['location0','location1','location2','location3','location4','location5','location6','location7','location8','location9']
mylocation=0
status='stop'
what_todo_list=['take_first_box','take_second_box','laydown_box','goto_stacking_area','goto_storage_cache']
what_todo='take_first_box'
saved_box=[['0','0'],['0','0']]
def take_box():
    raspi_message.send_text('e')

def detect_box():
    boxcolor,boxtype,x,y= get_boxtype()
    storage_cache[mylocation][0] = boxcolor
    storage_cache[mylocation][1] = boxtype


def go_to_location(wish_location):
    if abs((wish_location-mylocation))>=2 :
        if wish_location > mylocation :
            raspi_message.send_text('c')
        elif wish_location < mylocation :
            raspi_message.send_text('d')
        while 1 :
            if abs(wish_location-mylocation) <2 :
                if wish_location > mylocation:
                    raspi_message.send_text('a')
                elif wish_location < mylocation:
                    raspi_message.send_text('b')
                return (1)



def main():
    while 1 :
        if stacking_area[0]=='0' or stacking_area[1]=='0' or stacking_area[2]=='0' :
            if what_todo == 'take_first_box' :
                for i in storage_cache :
                    if i[0]=='red' :
                        go_to_location(storage_cache.index(i))
                        take_box()
                        text=raspi_message.receive_text()
                        if text == 's':
                            what_todo='take_second_box'
                raspi_message.send_text('s')
                text = raspi_message.receive_text()
                if text == 's':
                    detect_box()
                    print(storage_cache)
                    return 0
            elif what_todo == 'take_second_dox'  :
                for i in storage_cache :
                    if i[1]==saved_box[0][1]:
                        go_to_location(storage_cache.index(i))
                        take_box()
                        text=raspi_message.receive_text()
                        if text == 's':
                            what_todo='laydown_box'
                            break
                raspi_message.send_text('a')
                text = raspi_message.receive_text()
                if text == 's':
                    detect_box()
            elif what_todo == 'laydown_box\n':
                go_to_location()
                text=raspi_message.receive_text()
                if text == 's':
                    raspi_message.send_text('laydown_box\n')
                    text=raspi_message.receive_text()
                    if text == 's':
                        what_todo = 'take_first_box\n'
                        pass

if __name__ == '__main__':
    main()