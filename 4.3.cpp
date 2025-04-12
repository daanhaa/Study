#include<iostream>
using namespace std;

int main(){
    int x = 100;
    int num = 1;

    //x보다 작으면 반복실행됨
    while(num < x){ 
        cout << "present num: " << num << "\n";
        num *= 2;
    }
}

//for문은 반복횟수가 명확할때 사용
//if문은 조건이 참일때 한번 실행