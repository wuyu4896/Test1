// #include <opencv2/opencv.hpp>

// int main() {
//     cv::Mat img = cv::imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg");
  
//     cv::Mat gray;
//     cv::cvtColor(img, gray, cv::COLOR_BGR2GRAY);
//     cv::imwrite("gray.png", gray);
//     return 0;
// }
// ---------------------------------------------------------------------
// #include <opencv2/opencv.hpp>

// int main() {
//     cv::Mat img = cv::imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg");

//     cv::Mat hsv_img, mask;
//     cv::cvtColor(img, hsv_img, cv::COLOR_BGR2HSV);
//     cv::inRange(hsv_img, cv::Scalar(0, 0, 200), cv::Scalar(179, 30, 255), mask);
//     img.setTo(cv::Scalar(0, 0, 0), mask);
    
//     cv::namedWindow("hsv", cv::WINDOW_NORMAL);
//     cv::imshow("hsv", img);
//     cv::waitKey(0);
//     return 0;
// }
// //-----------------------------------------------------------------


// #include <opencv2/opencv.hpp>
// #include <vector>

// int main() {
//     // 读取图像
// cv::Mat img = cv::imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg");
    
//     // 分离通道
// std::vector<cv::Mat> channels;
// cv::split(img, channels);
//     // 保存
// cv::imwrite("r_channel.png", channels[2]);  // R通道
// cv::imwrite("g_channel.png", channels[1]); // G通道 
// cv::imwrite("b_channel.png", channels[0]); // B通道

    
//     return 0;
// }

// //----------------------------------------------------



// #include <opencv2/opencv.hpp>
// #include <vector>

// int main() {
//     cv::Mat img = cv::imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg");
  
//     cv::Mat gray, thresh, dilated;
//     cv::cvtColor(img, gray, cv::COLOR_BGR2GRAY);
//     cv::threshold(gray, thresh, 240, 255, cv::THRESH_BINARY_INV);
    
//     cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(5, 5));
//     cv::dilate(thresh, dilated, kernel, cv::Point(-1, -1), 2);
    
//     std::vector<std::vector<cv::Point>> contours;
//     cv::findContours(dilated, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);
    
//     for (const auto& cnt : contours) {
//         cv::drawContours(img, std::vector<std::vector<cv::Point>>{cnt}, -1, cv::Scalar(0, 0, 255), 2);
//     }
    
//     cv::imwrite("huakuang.png", img);
//     return 0;
// }


// #------------------------------------------------------------------

#include <opencv2/opencv.hpp>

int main() {
    cv::Mat img = cv::imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg");
    
//旋转计算中心点
    cv::Point2f center(img.cols / 2.0f, img.rows / 2.0f);
    cv::Mat M = cv::getRotationMatrix2D(center, 45, 1.0);
    cv::Mat rotated;
    cv::warpAffine(img, rotated, M, img.size());
    
    cv::imwrite("xuuanzhuan.png", rotated);
    return 0;
}