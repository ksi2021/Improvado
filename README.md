# Improvado


#include <iostream>
#include <cmath>
using namespace std;

int main()
{
//    cout << "Hello World!" << endl;
//    float x,result;
//    cin >> x;
//    result = (pow(x,2) + cos(x+3)) / ( sqrt(x+1));
//    cout<<endl<<result;


//    float x,result;
//    cin >> x;
//    result = sin(pow(x,2)+2*x-1) / ( sqrt(x+2)  - 2);
//    cout<<endl<<result;


    //1
      cout<<"****"<<endl<<"*"<<endl<<"*"<<endl<<"*"<<endl<<"*"<<endl<<"****";
    //2
       int radius;
       cout<<endl<<"input radius"<<endl;
       cin>> radius;
       cout<<"\n S = "<< 3.14 * pow(radius,2)<<endl;
       cout<<"\n P = "<< 2 * 3.14 * radius <<endl;

    //3
       float a,b;
       cin >> a >> b;
       b=b+a;
       a=b-a;
       b=b-a;
    //4
       float a,b;
       cin >> a >> b;
       float r = (a+4*b)*(a-3*b)+pow(a,2);
       cout<<endl<<r;
    //5
        float distance;
        int emmiter;
        float result;
        cout<< "\n input distance (meter)"<< endl;
        cin >> distance;
        cout<< "choose a convert type: \n  1 - km, 2 - versti \n";
        cin >> emmiter;
        switch (emmiter) {
        case 1:
            distance/=1000;
            break;
        case 2:
            
            break;
        default:
            break;
        }
    //6
       float arr[3];
       for(int i = 0 ; i < 3; i++) cin >> arr[i];
       float temp = arr[0];
       for(int i = 1 ; i < 3; i++) if(arr[i] > temp) temp= arr[i];
       cout << endl<< temp;
    return 0;
}
