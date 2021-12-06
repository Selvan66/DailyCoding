#ifndef FACEDETECTOR_FACEDETECTORCASCADE_H
#define FACEDETECTOR_FACEDETECTORCASCADE_H

#include "opencv2/objdetect.hpp"

class FaceDetectorCascade
{
private:
    cv::CascadeClassifier classifier;
    const double scale;
    const int minNeighbors;
    const std::string label;
public:
    FaceDetectorCascade();
    std::vector<cv::Rect> detectFace(const cv::Mat& frame);
    void show(cv::Mat& frame);
    std::string getLabel() const;
};

#endif //FACEDETECTOR_FACEDETECTORCASCADE_H
