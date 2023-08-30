import cv2 as cv
from dotenv import load_dotenv

load_dotenv()

H, W = 480, 640
CONTOUR_AREA = 500


def get_source():
    capture = cv.VideoCapture(0)
    if not capture.isOpened():
        print("Failed to open video stream")
        return None

    return capture


def is_valid_contour_area(contour):
    if cv.contourArea(contour) < CONTOUR_AREA * 4:
        return True

    return False


def process_frames(source):
    # bg_substractor = cv.createBackgroundSubtractorMOG2()
    bg_substractor = cv.createBackgroundSubtractorKNN()

    first_frame = None
    while True:
        ret, frame = source.read()
        key = cv.waitKey(1)
        if not ret or ord("q") == key or frame is None:
            source.release()
            break

        frame = cv.resize(frame, (W, H))
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (21, 21), 0)
        if first_frame is None:
            first_frame = blur
            continue

        # frame_delta = cv.absdiff(first_frame, blur)
        # thresh = cv.threshold(frame_delta, 25, 255, cv.THRESH_BINARY)[1]
        # dilated = cv.dilate(thresh, None, iterations=2)
        # contours, _ = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # for cnt in contours:
        #     if cv.contourArea(cnt) < CONTOUR_AREA:
        #         continue

        #     x, y, w, h = cv.boundingRect(cnt)
        #     cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # ref - https://docs.opencv.org/3.4/d1/dc5/tutorial_background_subtraction.html
        # as long as there is movement in the image, we can expect to find contours in the frame
        fg_mask = bg_substractor.apply(blur)
        fgmask_contours, _ = cv.findContours(fg_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cnt in fgmask_contours:
            if cv.contourArea(cnt) < CONTOUR_AREA * 4:
                continue

            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # cv.rectangle(frame, (10, 2), (100, 20), (0, 0, 255), 2)
        # cv.putText(
        #     frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)),
        #     (15, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0)
        # )
        yield frame, fg_mask, fgmask_contours



def main():
    source = get_source()
    if source is None:
        return 1

    for fg_mask, frame, contours in process_frames(source):
        print(contours)

        cv.imshow("Frame", frame)
        # cv.imshow('frame delta', frame_delta)
        # cv.imshow('thresh', thresh)
        cv.imshow("FG Mask", fg_mask)

    cv.destroyAllWindows()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
