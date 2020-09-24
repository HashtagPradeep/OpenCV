import cv2

# now read the video
my_video = cv2.VideoCapture('shortclip.mp4')

# write a loop to show each video frame
while True:

    is_it_success, my_frame = my_video.read(0)

    if is_it_success == True:
        cv2.imshow('sssup', my_frame)

        if cv2.waitKey(48) & 0xFF == ord('q'):
            break
    else:
        print('get me a video')
        break


