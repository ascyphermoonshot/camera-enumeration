import cv2
import sys

def testcam(camera):
    source = cv2.VideoCapture(camera)
    ret, frame = source.read()
    source.release()
    try:
        reso=frame.shape
        cv2.imshow('frame', frame)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    except:
        print("{} has no camera".format(camera))
        reso=None
    finally:
        return tuple((ret,reso))
if __name__ == '__main__':
    s = 0
    if len(sys.argv) > 1:
        s = sys.argv[1]
    cameras=[]
    for camnun in range(s,s+11):
        #print(camnun)
        success,resolution=testcam(camnun)
        if success:
            cameras.append(tuple((camnun,resolution)))
    print(cameras)