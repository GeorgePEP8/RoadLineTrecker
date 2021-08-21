import  cv2 as cv
import  numpy as np
import lanes

video = cv.VideoCapture("полоса 2.MP4")

if not video.isOpened():
    print("error while opening the video")

cv.waitKey(1) # минимальная задержка

while video.isOpened(): #пока видео открыто
    _, frame = video.read() # запись кадра

    #frame= frame[10:500, 500:2000] размер
    cv.namedWindow("Video", cv.WINDOW_NORMAL)
    cv.resizeWindow("Video",1300,800)

    copy_img = np.copy(frame)


    try:
        frame = lanes.canny(frame)
        frame = lanes.mask(frame)  # обрабатываем видео в чб
        lines = cv.HoughLinesP(frame, 2, np.pi / 180, 100, np.array([()]),
                                minLineLength=40,
                                maxLineGap=5)  # усредняем линии
        averaged_lines = lines.average_slope_intercept(frame, lines)
        line_image = lanes.display_lines(copy_img, averaged_lines)

        combo = cv.addWeighted(copy_img, 0.8, line_image, 0.5, 1)
        cv.imshow("Video", copy_img)

    except:
        pass





    if cv.waitKey(1) & 0xFF == ord('q'):#выход при нажатии q
        video.release()
        cv.destroyAllWindows()

video.release()
cv.destroyAllWindows()

