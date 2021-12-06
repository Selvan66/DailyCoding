#include "FaceDetectorCascade.h"
#include "opencv2/opencv.hpp"

FaceDetectorCascade::FaceDetectorCascade() : scale(1.1), minNeighbors(3), label("HaarCascadeDetector")
{
    classifier.load(FACE_DETECTION_HAARCASCADE);
    if (classifier.empty())
        throw std::invalid_argument("Cannot create Haar Cascade");
}

std::string FaceDetectorCascade::getLabel() const
{
    return label;
}

std::vector<cv::Rect> FaceDetectorCascade::detectFace(const cv::Mat& frame)
{
    std::vector<cv::Rect> ret;
    classifier.detectMultiScale(frame, ret, scale, minNeighbors, cv::CASCADE_SCALE_IMAGE, cv::Size(30, 30));
    return ret;
}

void FaceDetectorCascade::show(cv::Mat& frame)
{
    auto rectangles = detectFace(frame);
    cv::Scalar color(0x4B, 0xB7, 0x82);
    int frame_thickness = 4;
    for (const auto& r : rectangles)
    {
        cv::rectangle(frame, r, color, frame_thickness);
        std::string sizeText = std::to_string(r.size().width) + "x" + std::to_string(r.size().height);
        cv::putText(frame, sizeText, r.br(), cv::FONT_HERSHEY_SIMPLEX, 0.5, color);

        cv::Point labelPosition = r.tl();
        labelPosition.y -= 3;
        cv::putText(frame, label, labelPosition, cv::FONT_HERSHEY_SIMPLEX, 0.5, color);
    }
    imshow(label, frame);
}
