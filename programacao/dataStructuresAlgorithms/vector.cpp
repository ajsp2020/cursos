#include<iostream>
#include<vector>
using namespace std;

int main(){
    // Demo Vector
    //vector<int> arr = {1, 2, 10 , 12, 15};

    //Fill Constructor
    vector<int> arr(10,7);

    //Pop_back
    arr.pop_back();

    // Push_Back 0 (1) --> add an element
    arr.push_back(16);

    for(int x : arr){
        cout << x << ",";
    }

    // //Print all the elements
    // for(int i = 0; i < arr.size(); i++){
    //     cout<< arr[i] << endl;
    // }

    // // //Size of the vector (No of elements)
    // cout<<arr.size() <<endl;

    // //Capacity of the vector
    // cout <<arr.capacity() <<endl;

    return 0;
}