#include<iostream>
#include<string>
using namespace std;


class score
{private:
    static string classname;//静态成员
   //封装


public:
    int Chinese;
    int English;
    int Math;
    int Physics;
//构造函数
score()
{
   cout<<"学生成绩为"<<endl;
}
   

void print(){
//类内函数访问私有成员
   cout<<"班级为："<<classname<<endl;
}

   void show(){
      cout<<"语文成绩"<<Chinese<<"\n英语成绩"<< English<<"\n数学成绩"<<Math<<"\n物理成绩"<<Physics<<endl;
   }



   void end()
   {
      cout<<"考生的全部成绩输出完毕"<<endl;
   }

~score(){
   cout<<"输入完成"<<endl;
}
};
class phonenumber{
   //联系人
   string name;
   int number;
};

 //子类继承父类
class Student:public score
{public:
  string name;
   int id;
phonenumber phone;
void show2(){
   cout<<name<<id<<endl;
}

};
string score::classname="一班";


 //多态
 void test01(){
    Student s1;
s1.name="张三";
s1.id=01;
s1.show2();
s1.Chinese=100;
s1.English=90;
s1.Math=80;
s1.Physics=70;
s1.show();
s1.end();

Student s2;
s2.name="李四";
s2.id=02;
s2.show2();
s2.Chinese=60;
s2.English=50;
s2.Math=40;
s2.Physics=30;
s2.show();
s2.end();

}

int main(){
test01();
return 0;

}



