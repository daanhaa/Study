#include <iostream>
using namespace std;

int main(){
    int A,B;
    cout<<"A B: ";
    cin>>A >> B; //공백 구분하여 따로 저장

    for(int i=B; i>=A; i--){
        cout<<i<<" ";
    }
}