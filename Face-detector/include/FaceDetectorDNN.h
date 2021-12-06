#ifndef FACEDETECTOR_FACEDETECTORDNN_H
#define FACEDETECTOR_FACEDETECTORDNN_H

#include <vector>

#include "opencv2/dnn.hpp"

class FaceDetectorDNN
{
private:
    cv::dnn::Net network;
    const int width;
    const int height;
    const double scale;
    const cv::Scalar mean_value;
    const float threshold;
    const std::string label;
public:
    FaceDetectorDNN();
    std::vector<cv::Rect> detectFace(const cv::Mat& frame);
    void show(cv::Mat& frame);
    std::string getLabel() const;
};


#endif //FACEDETECTOR_FACEDETECTORDNN_H
