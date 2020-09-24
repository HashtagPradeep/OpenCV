import cv2

# now read the video
my_video = cv2.VideoCapture('shortclip.mp4')
frame_width = int(my_video.get(3)) 
frame_height = int(my_video.get(4)) 
size = (frame_width, frame_height)
# cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter('gray_file.mp4',  
                         fourcc, 
                         10, size,0) 
# write a loop to show each video frame
while True:

    is_it_success, my_frame = my_video.read()
    gray = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
    if is_it_success == True:
        cv2.imshow('sssup', gray)
        result.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('get me a video')
        break
