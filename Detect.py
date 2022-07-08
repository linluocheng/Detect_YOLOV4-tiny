import cv2

class Detect():
    def Detcetion(self, img):
        net = cv2.dnn.readNet("DetectModel/yolov4-tiny.weights", "DetectModel/yolov4-tiny.cfg")
        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(size=(320, 320), scale=1 / 255)
        classes = []
        with open("DetectModel/classes.txt", "r") as file_object:
            for class_name in file_object.readlines():
                class_name = class_name.strip()
                classes.append(class_name)

        frame = img
        (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
        ReturnList = []
        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h) = bbox
            class_name = classes[class_id]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            pt1, pt2 = (x, y), (x + w, y + h)
            text = class_name
            ReturnList.append(class_name)
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
            fontScale = 1
            thickness = 1
            retval, baseLine = cv2.getTextSize(text, fontFace=fontFace, fontScale=fontScale, thickness=thickness)
            topleft = (pt1[0], pt1[1] - retval[1])
            bottomright = (topleft[0] + retval[0], topleft[1] + retval[1])
            cv2.rectangle(frame, (topleft[0], topleft[1] - baseLine), bottomright, thickness=-1, color=(0, 255, 0))
            cv2.putText(frame, text + str(score), (pt1[0], pt1[1] - baseLine), fontScale=fontScale, fontFace=fontFace,
                        thickness=thickness, color=(0, 0, 0))
        return  frame, ReturnList
