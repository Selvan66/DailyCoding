#include "FaceDetectorDNN.h"

#include "opencv2/opencv.hpp"

FaceDetectorDNN::FaceDetectorDNN() : threshold(0.5), height(300), width(300), scale(1.0), mean_value(104.0, 177.0, 123.0), label("FaceDetectorDNN")
{
    network = cv::dnn::readNetFromCaffe(FACE_DETECTION_CONFIGURATION, FACE_DETECTION_WEIGHTS);
    if (network.empty())
        throw std::invalid_argument("Cannot create DNN");
}

std::vector<cv::Rect> FaceDetectorDNN::detectFace(const cv::Mat& frame)
{
    cv::Mat blob = cv::dnn::blobFromImage(frame, scale, cv::Size(width, height), mean_value);
    network.setInput(blob, "data");
    cv::Mat detection = network.forward("detection_out");
    cv::Mat detection_matrix(detection.size[2],detection.size[3], CV_32F,detection.ptr<float>());
    std::vector<cv::Rect> faces;

    for (int i = 0; i < detection_matrix.rows; i++)
    {
        float confidence = detection_matrix.at<float>(i, 2);
        if (confidence < threshold)
            continue;

        int x_left_bottom = static_cast<int>(detection_matrix.at<float>(i, 3) * frame.cols);
        int y_left_bottom = static_cast<int>(detection_matrix.at<float>(i, 4) * frame.rows);
        int x_right_top = static_cast<int>(detection_matrix.at<float>(i, 5) * frame.cols);
        int y_right_top = static_cast<int>(detection_matrix.at<float>(i, 6) * frame.rows);
        faces.emplace_back(x_left_bottom, y_left_bottom,(x_right_top - x_left_bottom),(y_right_top - y_left_bottom));
    }

    return faces;
}

void FaceDetectorDNN::show(cv::Mat& frame)
{
    auto rectangles = detectFace(frame);
    cv::Scalar color(0x54, 0xA2, 0xD2);
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

std::string FaceDetectorDNN::getLabel() const
{
    return label;
}

