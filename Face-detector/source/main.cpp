#include "opencv2/opencv.hpp"
#include "FaceDetectorDNN.h"
#include "FaceDetectorCascade.h"

int main()
{
    cv::VideoCapture video_capture;
    if (!video_capture.open(0))
        return 0;

    FaceDetectorDNN detectorDnn;
    FaceDetectorCascade detectorCascade;
    cv::Mat frame;
    while (true)
    {
        video_capture >> frame;
        cv::Mat copyFrame = frame.clone();

        detectorCascade.show(frame);
        detectorDnn.show(copyFrame);

        if (cv::waitKey(10) == 27)
            break;

        try
        {
            cv::getWindowImageRect(detectorDnn.getLabel());
            cv::getWindowImageRect(detectorCascade.getLabel());
        }
        catch (...)
        {
            break;
        }
    }

    cv::destroyAllWindows();
    video_capture.release();
    return 0;
}