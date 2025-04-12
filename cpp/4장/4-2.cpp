#include<iostream>
using namespace std;

int main(){
    int a, b;

    cout<<"start point: ";
    cin >> a;

    cout<<"end point: ";
    cin >> b;

    for(int i=a; i<b; i++){
        cout << i << "\n";
    }
}